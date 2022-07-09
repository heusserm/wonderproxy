import pytest
#from ..page_factory import
from .cart_page_model import CartPageModel

from ..catalog.catalog_page_model import CatalogPageModel

# test ideas for cart:
# item total count is good
# added items have description, price and quantity
# update sets the item count for the updated item
# update with the same count doesn't do anything
# update stays on the cart page.
@pytest.mark.skip(reason="ignore")
def test_home_page_title(page):
    cart = CartPageModel(page)
    cart.goto()
    assert page.title() == 'Sample system under test'

@pytest.mark.skip(reason="ignore")
def test_check_items(page):
    setup_cart_items(page)

def setup_cart_items(page):
    catalog = CatalogPageModel(page)
    catalog.add_item_by_index(2, 5)
    catalog.add_item_by_index(4, 1)
    pass

