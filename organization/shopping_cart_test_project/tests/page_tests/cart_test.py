import pytest

from ...pages.catalog.catalog_page_model import CatalogPageModel
from ...pages.catalog.catalog_detail_page_model import CatalogDetailPageModel

from ...pages.cart.cart_page_model import CartPageModel

@pytest.mark.page_test
@pytest.mark.cart
def test_items_added_from_catalog_appear_in_cart(page):
    # setup
    setup_cart_items(page)
    cart = CartPageModel(page)
    cart.goto()

    # verify items
    items_in_cart = cart.get_items()
    assert len(items_in_cart) == 2
    assert items_in_cart[0]['description'] == 'blinker fluid'
    assert items_in_cart[0]['price'] == '10'
    assert items_in_cart[0]['quantity'] == '2'
    assert items_in_cart[1]['description'] == 'alternator'
    assert items_in_cart[1]['price'] == '95'
    assert items_in_cart[1]['quantity'] == '1'

@pytest.mark.page_test
@pytest.mark.cart
def test_item_costs_totaled(page):
    # setup
    setup_cart_items(page)
    cart = CartPageModel(page)
    cart.goto()

    # verify total cost
    assert cart.get_total_cost() == '115'

# setup helper
def setup_cart_items(page):
    catalog = CatalogPageModel(page)

    # add an items to the cart
    catalog.goto()
    catalog.click_item("blinker fluid")
    catalog_detail = CatalogDetailPageModel(page)
    catalog_detail.quantity(2)
    catalog_detail.add()

    # add an items to the cart
    catalog.goto()
    catalog.click_item("alternator")
    catalog_detail = CatalogDetailPageModel(page)
    catalog_detail.quantity(1)
    catalog_detail.add()
