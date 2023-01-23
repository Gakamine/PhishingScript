import smtplib
import base64

def sendMail(email,filepath):
	fo = open(filepath, "rb")
	filecontent = fo.read()
	encodedcontent = base64.b64encode(filecontent)  # base64

	sender = 'awfullybademail@gmx.com'
	reciever = email

	marker = "IMPORTANT"

	body="""
	This is a test email to send an attachement.
	"""

	headers="""From: Google Scam <scam@google.com>
	To: To You <amrood.admin@gmail.com>
	Subject: Sending Attachement
	MIME-Version: 1.0
	Content-Type: multipart/mixed; boundary=%s
	--%s
	""" % (marker, marker)

	message_action="""Content-Type: text/plain
	Content-Transfer-Encoding:8bit
	%s
	--%s
	""" % (body,marker)

	attachment = """Content-Type: multipart/mixed; name=\"%s\"
	Content-Transfer-Encoding:base64
	Content-Disposition: attachment; filename=%s

	%s
	--%s--
	""" %(filepath, "Document.txt", encodedcontent, marker)
	message = headers + message_action + attachment

	try:
	   smtpObj = smtplib.SMTP_SSL(SMTPSERVER)
	   smtpObj.login(SENDER,PASSWORD)
	   smtpObj.sendmail(sender, reciever, message)
	   print("Successfully sent email to "+email )
	except Exception as e:
	   print("Error: unable to send email to " +email)
	   print(e)
