#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 8
# Link: http://www.pythonchallenge.com/pc/def/integrity.html
# Date: 2012-07-10 16:57
#######################################################

def main():
    # main logic to solve problem 8 with link http://www.pythonchallenge.com/pc/def/integrity.html
    un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
    pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
    import bz2
    print bz2.decompress(un)
    print bz2.decompress(pw)

if __name__ == "__main__":
    main()
