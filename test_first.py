import pytest
from pages.contactus import Contact

from pages.home import Select
import re
from playwright.sync_api import expect

@pytest.fixture(autouse=True)
def setup(page):
    page.goto("https://demo.nopcommerce.com/")
    yield
    page.close()


# def test_select_currency(page,setup):
#     select=Select(page)
#     select.select("https://demo.nopcommerce.com/changecurrency/6?returnUrl=%2F")



# def test_contact(page,setup):
#     cont=Select(page)
#     cont.contactlinkclick()
#     contact=Contact(page)
#     contact.submitcontact("mohamed","walled@gmail.com","this was good")
#     expect(contact.result).to_contain_text("Your enquiry has been successfully")


def test_search(page):
        select=Select(page)
        select.search("mac")
        select.wishclick()


    




