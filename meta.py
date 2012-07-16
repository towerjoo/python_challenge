#coding=utf-8

###########################################################################
# This source file is to generate the skeleton to solve the challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# Date: 2012-07-10 10:41 
###########################################################################


skeleton = """#coding=utf-8

#######################################################
# Source file is to solve the python challenge
# Author: Tower Joo<zhutao.iscas@gmail.com>
# No.: %(number)s
# Link: %(link)s
# Date: %(date)s
#######################################################

def main():
    # main logic to solve problem %(number)s with link %(link)s
    pass

if __name__ == "__main__":
    main()
"""

import sys
from datetime import datetime
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--link", dest="link", help="link of the question")
parser.add_option("-n", "--number", dest="number", help="number of this question")

(options, args) = parser.parse_args()

if options.link and options.number:
    answer_file_name = "%s.py" % options.number
    import os
    if os.path.exists(answer_file_name):
        print "The file with name %s already exists!" % answer_file_name
        sys.exit(0)
    else:
        fh = open(answer_file_name, "w")
        now = datetime.now()
        now_str = now.strftime("%Y-%m-%d %H:%M")
        cont = skeleton % ({"link" : options.link, "number" : options.number, "date" : now_str})
        fh.write(cont)
        fh.close()
        print "The file with name %s has been generated successfully!" % answer_file_name
        sys.exit(0)
else:
    print "Please specify the link and number of the question at first!"
    parser.print_help()
    sys.exit(0)

