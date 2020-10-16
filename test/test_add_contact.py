# -*- coding: utf-8 -*-

from model.contact import Contact
from sys import maxsize

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров", nickname="petr", title=u"-", company=u"АСТА",
                            address=u"Москва, ул. Мира, д.23-к.84", homephone="902345", mobilephone="89212346789", workphone="902445", fax="789078",
                            email="f4@moi-uni.ru", email2="f5@moi-uni.ru", email3="f6@moi-uni.ru", homepage="https://moi-universitet.ru/", bday="16",
                            bmonth="August", byear="1959", aday="12", amonth="August", ayear="2009", address2=u"Москва, ул. Красная, 34-23",
                            phone2="902347", notes=u"test")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)