#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: 5
# Link: http://www.pythonchallenge.com/pc/def/peak.html
# Date: 2012-07-10 11:57
#######################################################

def main():
    # main logic to solve problem 5 with link http://www.pythonchallenge.com/pc/def/peak.html
    import pickle
    fh = open("banner.p")
    cont = fh.read()
    fh.close()
    out = pickle.loads(cont)
    for item in out:
        s = ""
        for tup in item:
            s += tup[0] * tup[1]
        print s


if __name__ == "__main__":
    main()
