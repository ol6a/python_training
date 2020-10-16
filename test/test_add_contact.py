# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(u"Светлана", u"Николаевна", u"Медвееава", "alena", u"нет", u"АСТА",
                            u"Москва, ул. Мира, д.23-к.89", "902345", "89212346789", "902445", "789078",
                            "f1@moi-uni.ru", "f2@moi-uni.ru", "f3@moi-uni.ru", "https://moi-universitet.ru/", "12",
                            "August", "1989", "12", "August", "2019", u"Москва, ул. Красная, 34-23", "902345",
                            u"примечание")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)