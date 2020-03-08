from pony.orm import *
from model.group import Group
from model.contact import Contact
from pymysql.converters import decoders


class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse='groups', lazy=True)
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse='contacts', lazy=True)
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        deprecated = Optional(str, column='deprecated')
        middlename = Optional(str, column='middlename')
        nickname = Optional(str, column='nickname')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        company = Optional(str, column='company')
        homephone = Optional(str, column='home')
        mobilephone = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        faxphone = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        bday = Optional(str, column='bday')
        bmonth = Optional(str, column='bmonth')
        byear = Optional(str, column='byear')
        aday = Optional(str, column='aday')
        amonth = Optional(str, column='amonth')
        ayear = Optional(str, column='ayear')
        address2 = Optional(str, column='address2')
        secondaryphone = Optional(str, column='phone2')

    def __init__(self, host, name, user, password):
        # self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=decoders) с декодером не работает
        self.db.bind('mysql', host=host, database=name, user=user, password=password)
        self.db.generate_mapping()
        sql_debug(True)

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, middlename=contact.middlename,
                                                lastname=contact.lastname, nickname=contact.nickname,
                                                title=contact.title, company=contact.company,
                                                address=contact.address, homephone=contact.homephone,
                                                mobilephone=contact.mobilephone, workphone=contact.workphone,
                                                faxphone=contact.faxphone, mail=contact.email,
                                                email2=contact.email2, email3=contact.email3,
                                                homepage=contact.homepage,
                                                bday=contact.bday, bmonth=contact.bmonth, byear=contact.byear,
                                                aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear,
                                                address2=contact.address2, secondaryphone=contact.secondaryphone,
                                                all_phones_from_home_page=contact.all_phones_from_home_page,
                                                all_emails_from_home_page=contact.all_emails_from_home_page
                           )
        return list(map(convert, contacts))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))

    @db_session
    def get_contact_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(orm_group.contacts)

    @db_session
    def get_contact_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(select(
            c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))
