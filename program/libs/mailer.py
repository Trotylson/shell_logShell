from configparser import ConfigParser
import smtplib

config = ConfigParser()
config.read('./program/config/config.ini')


class Sender():
    
    def __init__(self, reciver, code):
        self._reciver = reciver
        self._code = code
        
        self._smtp = config.get('email', 'smtp_server')
        self._port = config.get('email', 'port')
        
        self._sender = config.get('email', 'address')
        self._pass = config.get('email', 'password')

        self._from = config.get('email', 'from')
        self._subject = 'Account active code.'
        self._body = config.get('email', 'message') + '\nYour account active code: ' + self._code

    def send(self):
        
        email_text = f"""\
        From: {self._from}
        Subject: {self._subject}

        {self._body}
        """

        try:
            smtp_server = smtplib.SMTP_SSL(self._smtp, self._port)
            smtp_server.ehlo()
            smtp_server.login(self._sender, self._pass)
            smtp_server.sendmail(self._from, self._reciver, email_text)
            smtp_server.close()
            print ("Email sent successfully!")
        except Exception as ex:
            print ("Something went wrong….",ex)
        
        