from_addr = 'from_addr@gmail.com'
to_addr = 'to_addr@gmail.com'
password = 'from_addr_password'
app_password = 'from_addr_app_password'

'''
message wrapper 1 : email.message
set_content(), add_alternative() 二擇一即可
'''
import email.message
msg = email.message.EmailMessage()
msg["From"] = from_addr  # 若 smtplib 連線到 gmail 的主機，則寄件者須為 gmail 帳戶
msg["To"] = to_addr # 收件者
msg["Subject"] = "Demo python send email"  # 郵件標題
msg.set_content('Send email successfully.') # 寄送純文字內容
# msg.add_alternative("<h3>Notice<h3>Send email successfully.", subtype="html") # 寄送 html 內容

'''
message wrapper 2 : email.mime
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
用不同 function 傳遞不同種類的信息
'''
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

content = MIMEMultipart()  # 建立MIMEMultipart物件
content["subject"] = "Demo python send email"  # 郵件標題
content["from"] = from_addr  # 若 smtplib 連線到 gmail 的主機，則寄件者須為 gmail 帳戶
content["to"] = to_addr # 收件者
content.attach(MIMEText("Send email successfully."))  # 郵件文字內容

'''
經過 SSL 加密，建立 smtp server 連線
登入帳密後傳遞訊息
'''
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login(from_addr, password) # README：變更 google 帳戶安全性 - 使用 google 帳密寄送信件
# server.login(from_addr, app_password) # README：變更 google 帳戶安全性 - 使用 google 應用程式密碼寄送信件
server.send_message(msg) # message wrapper 1
# server.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=content.as_string()) # message wrapper 2
server.quit()
