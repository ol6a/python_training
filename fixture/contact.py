from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_home()
        # init contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit_contact_form
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_selectfield_value("bday", contact.bday)
        self.change_selectfield_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_selectfield_value("aday", contact.aday)
        self.change_selectfield_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_selectfield_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_name).click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)


    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self,index):
        wd = self.app.wd
        self.open_home()
        self.select_contact_by_index(index)
        #submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector("div.msgbox")
        self.contact_cache = None


    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='edit.php?id=" + id + "']").click()

    def modify_contact(self, index, contact):
        wd = self.app.wd
        self.open_home()
        self.open_contact_to_edit_by_index(index)
        # fill contact form
        self.fill_contact_form(contact)
        # submit update
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact(0)


    def count(self):
        wd = self.app.wd
        self.open_home()
        return len(wd.find_elements_by_name("selected[]"))

    def open_home(self):
        wd = self.app.wd
        if not (len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_css_selector("td")
                text_lastname = cells[1].text
                text_name = cells[2].text
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=text_lastname, firstname=text_name, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], phone2= all_phones[3]))
        return list(self.contact_cache)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements__by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def open_contact_to_edit_by_index(self,index):
        wd = self.app.wd
        self.open_home()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact (firstname=firstname, lastname=lastname, id=id, homephone=homephone, mobilephone=mobilephone,
                        workphone=workphone, phone2=phone2)
