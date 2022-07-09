base = 'http://localhost:8080/simple-store.html'

class ShippingPageModel:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(base + '#shipping')

    def set_name(self, name):
        self.page.locator("#ship-name").fill(name)

    def set_address1(self, name):
        self.page.locator("#ship-addr1").fill(name)

    def set_address2(self, name):
        self.page.locator("#ship-addr2").fill(name)

    def set_city(self, name):
        self.page.locator("#ship-city").fill(name)

    def set_state(self, name):
        self.page.locator("#ship-state").fill(name)

    def set_zip(self, name):
        self.page.locator("#ship-zip").fill(name)


    def confirm_order(self):
        self.page.locator(".shipping-confirm").click()

# register page model
# todo: figure out what needs to be passed in.
# todo: figure out the factory bits later???
# register_page_model('cart', CartPageModel)
