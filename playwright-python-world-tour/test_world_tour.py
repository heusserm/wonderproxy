import os
import pytest

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
    # Create a context with the proxy server for current location:
    context = browser.new_context(proxy={
        "server": 'http://' + location['server'] + ':10000',
        "username": os.environ['PROXY_USER'],
        "password": os.environ['PROXY_PASS']
    })

    # Create a page from the context and visit Google home:
    page = context.new_page()
    page.goto("https://google.com")

    # Extract the text from the buttons on the page:
    input_selector = 'input[type="submit"]'
    input_list = page.evaluate("""(selector) => {
        // This is evaluated in the browser which allows cool tricks but can be confusing.
        const elements = Array.from(document.querySelectorAll(selector));
        return elements.map(element => element.defaultValue);
    }""", input_selector)

    # Assert values match current location:
    assert input_list[0] == location['searchButtonText']
    assert input_list[1] == location['luckyButtonText']
