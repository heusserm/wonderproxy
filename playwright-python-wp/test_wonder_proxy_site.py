import pytest

def test_home_page_title(page):
    # Simple test, load homepage and check title
    page.goto("https://wonderproxy.com")
    assert page.title() == 'Localization testing with confidence - WonderProxy'

@pytest.mark.parametrize("test_input", ["lansing", "orlando", "perth", "knoxville"])
def test_check_server_status(page, test_input):
    # Check server status for multiple servers
    page.goto("https://wonderproxy.com/servers/status")
    server_status = page.inner_text("//a[@href='/servers/" + test_input + "']/ancestor::li/span[5]")
    assert server_status == "up"
