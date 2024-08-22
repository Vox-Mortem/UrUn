domain = ('.com', '.ru', '.net')


def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if '@' in sender and '@' in recipient:
        pass
    else:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if sender.endswith(domain) is False or recipient.endswith(domain) is False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
        return
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
        return
    if sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


send_email('Это сообщение для проверки связи', 'vasyok@1337gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
