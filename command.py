import smtplib
import subprocess


server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( 'hunter.pi.motion@gmail.com', 'acdc2007' )


cmd = ["uptime"]
output = subprocess.Popen( cmd, stdout=subprocess.PIPE ).communicate()[0]
x = "I've been up for " + output[10:17] + "!"

server.sendmail( 'hunter.pi.motion@gmail.com', 'tweet@tweetymail.com', "testing 2" )