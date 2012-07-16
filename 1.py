#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 1
# Link: http://www.pythonchallenge.com/pc/def/map.html
# Date: 2012-07-10 10:48
#######################################################

def main():
    # main logic to solve problem 1 with link http://www.pythonchallenge.com/pc/def/map.html
    src = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    # rules: K->M  O->Q E->G
    offset = 2
    def convert(char):
        if char < 'a' or char > 'z':
            return char
        new = ord(char) + offset
        new = new - ord('z') + ord('a') -1 if new > ord('z') else new
        return chr(new)
    dst = ''.join([convert(x) for x in src])
    print dst
    src = "map"
    dst = ''.join([convert(x) for x in src])
    print dst

def main2():
    # for improvement
    import string
    offset = 2
    table = string.maketrans(string.ascii_lowercase, 
            string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset])
    src = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print string.translate(src, table)
    print string.translate("map", table)



if __name__ == "__main__":
    main()
    main2()
