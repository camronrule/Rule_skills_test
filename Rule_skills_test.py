# Camron Rule
# Fall 2024
# Software Engineering programming assignment 1

import glob # pull file names
import os # check on dirs

# to install Pillow if not already installed
import sys
import subprocess

def checkPillowInstalled():
    try:
        from PIL import Image, ImageDraw # draw on PNGs
        print('Pillow module found\n')
    except:
        print('Pillow not installed... installing with pip\n')
        python = sys.executable
        subprocess.check_call([python, '-m', 'pip', 'install', 'Pillow'])



def createDirectories():
    if not os.path.isdir('input'):
        raise NotADirectoryError('No input directory found')

    #Deal with input/output folders
    if not os.path.isdir('output'):
        os.mkdir('output')

    else: # if output folder exists, remove all files in it
        output_files = glob.glob('/output/*')
        for f in output_files:
            os.remove(f)
    return



#For each .xml file in ./input/
    #split on '/>'    -> cut off at the end of each leaf node
    #split on '<node' -> isolate this leaf node from its parents
    #check if 'bounds' is in the string to avoid the closing tags causing problems
def findAllLeafCoordinatesinFile(f):
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
    print('Coordinates of leaf nodes:\n{}'.format(bounds))
    return bounds



def drawDottedRectangle(bound, img, draw):
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



def main():

    checkPillowInstalled()

    createDirectories()

    #Find all file names ending with .xml in ./input/
    files = []
    for f in glob.glob("input/*.xml"):
        files.append(f)

    print('Files found:{}'.format(files))

    for f in files:
        bounds = []
        bounds = findAllLeafCoordinatesinFile(f)

        # https://www.geeksforgeeks.org/python-pillow-imagedraw-module/
        img_name = f[:-3]+'png'
        img = Image.open(img_name)
        draw = ImageDraw.Draw(img)

        for bound in bounds:
            drawDottedRectangle(bound, img, draw)

        #img.show()
        img.save('output/'+img_name.strip('/input')) # save changed image into output folder



if __name__ == "__main__":
    main()