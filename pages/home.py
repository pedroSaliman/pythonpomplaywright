class Select:
    def __init__(self, page):
        self.page = page
        self.selectopt = page.locator('#customerCurrency')
        self.contactlink =   page.locator("//a[normalize-space()='Contact us']")
        self.searchbar=page.locator("#small-searchterms")
        self.apple=page.locator("//span[normalize-space()='Apple MacBook Pro 13-inch']")
        

    def select(self, text):
        self.selectopt.select_option(text)



    def contactlinkclick(self):
        self.contactlink.click()
        

    def search(self,product):
        self.searchbar.fill(product)
        self.apple.click()
        
  