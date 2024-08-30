# Camron Rule
# Fall 2024
# Software Engineering programming assignment 1

import glob # pull file names
from PIL import Image, ImageDraw # draw on PNGs

def main():

    #Ensure that input PNGs can be overwritten
    print('\n-WARNING-')
    print('The output from this script will overwrite the original PNGs, placing the highlighted squares on the input PNGs')
    print('Is this ok? Y/N')
    if input().capitalize() != 'Y':
        return
    
    #Find all file names ending with .xml in this directory
    files = []
    for f in glob.glob("*.xml"):
        files.append(f)

    #For each .xml file
        #split on '/>'    -> cut off at the end of each leaf node
        #split on '<node' -> isolate this leaf node from its parents
        #check if 'bounds' is in the string to avoid the closing tags causing problems

    for f in files:
        bounds = []
        with open(f, "r") as filename:
            print('\nopened '+f)
            text = filename.read().split('/>')
            for t in text:

                t = t.split('<node')[-1]

                if 'bounds' in t:           
                    #isolates the bounds of the leaf node
                    #trims the string into 4 tuple of (0,1,2,3)
                    t = t.split('bounds=')
                    if '][' in t[0]: t = t[0]
                    else: t = t[1]
                    bounds.append(eval(t.split('"')[1].replace('][', ',').strip('[]')))    

        #print the coordinates of leaf nodes that were found
        print(bounds)

        # https://www.geeksforgeeks.org/python-pillow-imagedraw-module/
        img_name = f[:-3]+'png'
        img = Image.open(img_name)
        draw = ImageDraw.Draw(img)

        for bound in bounds:

            SKIP = False #boolean that switches on each line draw, to create a dotted effect
            DOT_WIDTH = 10 #size of the spacing between each dot on the dotted line
            LINE_WIDTH = 10 #size of the pen to draw the dotted line

            x_cur = bound[0]
            y_cur = bound[1]

            x_end = bound[2]
            y_end = bound[3]

            #draw two lines in x dir
            while x_cur <= x_end:
                SKIP = not SKIP
                if not SKIP:
                    draw.line((x_cur, y_cur, x_cur+DOT_WIDTH, y_cur), width=LINE_WIDTH, fill='yellow')
                    draw.line((x_cur, y_end, x_cur+DOT_WIDTH, y_end), width=LINE_WIDTH, fill='yellow')
                x_cur += DOT_WIDTH

            #reset x start coordinate
            x_cur = bound[0]
           
            #draw two lines in y dir
            while y_cur <= y_end:
                SKIP = not SKIP
                if not SKIP:
                    draw.line((x_cur, y_cur, x_cur, y_cur+DOT_WIDTH), width=LINE_WIDTH, fill='yellow')
                    draw.line((x_end, y_cur, x_end, y_cur+DOT_WIDTH), width=LINE_WIDTH, fill='yellow')  
                y_cur += DOT_WIDTH
                
        img.show()
        img.save(img_name)

if __name__ == "__main__":
    main()