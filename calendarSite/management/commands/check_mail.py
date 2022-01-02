#check_mail.py
from django.core.management.base import BaseCommand, CommandError


#import pandas as pd
import datetime #日付や時間を指定するモジュール
import smtplib #メールさメールサーバーを操作してメールを送信する SMTP
import ssl #暗号化や認証の仕組み
from email.mime.text import MIMEText #メールを日本語で送信できるようにするためのモジュール
import sys, codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout)
from email.mime.multipart import MIMEMultipart #メール本文以外に添付ファイルを送信できるようにする
from email.mime.base import MIMEBase #添付ファイルの形式を指定する
from email import encoders #添付ファイルをメールで送ることができるようにする


# gmail_account = "pbl2021team1@gmail.com"
# gmail_password = "fitrakugaku"

# mail_to = "s20a2005@gmail.com"
# send_name = "稲岡天駿"
today_date = datetime.date.today()

#gmailを送る関数
def gmail_send(send_name, mail_to, task, delivery_date ):

  subject = "{0}様、{1}の課題の締め切りが近づいています。".format(send_name,task)
  body = '''課題締め切りのお知らせをします。<br>
            myFITをご確認ください。<br>
            {0}の期限は{1}となります。<br><br>
            プロジェクト型演習team1メンバーより'''.format(task,delivery_date)
  msg=MIMEMultipart()

  msg['Subject'] = subject
  msg['To'] = mail_to
  msg['From'] = gmail_account
  msg_body = MIMEText(body, "html")

  msg.attach(msg_body)

  server = smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context())
  server.login(gmail_account, gmail_password)
  server.send_message(msg)
  server.close()
#   print(send_name,'様：送信完了')


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'Check if you can send an email'

    def handle(self, *args, **options):
        gmail_send("s20a2005", "s20a2005@bene.fit.ac.jp", "課題1:テスト", "2022/1/2" )
        print("hello")