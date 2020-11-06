from pony.orm import *
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders
from datetime import datetime

class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column="group_id")
        name = Optional(str, column="group_name")
        header = Optional(str,column="group_header")
        footer = Optional(str, column="group_footer")
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True)

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str)
        address = Optional(str)
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        fax = Optional(str)
        email = Optional(str)
        email2 = Optional(str)
        email3 = Optional(str)
        homepage = Optional(str)
        bday = Optional(int)
        bmonth = Optional(str)
        byear = Optional(str)
        aday= Optional(int)
        amonth = Optional(str)
        ayear = Optional(str)
        address2 = Optional(str)
        phone2 = Optional(str)
        notes = Optional(str)
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)
        deprecated = Optional(str, column='deprecated')

    def __init__(self, host, name, user, password):
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert,groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, middlename=contact.middlename, lastname=contact.lastname, nickname=contact.nickname, company=contact.company,
                           title=contact.title, address=contact.address, homephone=contact.homephone, mobilephone=contact.mobilephone,
                           workphone=contact.workphone, fax=contact.fax, email=contact.email, email2=contact.email2, email3=contact.email3,
                           homepage=contact.homepage, bday=contact.homepage, bmonth=contact.bmonth, byear=contact.byear, aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear,
                           phone2=contact.phone2, notes=contact.notes)
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contact_in_group(self,group):
        orm_group=list(select(g for g in ORMFixture.ORMGroup if g.id==group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contact_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None
                   and orm_group not in c.groups))

