import pytest

from ...pages.catalog.catalog_page_model import CatalogPageModel
from ...pages.catalog.catalog_detail_page_model import CatalogDetailPageModel

from ...pages.cart.cart_page_model import CartPageModel

@pytest.mark.page_test
@pytest.mark.catalog
def test_show_cart_when_item_added_from_catalog(page):
    #setup
    catalog = CatalogPageModel(page)

    # add an items to the cart
    catalog.goto()
    catalog.click_item("blinker fluid")
    catalog_detail = CatalogDetailPageModel(page)
    catalog_detail.quantity(2)
    catalog_detail.add()

    # verify location
    assert "cart" in page.url


