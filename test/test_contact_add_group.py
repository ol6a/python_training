from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture


def test_contact_add_group(app):
    orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups=app.group.get_group_list()
    group=random.choice(groups)
    if len(orm.get_contact_not_in_group(group)) == 0 or len(orm.get_contact_list()) == 0:
        app.contact.create(Contact(firstname=u"Петр", middlename=u"Петрович", lastname=u"Петров"))

    contacts = orm.get_contact_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.contact_add_group(contact.id, group.id)
    new_contacts = orm.get_contact_in_group(group)
    print("Контакт с id=" + str(contact.id) + " входит в группу с id=" + str(group.id))
    assert contact in new_contacts
   #l = db.get_contact_in_group(group)
   #try:
   #    for item in l:
   #         if item == contact:
   #             print("Контакт с id=" + str(contact.id) + " входит в группу с id=" + str(group.id))
   #             return True
  # finally:
  #      pass


