from PIL import Image
import pyperclip as ppc

gray_scale = ["@@", "%%", "##", "**", "++", "==", "--", "::", "..", "  "]


img = Image.open("cr7.png")
img_cinza = img.convert("L")
img_cinza = img_cinza.resize((600, 600))

img_cinza.save("cr7cinza.png")

pixels = img_cinza.load()
txt = ""
print(img_cinza.size)
for y in range(img_cinza.height):
    for x in range(img_cinza.width):
        txt += gray_scale[min(int(pixels[x, y] / 256 * len(gray_scale)), len(gray_scale) - 1)]
    txt += "\n"
    
img_cinza.show()
ppc.copy(txt)
print("Arte Ascii copiada para sua área de transferência!")

