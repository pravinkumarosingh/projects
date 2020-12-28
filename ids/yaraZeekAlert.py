#!/usr/bin/python
import subprocess
import os
import time
import sys
import hashlib
import smtplib
import subprocess
import glob
import paramiko
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import Encoders


alertedFilesFolder =  "/root/alertedFiles"
extractedFilePath = "/root/yaraZeekAlert/extract_files"
yaraRulesPath = "/root/YARA/rules"
sevenZipCommand = "/bin/7za"
yaraAlertConfigFile = "/root/yaraZeekAlert/yaraAlert.conf" 

if not os.path.isfile(yaraAlertConfigFile):
	print "file does not exist: " + yaraAlertConfigFile
	sys.exit(1)

with open(yaraAlertConfigFile,"r") as f:
	for line in f:
		lineLst = line.strip("\n").split("=")
		if lineLst[0] in "mailUsername":
			broMailUsername = lineLst[1]
		elif lineLst[0] in "mailPassword":
			broMailPassword = lineLst[1]
		elif lineLst[0] in "mailServer":
			mailServer = lineLst[1]
		elif lineLst[0] in "mailPort":
			mailPort = lineLst[1]
		elif lineLst[0] in "mailDisplayFrom":
			mailDisplayFrom = lineLst[1]
		elif lineLst[0] in "mailTo":
			mailTo = lineLst[1]
def hashes(fname):
	md5 = hashlib.md5(open(fname,'rb').read()).hexdigest()
	sha1 = hashlib.sha1(open(fname,'rb').read()).hexdigest()
	sha256 = hashlib.sha256(open(fname,'rb').read()).hexdigest()
	return [md5,sha1,sha256]

def get_log(extract_string):
	print("[+] Get Log")
	out = subprocess.call(['./get_ip.sh',extract_string])
	f = open("destination_ip.txt", "r")
	destination_ip = f.read()

	hostname = destination_ip
	port = 22
	username = 'root'
	password= 'a'
	print("[+] Destination IP of Malicious/Infected System :-",destination_ip)	
	# Remove the Destination Ip
	print("[+] Removing Infected System From Network (This Might take some time)")
	s = paramiko.SSHClient()
	s.load_system_host_keys()
	print("[+] Trying to connect with the infected machine")
	s.connect(hostname, port, username, password)
	print("[+] Connection Successful")
	print("[!] Trying to shutdown")
	command = 'shutdown now'
	s.exec_command(command)
	print("[+] Successfully Isolated Infected machine from Network")
	s.close()


def searchContext(searchPath, pattern,archived):
		flog = open("/home/bro/YARA/actions.log","w+")
		flog.write("searching for pattern: " + pattern + " in " + searchPath)

		out = ""
		currentLogPath="/home/bro/logs/current"
		
		if not archived:
			files = glob.glob(searchPath + "/*.log")
		else:
			files = glob.glob(searchPath + "/*.log.gz")
		
		for f in files:
        		flog.write("searching in " + f)

			if not archived:
        			command = "/bin/cat " + f + " | /usr/local/bro/bin/bro-cut -d | grep " + pattern + " "
				flog.write("command :" + command)
			else:
				command = "/bin/zgrep " + pattern + " " + f
				flog.write("command :" + command)
				print command

        		try:
                		flog.write("before appending \n" + out)
				out += subprocess.check_output(command, shell=True)
                		flog.write("after appending \n" + out)
        		except:
                		pass
		
		print "context found in path: " + searchPath
		flog.write("context found in path: \n" + searchPath)

		if out =="":
			out = "Context not found in current logs \n"

		print out
		flog.write("output: " + out)
		return out

'''
def sendAlertEmail(message,fromaddr,recipient,filepath,context):
	toaddr = recipient

	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = recipient
	msg['Subject'] = "YARA Alert"

	body = "alerted rules: " + str(message[0]) + "\n"
	body = body + "filepath: " + str(message[1]) + "\n"
	body = body + "md5sum : " + str(message[2]) + "\n"
	body = body + "sha1sum: " + str(message[3]) + "\n"
	body = body + "sha256sum: " + str(message[4]) + "\n\n"

	
	filename = filepath.split("/")[-1]	
	generatedZip = alertedFilesFolder + "/" + filename + ".zip"
	print "generatedZip: " + generatedZip
	
	if os.path.isfile(generatedZip):
		os.remove(generatedZip)

	rc = subprocess.call([sevenZipCommand, 'a', '-pinfected', '-y', generatedZip, filepath])

	body = body + "saved Zip file: " + generatedZip + "\n\n"
	body = body + "context: " + context + "\n"

	filesize = os.path.getsize(generatedZip)
	
	print body
	
	print "filepath: " + filepath + " size: " + str(filesize)
	if os.path.getsize(generatedZip) < 10000000:
		part = MIMEBase('application', "zip")
		part.set_payload(open(generatedZip, "rb").read())
		Encoders.encode_base64(part)
		part.add_header('Content-Disposition', 'attachment; filename="' + filename + ".zip")
 		msg.attach(part)
	else:
		body = body + "File is too big for the attachment"

	msg.attach(MIMEText(body, 'plain'))
	server = smtplib.SMTP(mailServer,mailPort)
   	server.ehlo()
	server.starttls()
	server.ehlo

	# Base64 encoding prevents issues with special characters with passwords/usernames
	broMailPasswordB64 = broMailPassword.encode("base64")
	broMailUsernameB64 = broMailUsername.encode("base64")
	server.login(broMailUsernameB64.decode("base64"),broMailPasswordB64.decode("base64"))
    	text = msg.as_string()
    	server.sendmail(fromaddr, toaddr, text)
    	server.close()
'''

def sendAlertEmail():
	print("ALERT")
	gmail_user = 'okzeekok@gmail.com'
	gmail_password = 'manishsingh'

	sent_from = gmail_user
	to = ['thepoweroframesh@gmail.com', 'bill@gmail.com']
	subject = 'ALERT '
	body = "Malware detected"

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)
	

	try:
	    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	    server.ehlo()
	    server.login(gmail_user, gmail_password)
	    server.sendmail(sent_from, to, email_text)
	    server.close()

	    print 'Email sent!'
	except:
	    print 'Something went wrong...'

	
fout = open("/tmp/yaraAllRules","w")

print extractedFilePath
yaraRules = subprocess.check_output("find " + yaraRulesPath + " -name '*.yar' -exec cat {} + ", shell=True)

fout.write(yaraRules)
fout.close()

start = time.time()
#scanOutput =  subprocess.check_output("yara -r /tmp/yaraAllRules " + extractedFilePath, shell=True)
scanOutput = subprocess.check_output("yara -r /tmp/yaraAllRules " + extractedFilePath + " -d extension=\"noext\" -d filename=\"nofilename\" -d filepath=\"nofilepath\" -d filetype=\"nofiletype\"", shell=True)

end = time.time()

print "Run time: " + str((end - start))
i=0
scanOutput = scanOutput.split("\n")

filesWithAlerts = {}

for line in scanOutput:
	if not "warning" in line and len(line) > 10:
		rule,filepath = line.strip().split(" ")

		# If the file exists, it obtains the file hash
		if filepath in filesWithAlerts.keys():
			filesWithAlerts[filepath].append(rule)		
		else:
			filesWithAlerts[filepath] = [rule]

for filepath, matchedRules in filesWithAlerts.items():
	print "filepath: " + filepath + " v: " +  str(matchedRules)
	# Changed... Regex pattern extract
	extracted_file_path = filepath.split('/root/yaraZeekAlert/extract_files/')[1]

	entry = [str(matchedRules),filepath] + hashes(filepath)
	try:
		print "send alert email"
		pattern = filepath.split("/")[-1].split("-")[-1].split(".")[-2]
		
		context = searchContext("/home/bro/logs/current", pattern,archived=False)

		if context == "":
			print "No additional context was found, searching on the historical log."
		else:
			print context

		#sendAlertEmail(entry,mailDisplayFrom,mailTo,filepath,context)
		sendAlertEmail()
		get_log(extracted_file_path)
	except Exception as e:
		print(e)

files = glob.glob(extractedFilePath + "/*")

for f in files:
	os.remove(f)
