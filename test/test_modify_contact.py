from model.contact import Contact

def test_modify_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров", nickname="petr", title=u"-", company=u"АСТА",
                            address=u"Москва, ул. Мира, д.23-к.84", homephone="902345", mobilephone="89212346789", workphone="902445", fax="789078",
                            email="f4@moi-uni.ru", email2="f5@moi-uni.ru", email3="f6@moi-uni.ru", homepage="https://moi-universitet.ru/", bday="16",
                            bmonth="August", byear="1959", aday="12", amonth="August", ayear="2009", address2=u"Москва, ул. Красная, 34-23",
                            phone2="902347", notes=u"test"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


#def test_modify_first_contact_company(app):
 #   if app.contact.count() == 0:
 #       app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))
 #   app.contact.modify_first_contact(Contact(company=u"ИНФОРМ"))


#def test_modify_first_contact_birthday(app):
   # if app.contact.count() == 0:
   #     app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))
   # app.contact.modify_first_contact(Contact(bday="22", bmonth="September", byear="1980"))
