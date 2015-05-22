import os
import sys
import tempfile
import email.parser
import email.utils
import smtplib

import util
import config


def _verify_email(content):
    """
    Show email contents and ask whethere it should be sent. Returns boolean.
    """
    tmpfile = tempfile.mktemp()
    f = open(tmpfile, "w")
    f.write("PROPOSING TO SEND THE FOLLOWING EMAIL.\n")
    f.write("After quitting 'less', you will be asked whether to send it.\n")
    f.write("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n")
    f.write(content)
    f.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    f.close()
    try:
        os.system("less %s" % tmpfile)
    except KeyboardInterrupt:
        pass
    os.remove(tmpfile)

    while True:
        print "Send email? (Y/N): ",
        ans = sys.stdin.readline().lower()
        if not ans:
            return False
        if ans.startswith("y"):
            return True
        if ans.startswith("n"):
            return False


def _get_address(text):
    "return just the email address in a From/To line"
    return email.utils.parseaddr(text)[1]


def send_email(content,
               smtp_server = config.email_smtp_server, 
               verbose = False):
    s = smtplib.SMTP(smtp_server)

    # get the envelope From and To by parsing the message
    parser = email.parser.Parser()
    parsed_msg = parser.parsestr(content)
    from_addr = _get_address(parsed_msg.get("From"))
    to_addr = _get_address(parsed_msg.get("To"))
    util.call_verbose("Sending email", verbose, 
                      s.sendmail,
                      from_addr, to_addr, content)

def verify_and_send_email(content, **kwargs):
    """
    verify that the email is to be sent, and if so, send it
    """
    if _verify_email(content):
        send_email(content, **kwargs)
    else:
        print "email not sent"
