# -*- coding: utf-8 -*-

from PIL import Image

IMG = "5.JPG"
WIDTH = 200
HEIGHT = 100


ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):  # alpha(灰度）
    if alpha == 0:                # 如果灰度是0，说明这里没有图片
        return ' '
    length = len(ascii_char)      # 计算这些字符的长度
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b) # RGB转灰度
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)] # 这个相当于是选出了灰度与哪个字符对应

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST) # 更改图片的显示比例

    txt = ""

    for i in range(HEIGHT):   # i代表纵坐标
        for j in range(WIDTH): # j代表横坐标
            # 把图片按照横纵坐标解析成r,g,b以及alpha这几个参数，然后调用get_char函数，把对应的图片转换成灰度值，把对应值得字符存入txt中
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    #print txt

    # 字符画输出到文件
    output = IMG + ".txt"
    with open(output, 'w') as f:
            f.write(txt)