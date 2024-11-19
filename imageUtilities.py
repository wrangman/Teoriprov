'''
IAMGE-UTILITES.PY: Methods that are shared over different classes/files

__author__  = "Johan Wrangö"
__version__ = "1.0.0"
__email__   = "johan.wrango@ga.ntig.se"
'''


from PIL import Image, ImageTk

@staticmethod
def open_image(image):
    try: 
        temp_image = Image.open(image)
        new_width = 314
        width_percent = (new_width / float(temp_image.size[0]))
        new_height = int(float(temp_image.size[1]) * float(width_percent))
         
        temp_image = temp_image.resize((new_width, new_height))
        temp_image = ImageTk.PhotoImage(temp_image)
        return temp_image
    except FileNotFoundError:
        return None
