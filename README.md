# Rule_skills_test


## Description

When given a set of PNG/XML file pairs, this Python script will highlight leaf level UI components specified in the XML file with a dotted yellow line. Designed with XML files captured from android using the dump feature of the uiautomator framework in Android. Input data is placed into the `/input/` directory. The output PNGs are placed into the `/output/` directory. 

## To Run

Requires [Pillow](https://pillow.readthedocs.io/en/stable/), which should be installed by default on most Linux distributions. 

To install pillow,
```
pip install Pillow
```

Place XML/PNG pairs into `/input/`. Run on Mac or Linux with 
```
python3 Rule_skills_test.py
``` 

If on Windows, use 
```
py Rule_skills_test.py
```

## Reasoning

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
