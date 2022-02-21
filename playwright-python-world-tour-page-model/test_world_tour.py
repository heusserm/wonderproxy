import pytest
from google_search import GoogleSearch

# A list of locations to visit from:
locations = [
  { 'location': 'Lansing', 'server': 'lansing.wonderproxy.com', 'searchButtonText': 'Google Search', 'luckyButtonText': 'I\'m Feeling Lucky' },
  { 'location': 'Amsterdam', 'server': 'amsterdam.wonderproxy.com', 'searchButtonText': 'Google Zoeken', 'luckyButtonText': 'Ik doe een gok' },
  { 'location': 'Venice', 'server': 'venice.wonderproxy.com', 'searchButtonText': 'Cerca con Google', 'luckyButtonText': 'Mi sento fortunato' },
  { 'location': 'Tokyo', 'server': 'tokyo.wonderproxy.com', 'searchButtonText': 'Google 検索', 'luckyButtonText': 'I\'m Feeling Lucky' },
]

# This is the Python way to run a single test with multiple parameters:
@pytest.mark.parametrize("location", locations)
def test_visit_location(browser, location):

    # Arrange: instantiate Page Model
    google_search = GoogleSearch(browser, location['server'])

    # Act: trigger action:
    google_search.visit()

    # Assert values match current location:
    assert google_search.search_button_text == location['searchButtonText']
    assert google_search.lucky_button_text == location['luckyButtonText']
