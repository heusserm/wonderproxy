import os

class GoogleSearch:
    """Page model for the Google search page"""

    # Contstructor - receive browser and setup proxy, get ready to run actions
    def __init__(self, browser, proxy_server_name):
        self.browser = browser
        self.context = self.browser.new_context(proxy={
            "server": 'http://' + proxy_server_name + ':10000',
            "username": os.environ['PROXY_USER'],
            "password": os.environ['PROXY_PASS']
        })
        self.page = self.context.new_page()

    # visit the page - a more complex page would have methods for clicking buttons and filling in text
    def visit(self):
        self.page.goto("https://google.com")
        # Extract the text from the buttons on the page:
        input_selector = 'input[type="submit"]'
        input_list = self.page.evaluate("""(selector) => {
            // This is evaluated in the browser which allows cool tricks but can be confusing.
            const elements = Array.from(document.querySelectorAll(selector));
            return elements.map(element => element.defaultValue);
        }""", input_selector)

        # Update values match current location:
        self.search_button_text = input_list[0]
        self.lucky_button_text = input_list[1]

