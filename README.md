# Rule_skills_test
Software Engineering programming assignment 1

#Description

When given a set of PNG/XML file pairs, this Python script will highlight leaf level UI components specified in the XML file with a dotted yellow line. Designed with XML files captured from android using the dump feature of the uiautomator framework in Android. The output PNG overwrites the input PNG. Store the input PNGs outside of the current working directory if the original copies are needed.

#To Run

No external dependencies required. Makes use of the Python Pillow library to modify images. Place the script Rule_skills_test.py into the same directory as the data, and run with `py Rule_skills_test.py`

#Reasoning

The flow of the script is:
    - Gather file names for each XML/PNG pair
    - For each file pair:
        - Decide which UI elements have no children and store the relevant coordinates
        - Open the corresponding PNG
        - For each set of coordinates of a leaf element:
            - Draw many small yellow lines surrounding this element, with an offset between them
        - Show and save the PNG

I encountered two issues:
    1. An error in one of the XML files. I was planning on using the ElementTree XML parser but had to figure out how to manually parse the XML files using Python string functions.
    2. The Python Pillow library does not natively have the functionality to draw a dotted line. Instead of just calling the function to draw a rectangle, I had to instead draw many small lines with offsets between them to mimic a dotted line.