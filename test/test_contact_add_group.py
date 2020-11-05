from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_contact_add_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = app.contact.get_contact_list()
    contact = random.choice(contacts)
    groups=app.group.get_group_list()
    group=random.choice(groups)
    app.contact.contact_add_group(contact.id, group.name)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    l = db.get_contact_in_group(group)
    try:
        for item in l:
            if item == contact:
                return True
    finally:
        pass


