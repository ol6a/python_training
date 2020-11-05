from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

def test_contact_remove_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups=app.group.get_group_list()
    group=random.choice(groups)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(db.get_contact_in_group(group)) == 0:
        contacts = app.contact.get_contact_list()
        contact = random.choice(contacts)
        app.contact.contact_add_group(contact.id, group.id)
        print("Контакт с id=" + str(contact.id) + " добавлен в группу с id=" + str(group.id))
    else:
        contacts=db.get_contact_in_group(group)
        contact=random.choice(contacts)
    app.contact.contact_del_group(contact, group)

    l = db.get_contact_not_in_group(group)
    try:
        for item in l:
            if item == contact:
                print("Контакт с id="+str(contact.id)+" удален из группы с id="+str(group.id))
                return True
    finally:
        pass


