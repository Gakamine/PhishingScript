from src.generateFile import generateFile
from src.sendMail import sendMail

emails= open("emails","r")

if __name__ == '__main__':
	for email in emails:
		filepath=generateFile()
		sendMail(email,filepath)
