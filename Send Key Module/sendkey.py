import os
def sendkey(text):
	cmd = """osascript -e 'tell application "System Events" to keystroke "%s" using {}'""" % (text)
	os.system(cmd)

sendkey("")