cadena =" "
def rgb(r, g, b):
    if r >= 255:
      cadena.__add__("FF")
    elif 0 < r < 255 :
      cadena.__add__(r/2)
    else:
      cadena.__add__("00")
    if g >= 255:
      cadena.__add__("FF")
    elif 0 < g < 255 :
      cadena.__add__(g/2)
    else:
      cadena.__add__("00")
    if b >= 255:
      cadena.__add__("FF")
    elif 0 < b < 255 :
      cadena.__add__(b/2)
    else:
      cadena.__add__("00")
    return cadena
print(rgb(255, 255, 255))