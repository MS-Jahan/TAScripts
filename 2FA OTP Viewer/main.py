!#/bin/python

import os, json

dir = "." # This is the directory where all the files containing OTP tokens will be placed.

def do_totp():
	global dir
	files_list = os.listdir(".")
	files_list.remove(os.path.basename(__file__))
	sheet = ""

	for file in files_list:
		sheet += "'" + file + "',"

	sheet = sheet[:-1]
	cmd_output = os.popen("termux-dialog sheet -v " + sheet).read()
	cmd_output = json.loads(cmd_output)

	totp = ""

	if cmd_output['text'] != "":
		with open(dir + "/" + cmd_output['text'] + "", "r") as file:
			totp = file.read()

	import onetimepass as otp
	totp = str(otp.get_totp(totp))
	os.popen("termux-clipboard-set " + totp)
	os.popen("termux-toast " + "Copied to clipboard: " + totp)

cmd_output = os.popen("termux-fingerprint -t 'Authentication Required!' -d 'Enter your Fingerprint'").read()
cmd_output = json.loads(cmd_output)

if cmd_output['auth_result'] == 'AUTH_RESULT_SUCCESS':
	do_totp()
else:
	os.popen("termux-toast Authentication failed!")
