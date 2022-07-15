
base = 'http://localhost:8080/simple-store.html'

class CatalogPageModel:
    def __init__(self, page):
        self.page = page

    def goto(self):
        if self.page.url.find(base) == -1:
            self.page.goto(base)
        self.page.locator('#catalog-menu-item').click()

    def validate_page(self):
        """Check that the browser is on the catalog page"""
        # TODO: get the fragment and verify it is '#catalog'
        pass

    def add_item_by_index(self, index, quantity):
        self.validate_page()
        # click on item to get detail
        # enter quantity in box
        # click button
        pass

    def click_item(self, description):
        self.validate_page()
        #self.page.locator("a", text=description).click()
        self.page.locator("text=" + description).first.click()

    def get_total_cost(self):
        # scrounge up the total cost
        return 0

# register page model
# todo: figure out what needs to be passed in.
# todo: figure out the factory bits later???
# register_page_model('cart', CartPageModel)
