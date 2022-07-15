import pytest

from ...pages.cart.cart_page_model import CartPageModel
from ...pages.catalog.catalog_page_model import CatalogPageModel
from ...pages.catalog.catalog_detail_page_model import CatalogDetailPageModel
from ...pages.checkout.checkout_page_model import CheckoutPageModel
from ...pages.shipping.shipping_page_model import ShippingPageModel
from ...pages.shipping.shipping_confirmation_page_model import ShippingConfirmationPageModel

@pytest.mark.path2purchase
def test_add_item_to_cart(page):
    # load catalog
    catalog = CatalogPageModel(page)
    catalog.goto()

    # add an item to the cart
    catalog.click_item("blinker fluid")
    catalog_detail = CatalogDetailPageModel(page)
    catalog_detail.quantity(2)
    catalog_detail.add()

    # validate cart items and click checkout button
    cart = CartPageModel(page)
    assert_cart_items(cart)
    cart.checkout()

    # validate items in checkout and click confirm
    checkout = CheckoutPageModel(page)
    assert_checkout_items(checkout)
    checkout.confirm_order()

    # fill in shipping information and click confirm
    shipping = ShippingPageModel(page)
    fill_in_address_information(shipping)
    shipping.confirm_order()

    ship_confirmation = ShippingConfirmationPageModel(page)
    assert "Thank you for your order" in ship_confirmation.get_message()

#helper functions:
def assert_cart_items(cart):
    items_in_cart = cart.get_items()
    assert len(items_in_cart) == 1
    assert items_in_cart[0]['description'] == 'blinker fluid'
    assert items_in_cart[0]['price'] == '10'
    assert items_in_cart[0]['quantity'] == '2'

    # verify total cost
    assert cart.get_total_cost() == '20'


def assert_checkout_items(checkout):
    items_in_checkout = checkout.get_items()
    assert len(items_in_checkout) == 1
    assert items_in_checkout[0]['description'] == 'blinker fluid'
    assert items_in_checkout[0]['price'] == '10'
    assert items_in_checkout[0]['quantity'] == '2'
    assert items_in_checkout[0]['line-total'] == '20'

    # verify total cost
    assert checkout.get_total_cost() == '20'

def fill_in_address_information(shipping):
    shipping.set_name("Test User")
    shipping.set_address1("Address1")
    shipping.set_address2("Address2")
    shipping.set_city("City")
    shipping.set_state("State")
    shipping.set_zip("ZIP")
