# PhishingScript
Basic phishing script that will generate a file with a varying hash for each recipient.
This way, you will prevent static analysis from hash calculation.

## How to use it?
- Create a docx file named ``Document.txt`` that contains a malicious Macro. It has to be at the root directory.
- Edit the ``emails`` files and add your victims. It has to be one email address per line.
- Edit the ``src\sendMail.py``:
  - At the line 42 change ``SMTPSERVER`` with the domain or IP of your SMTP Server
  - At the line 43 change ``SENDER`` and ``PASSWORD`` with your email and password to log on your smtp server
  - (OPTIONAL) You can edit the email in the code. I will let you figured out how to. In any case you can create an issue on the repository and would be glad to help you.

# FOR EDUCATION PURPOSE ONLY
