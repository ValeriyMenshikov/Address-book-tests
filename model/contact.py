from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None, workphone=None, new_group=None,
                 faxphone=None, mail=None, email2=None, email3=None, homepage=None, bday=None, bmonth=None, byear=None,
                 aday=None, amonth=None, ayear=None, address2=None, secondaryphone=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.mail = mail
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.new_group = new_group
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return f"firstname={self.firstname}, middlename={self.middlename}, lastname={self.lastname}, " \
               f"nickname={self.nickname}, title={self.title}, company={self.company}, address={self.address}, " \
               f"homephone={self.homephone}, mobilephone={self.mobilephone}, workphone={self.workphone}, " \
               f"faxphone={self.faxphone}, mail={self.mail}, email2={self.email2}, email3={self.email3}, " \
               f"homepage={self.homepage}, bday={self.bday}, bmonth={self.bmonth}, byear={self.byear}, " \
               f"aday={self.bday}, amonth={self.bmonth}, ayear={self.byear}, address2={self.address2}, " \
               f"secondaryphone={self.secondaryphone}, all_phones_from_home_page={self.all_phones_from_home_page}," \
               f"all_emails_from_home_page={self.all_emails_from_home_page}"

    def __eq__(self, other):
        return self.lastname == other.lastname, self.firstname == other.firstname and \
               (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
