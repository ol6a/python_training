import re

def test_info_home_and_edit_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_info_home_and_db(app, db):
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    for contact1 in contacts_from_home_page:
        for contact2 in contacts_from_db:
            if contact1.id == contact2.id:
                assert contact1.all_phones_from_home_page == merge_phones_like_on_home_page(contact2)
                assert clearp(contact1.address) == clearp(contact2.address)
                assert contact1.lastname == contact2.lastname
                assert contact1.firstname == contact2.firstname
                assert contact1.all_emails_from_home_page == merge_emails_like_on_home_page(contact2)

def clearp(s):
    return re.sub("[ ]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x:clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone,
                                        contact.workphone, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2,
                                        contact.email3]))))

def clear(s):
    return re.sub("[() -]", "", s)

def clear_email(s):
    return re.sub("[ ]", "", s)