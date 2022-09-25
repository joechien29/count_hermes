from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from setting import my_email
from setting import email_pw


def send_email():
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = "New Products for Sale at Hermes"  # 郵件標題
    content["from"] = my_email  # 寄件者
    content["to"] = my_email  # 收件者
    content.attach(MIMEText("New Products for Sale at Hermes"))  # 郵件內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login(my_email, email_pw)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
