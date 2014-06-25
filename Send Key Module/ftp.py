#!/usr/bin/python
import ftplib
import os
filename = "index2.html"
ftp = ftplib.FTP("192.168.1.33")
ftp.login("pi", "acdc2007")
ftp.cwd("/var/www")
os.chdir(r"/Users/hunter/GitRepos/Python Stuff/Send Key Module")
ftp.storlines("STOR " + filename, open(filename, 'r'))