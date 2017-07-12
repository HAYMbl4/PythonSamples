import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config = configparser.ConfigParser()
config.read("resources/config.ini")

team_email = config["TEAM"]["email"]
password = config["TEAM"]["password"]
couple_email = config["COUPLE"]["email"]


def notify_about_error(error_msg):
    msg = MIMEMultipart()
    msg["From"] = team_email
    msg["To"] = team_email
    msg["Subject"] = "Error: %s" % config["COUPLE"]["site_url"]
    msg.attach(MIMEText(str(error_msg), "plain"))

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    server.login(team_email, password)
    text = msg.as_string()
    server.sendmail(team_email, team_email, text)
    server.quit()


def notify_about_new_visitors(new_visitors):
    msg = MIMEMultipart()
    msg["From"] = team_email
    msg["To"] = couple_email
    msg["Subject"] = "Wedding Invitation. Ответ от гостей."

    body = responce_template % (
        config["COUPLE"]["her_name"], config["COUPLE"]["his_name"], collect_visitors_to_list(new_visitors),
        config["COUPLE"]["site_url"])
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.yandex.ru', 587)
    server.starttls()
    server.login(team_email, password)
    text = msg.as_string()
    server.sendmail(team_email, couple_email, text)
    server.quit()


def collect_visitors_to_list(new_visitors):
    visitors_list = ""
    for v in new_visitors:
        if v["willGo"]:
            visitors_list += "<li>%s (Пойду)</li>" % v["name"]
        else:
            visitors_list += "<li>%s (Не пойду)</li>" % v["name"]
    return visitors_list


responce_template = """\
<html>
<head></head>
<body>
<h3>Дорогие, %s и %s!</h3>
<p>
	Спешим сообщить, что следующие гости ответили на ваше свадебное приглашение:
</p>
<ul>
    %s	
</ul>
<p>
	Статистику всех ответивших гостей, вы можете посмотреть <a href="%s/statistic.html">по данной ссылке</a>.
</p>
<p>
	С наилучшими пожеланиями Wedding Invitation team!
</p>
</body>
</html>
"""
