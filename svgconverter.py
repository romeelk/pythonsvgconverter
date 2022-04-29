import os
import cairosvg

def traverse_folder(folder,count):
    global file_count
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if(os.path.isdir(path)):
            print(path)
            traverse_folder(path,count)
        else:
            if(path.endswith(".svg")):
                print(f"Found svg file {path}")
                convert_svg_to_png(path)
                file_count+=1
                print(file_count)
   

def convert_svg_to_png(file_path):
    svg_file = os.path.basename(file_path)
    png_file = os.path.dirname(file_path) + "/" +os.path.splitext(svg_file)[0] + ".png"
    cairosvg.svg2png(url=file_path, write_to=png_file,scale=5)

path_to_svg = input("Enter path to svg images:")


if(not os.path.exists(path_to_svg)):
    print(f"The path:{path_to_svg} cannot be found")

file_count=0
traverse_folder(path_to_svg,file_count)
print(f"Processed {file_count} svg files")
   


