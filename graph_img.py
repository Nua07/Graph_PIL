import numpy as np
import math
from PIL import ImageDraw, Image
import io

def Graph(exp, xSize, ySize):
    img = Image.new("RGBA", (1000,1000), (0,0,0,0))
    draw=ImageDraw.Draw(img)
    draw.rectangle(((0, 00), (1000, 1000)), fill="white")

    draw.line((500, 0, 500,1000) , fill="black")
    draw.line((0, 500, 1000, 500) , fill="black")

    lx=-1
    ly=-1

    for x in range(-500, 500+1, 2):
        try:
            y=eval(exp)
            if lx==-1 and ly==-1:
                lx=x+500
                ly=y+500

            draw.line((lx, ly, round(x+500), round(-y+500)), fill="black")
            lx=x+500
            ly=-y+500
        except Exception as e:
            print(e)
            pass
    
    out=io.BytesIO()
    img.save(out, "PNG")

    return out.getvalue()
