import rembg
from rembg import remove
import easygui
from PIL import Image

inputPath = easygui.fileopenbox(title='Select image file')
outputPath = easygui.filesavebox(title='save file to ..')

input = Image.open(inputPath)
output=remove(input)
output.save(outputPath)
