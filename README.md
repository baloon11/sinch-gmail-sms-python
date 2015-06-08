
This little script - one of the variants to send and recive SMS using Python.

For sending this script uses Python api http://sinch.com/ service

(You must create an account there,
 create an application
 and write the secret and public key into the script)

For recive it uses a smartphone with android application.

SMS comes to this smartphone and android application sends it to gmail.

Then the script reads mail with SMS.

Android application you can find here:
https://play.google.com/store/search?q=sms2email

Usage
-----
	git clone git://github.com/baloon11/sinch-gmail-sms-python.git

Send

    python all.py send international_number_with_plus text of message

Recive

    Read all letters on your gmail
    python all.py recive all

    Read new ( unread )letters on your gmail
    python all.py recive new

Script reads plain text letters that considers sms.

(Letters without constructions such as \< something \>.

 It is a simple checking for html-tags in the letter.

 It is not perfect checking but it can be used in very simple cases.)

Such letters in the mailbox it marked as Normal.

Оther letters it does not read.

Requirements
------------

You need to install 2 packages:

	git clone git://github.com/charlierguo/gmail.git
	(more about this package: https://github.com/charlierguo/gmail)

+

	pip install sinchsms
	(more about this package: https://pypi.python.org/pypi/sinchsms/1.0.3)


---------------------------------------


If my script is not suitable for any reason,
I advise look for services,which used HTTP GET request as API.

(These services exist.)

Then use this Python package for easy work with them:
	http://docs.python-requests.org/en/latest/
