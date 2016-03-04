#encode:'utf-8'
'''
Created on 2016��2��13��

@author: Administrator
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
#from email.mime.multipart import MIMEMultipart
#from email.mime.base import MIMEBase
import smtplib

class SendEmail:
    
    def __init__(self,from_addr,password,to_addr,smtp_server):
        self.from_addr=from_addr
        self.password=password
        self.to_addr=to_addr
        self.smtp_server=smtp_server
        
    def _foramt_addr(self,s):
        name,addr=parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))
    
    def setHeader(self,sender_name,receiver_name,subject,content='send by Pang'):
        self.msg = MIMEText(content, 'html', 'utf-8')
        self.msg['From']=self._foramt_addr(sender_name+(' <%s>'%(self.from_addr)))
        self.msg['To']=self._foramt_addr(receiver_name+(' <%s>'%(self.to_addr)))
        self.msg['Subject']=Header(subject,'utf-8').encode()
        
    def setEmailMessage(self,from_addr=None,password=None,to_addr=None,smtp_server=None):
        if from_addr:
            self.from_addr=from_addr
        if password:
            self.password=password
        if to_addr:
            self.to_addr=to_addr
        if smtp_server:
            self.smtp_server=smtp_server
            
    def send(self):
        server=smtplib.SMTP(self.smtp_server,25)
        server.set_debuglevel(1)
        server.login(self.from_addr,self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.quit()
  
if __name__=='__main__':
    sendEmail=SendEmail('pang_6170504@sina.com','9208150016','448680688@qq.com','smtp.sina.com')
    content='hi,this is a test'
    sendEmail.setHeader('pang', 'feng', 'Test',content)
    sendEmail.send()
        
        
        
        