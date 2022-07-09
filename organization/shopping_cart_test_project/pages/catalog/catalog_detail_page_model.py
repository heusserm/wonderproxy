
base = 'http://localhost:8080/simple-store.html'

class CatalogDetailPageModel:
    """Page model used to manipulate catalog detail pages"""
    def __init__(self, page):
        self.page = page

    def quantity(self, quantity):
        self.page.locator("input.catalog-quantity").fill(str(quantity))

    def add(self):
        self.page.locator("input.catalog-add").click()

# register page model
# todo: figure out what needs to be passed in.
# todo: figure out the factory bits later???
# register_page_model('cart', CartPageModel)
