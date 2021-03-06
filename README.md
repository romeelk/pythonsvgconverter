# pythonsvgconverter

Python script to convert svg to png given a folder

## Pre-requesites

You will need latest Python installed.

Create a virtual environment and activate in the directory.

```
python3 -m venv env
source env/bin/activate
```

## Packages

This script uses cairosvg python package to render png from svg.
Make sure you have all the pre-requesite dependancies installed on
your flavour of OS otherwise pip will fail to install.

On mac os you must install these packages via brew:

```
brew install cairo
```

```
pip3 install cairosvg
pip freeze > requirements.txt
```

## Simple test in Python interpreter

Try the following on an input svg file

```
python3
cairosvg.svg2png(url='image.svg', write_to='image.png')
```

This will generate a sample png file from a image.svg file in this repository.

## Execute the code

To execute the Python script point to a folder with svg files in it.

Run the following script passing a path to a folder. The script will recurse
through the folders looking for svg file. If a file is found it will be converted and written to the same folder but with the same file name with a png extension:


```
python3 svgconverter.py
Enter path to svg images:/Users/auser/Downloads/Icons           
Processed 10 svg files
```
