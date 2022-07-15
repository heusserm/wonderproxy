base = 'http://localhost:8080/simple-store.html'

class CartPageModel:
    def __init__(self, page):
        self.page = page

    def goto(self):
        if self.page.url.find(base) == -1:
            self.page.goto(base)
        self.page.locator('#cart-menu-item').click()

    def get_items(self):
        cart_items = []
        cart_item_locators = self.page.locator(".cart-item-container")
        for idx in range(0, cart_item_locators.count()):
            item = cart_item_locators.nth(idx)
            cart_items.append({
                "description": item.locator(".cart-item-description").inner_text(),
                "price": item.locator(".cart-item-price").inner_text(),
                "quantity": item.locator(".cart-item-quantity > input").input_value()
            })
        return cart_items

    def get_total_cost(self):
        return self.page.locator(".cart-total-cost").inner_text()

    def checkout(self):
        self.page.locator('.cart-checkout').click()
