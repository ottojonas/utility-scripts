from rembg import remove
from PIL import Image

inputPath = ""
outputPath = ""
inp = Image.open(inputPath)
output = remove(inp)
output.save(outputPath)
