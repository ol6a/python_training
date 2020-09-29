from model.contact import Contact

def test_modify_first_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(u"Андрей", u"Андреевич", u"Андреев", "andr", u"нет", u"АСТА",
                            u"Москва, ул. Мира, д.23-к.84", "902345", "89212346789", "902445", "789078",
                            "f4@moi-uni.ru", "f5@moi-uni.ru", "f6@moi-uni.ru", "https://moi-universitet.ru/", "16",
                            "August", "1959", "12", "August", "2009", u"Москва, ул. Красная, 34-23", "902347",
                            u"test"))
    app.session.logout()