"""
Задание 4
Жду от вас письмо! (слайды 13-17). Воспользуйтесь менеджером контекста (with … as) (слайд 17)
(Не забудьте для себя понять код из официальной документации – слайд 18).

"""
import smtplib

if __name__ == "__main__":
    # help(smtplib)
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp_object:
        smtp_object.starttls()
        smtp_object.login('s.penkovskyi@gmail.com', '***')
        smtp_object.sendmail(from_addr="s.penkovskyi@gmail.com",to_addrs="svpenya@ukr.net", msg="Subject:It works!\n\n It defenetely works!")
