#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 7
# Link: http://www.pythonchallenge.com/pc/def/hockey.html
# Link: http://www.pythonchallenge.com/pc/def/oxygen.html
# Date: 2012-07-10 14:52
#######################################################

def main():
    # main logic to solve problem 7 with link http://www.pythonchallenge.com/pc/def/hockey.html
    # main logic to solve problem 7 with link http://www.pythonchallenge.com/pc/def/oxygen.html
    import Image
    im = Image.open("oxygen.png")
    width, height = im.size
    o_x, o_y = 0, 0
    o_pixel = None
    need_break = False
    for x in range(width):
        if need_break:
            break
        for y in range(height):
            pix = im.getpixel((x, y))
            if pix[0] == pix[1] == pix[2]:
                o_y = y
                need_break = True
                break
            else:
                o_x = x
                o_y = y
                o_pixel = im.getpixel((o_x, o_y))

    print o_y
    row = [im.getpixel((x, o_y)) for x in range(0, width, 7)]
    ords = [r for r, g, b, a in row if r == g == b]
    out = "".join(chr(x) for x in ords)
    result = out[out.index("["):]
    result = result[1:-1].split(",")
    result = [x.strip() for x in result]
    print "".join([chr(int(x)) for x in result])

if __name__ == "__main__":
    main()
