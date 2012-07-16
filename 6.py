#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 6
# Link: http://www.pythonchallenge.com/pc/def/channel.html
# Date: 2012-07-10 12:04
#######################################################

import zipfile

def main():
    # main logic to solve problem 6 with link http://www.pythonchallenge.com/pc/def/channel.html
    fh = zipfile.ZipFile("channel.zip")
    filename = "90052"
    def find(fn):
        cont = fh.read("%s.txt" % fn)
        import re
        next_f = "".join(re.findall(r"([0-9]+)", cont))
        if next_f:
            find(next_f)
        else:
            print cont
    find(filename)

    comment = ""
    def get_comment(comm, fn):
        info = fh.getinfo("%s.txt" % fn)
        comm += info.comment
        cont = fh.read("%s.txt" % fn)
        import re
        next_f = "".join(re.findall(r"([0-9]+)", cont))
        if next_f:
            return get_comment(comm, next_f)
        return comm
    print get_comment(comment, filename)


if __name__ == "__main__":
    main()
