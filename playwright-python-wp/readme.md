# Getting started with Playwright and Python

* install the module: `pip install playwright`
  * may need `pip3 install playwright` depending on your environment
  * this is around 30 mb on my system
* install browsers: 'playwright install'
  * from the cli help: "ensure browsers necessary for this version of Playwright are installed"
  * this is around 120mb on my machine for chromium
  * then 70 mb for firefox
  * then 50 mb for webkit
* install pytest-playwright module: `pip3 install pytest-playwright`

* run a script: `python sanity.py`
* run pytest: `pytest`
* headed test with pytest: `pytest --headed`
  * see runners resource for more examples, different browser, multibrowser etc.

* Make a note about python version
  * Python 3.7 or newer is required

* References:
  * https://playwright.dev/python/docs/intro
  * https://playwright.dev/python/docs/intro#system-requirements
  * https://playwright.dev/python/docs/test-runners
