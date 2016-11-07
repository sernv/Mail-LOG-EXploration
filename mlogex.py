#version 5.0

import sys
import re
import gzip

class bcolors:
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

if len(sys.argv) < 3:
   print ("Syntax Error: Exim logs file or email address was not entered in the following syntax: python script.py <LogsFileName> <EmailAddress>")
   sys.exit(1)

#open compressed or uncompressed files
if 'gz' in sys.argv[1]:
   file=gzip.open(sys.argv[1],'r')
else:
    file=open(sys.argv[1],'r')

print ""
print "Searching logs for email address: " + bcolors.BLUE ,sys.argv[2] + bcolors.ENDC
print ""

for line in file:
 if "temporarily rejected RCPT" not in line:
      if sys.argv[2] in line:
         if "T=\"" in line:
             print ""
             print  bcolors.MAGENTA + "+++++++++++++++++++++++++++++++++++++++++++++++++" + bcolors.ENDC
             print "Line identify:" + bcolors.BOLD, line + bcolors.ENDC
             title = re.search('(T=\".*\")', line)
             if title:
                print "Subject Email " + bcolors.YELLOW,title.group(1) + bcolors.ENDC
             mail = re.search("(>\Wfor\W.*)", line)
             if mail:
                print "Email recipients " + bcolors.RED, mail.group(1) + bcolors.ENDC
                print ""

file.close()
