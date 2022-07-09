
#from ..page_factory import register_page_model


# actions for page
# get items
# locate item by description, product id, index
# update item (located item is an input)
# get total cost

base = 'http://localhost:8080/simple-store.html'

class CheckoutPageModel:
    def __init__(self, page):
        self.page = page

    def goto(self):
        self.page.goto(base + '#checkout')

    def get_items(self):
        cart_items = []
        cart_item_locators = self.page.locator(".checkout-item-container")
        for idx in range(0, cart_item_locators.count()):
            item = cart_item_locators.nth(idx)
            cart_items.append({
                "description": item.locator(".checkout-item-description").inner_text(),
                "price": item.locator(".checkout-item-price").inner_text(),
                "quantity": item.locator(".checkout-item-quantity").inner_text(),
                "line-total": item.locator(".checkout-item-line-total").inner_text()
            })
        return cart_items


    def get_total_cost(self):
        return self.page.locator(".checkout-total-cost").inner_text()

    def confirm_order(self):
        self.page.locator(".checkout-confirm").click()

# register page model
# todo: figure out what needs to be passed in.
# todo: figure out the factory bits later???
# register_page_model('cart', CartPageModel)
