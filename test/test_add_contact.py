# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(u"Алена", u"Николаевна", u"Пашкова", "alena", u"нет", u"АСТА",
                            u"Москва, ул. Мира, д.23-к.89", "902345", "89212346789", "902445", "789078",
                            "f1@moi-uni.ru", "f2@moi-uni.ru", "f3@moi-uni.ru", "https://moi-universitet.ru/", "12",
                            "August", "1989", "12", "August", "2019", u"Москва, ул. Красная, 34-23", "902345",
                            u"примечание"))
