base = 'http://localhost:8080/simple-store.html'

class ShippingConfirmationPageModel:
    def __init__(self, page):
        self.page = page

    def get_message(self):
        return self.page.locator("#done").inner_text()
