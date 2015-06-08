# -*- coding: utf-8 -*-
from sinchsms import SinchSMS
from gmail import Gmail
import sys
import re

pattern = '<[^>]+>'
def this_html(text):
    return True if len(re.findall(pattern,text)) else False

if sys.argv[1]=='send':
    number = sys.argv[2]

    message=''
    for word in sys.argv[3:]:
        message+=" "
        message+=word
    message=message.strip()

    client = SinchSMS("app_public_key","app_secret_key")
    print("Sending '%s' to %s" % (message, number))
    client.send_message(number, message)
#------------------------------------------------------
if sys.argv[1]=='recive':
    g = Gmail()
    g.login('gmail_login', 'gmail_pass')

# mark the letters without html markup as Normal
    messages = g.inbox().mail()
    for message in messages:
        message.fetch()
        message_body=message.body.split()
        message_body=("".join(message_body)).strip()
        if this_html(message_body)==False:
            message.add_label("Normal")

# all letters marked as Normal
    if sys.argv[2]=='all':
        all_messages=g.label("Normal").mail()
        for mes in all_messages:
            mes.fetch()
            mes.read() # mark letter as read
            print mes.fr #from whom
            print mes.body # main text (body) of e-mail
            print "--------------------------------"

# new (unread) letters marked as Normal
    if sys.argv[2]=='new':
        new_messages=g.label("Normal").mail(unread=True)
        for new_mes in new_messages:
            new_mes.fetch()
            new_mes.read() 
            print new_mes.fr
            print new_mes.body
            print "--------------------------------"

    g.logout()

