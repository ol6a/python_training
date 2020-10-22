# -*- coding: utf-8 -*-

from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + ("".join([random.choice(symbols) for i in range(random.randrange(maxlen))])).title()

def random_string_nickname(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + "_" + "-" + "." + "@"
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

def random_string_address(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*7 + "-" + "," + string.ascii_uppercase
    return prefix + "".join([random.choice(symbols) for i in range(maxlen)])

def random_string_phone(prefix):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(6)])

def random_string_mobilephone(prefix):
    symbols = string.digits
    return prefix + "".join([random.choice(symbols) for i in range(10)])

def random_string_homepage(maxlen):
    symbols = string.ascii_letters + "-"*4 + "/" + "."
    return "https://" + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_company(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*4 + "-"
    return prefix + ("".join([random.choice(symbols) for i in range(maxlen)])).title()

def random_string_month():
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']
    return random.choice(month)

def random_string_day():
    day = list(range(1,29))
    return str(random.choice(day))

def random_string_year():
    year = list(range(1940,2003))
    return str(random.choice(year))

def random_string_title(prefix):
    title = ['Dear', '-']
    return prefix + "".join(random.choice(title))

def random_string_notes(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ""*15 + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =[
    Contact(firstname=random_string("N", 10), middlename=random_string("M", 15),
            lastname=random_string("L", 20), nickname=random_string_nickname("nick", 10),
            title=random_string_title("title"), company=random_string_company("Company", 14),
            address=random_string_address("addr", 25), homephone=random_string_phone("HP"),
            mobilephone=random_string_mobilephone("MP"), workphone=random_string_phone("WP"),
            email=random_string_email("email", 12), email2=random_string_email("email2", 15),
            email3=random_string_email("email", 20), homepage=random_string_homepage(20),
            address2=random_string_address("addr2", 30), phone2=random_string_phone("P2"),
            notes=random_string_notes("Notes", 40), bday=random_string_day(), bmonth=random_string_month(), byear=random_string_year(),
            aday=random_string_day(), amonth=random_string_month(), ayear=random_string_year()
            )
    for i in range(3)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])

def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)