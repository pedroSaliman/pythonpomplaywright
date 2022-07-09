class Contact:
    def __init__(self, page):
        self.page = page
        self.name = page.locator('#FullName')
        self.email =   page.locator("#Email")
        self.comment =   page.locator("#Enquiry")
        self.submit =   page.locator("//button[normalize-space()='Submit']")
        self.result=page.locator(".result")


    def submitcontact(self,thename,theemail,thecomment):
        self.name.fill(thename)
        self.email.fill(theemail)
        self.comment.fill(thecomment)
        self.submit.click()

   
