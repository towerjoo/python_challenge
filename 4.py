#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 4
# Link: http://www.pythonchallenge.com/pc/def/linkedlist.php
# Date: 2012-07-10 11:49
#######################################################

src = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%(nothing)s"
def main():
    # main logic to solve problem 4 with link http://www.pythonchallenge.com/pc/def/linkedlist.php
    nothing = "12345"
    link = src % {"nothing" : nothing}
    def find(link):
        import urllib2, re
        fh = urllib2.urlopen(link)
        cont = fh.read()
        fh.close()
        out = "".join(re.findall(r"([0-9]+)", cont))
        if out:
            print out
            find(src % {"nothing" : out})
        else:
            print cont
    find(src)



if __name__ == "__main__":
    main()
