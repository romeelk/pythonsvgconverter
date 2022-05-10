import os
import sys
import cairosvg

"""
Given a path recurse through each folder until no
more subdirectories found
"""
def traverse_folder(folder,count):
    global file_count
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if(os.path.isdir(path)):
            traverse_folder(path,count)
        else:
            if(path.endswith(".svg")):
                print(f"Found svg file {path}")
                convert_svg_to_png(path)
                file_count+=1
                print(file_count)
   

def convert_svg_to_png(file_path):
    try:
        svg_file = os.path.basename(file_path)
        png_file = os.path.dirname(file_path) + "/" +os.path.splitext(svg_file)[0] + ".png"
        cairosvg.svg2png(url=file_path, write_to=png_file,scale=5)
        print(f"Successfully converted {svg_file}")
    except Exception as exception:
        print(f"Could not convert svg file:{svg_file}",exception)


path_to_svg = input("Enter path to svg images:")

if(not os.path.exists(path_to_svg)):
    print(f"The path:{path_to_svg} cannot be found")
    sys.exit(-1)

file_count=0
traverse_folder(path_to_svg,file_count)
print(f"Processed {file_count} svg files")
   


