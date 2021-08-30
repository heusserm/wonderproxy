# Getting started with Selenium - headless Chrome with Wonder Proxy
* Selenium needs Node v?.?.? or higher (see package.json for reference)
* `npm init`
  * set project name, etc, skip if adding test to existing project
  * when it asks the command to run the tests: `mocha`
* `npx gitignore node`
  * this adds a reasonable default .gitignore file
* `npm i -D selenium-webdriver mocha chai proxy-chain`
  * this will download and install the required packages
    * selenium is the automation framework
    * mocha is the test framework and runner
    * chai is an assertion framework
    * proxy-chain for adding proxy authentication
* Download chromedriver and setup path
  * rip the instructions off from the other Selenium Webdriver article
  * but add:
    * https://stackoverflow.com/questions/60362018/macos-catalinav-10-15-3-error-chromedriver-cannot-be-opened-because-the-de
  * and https://sites.google.com/a/chromium.org/chromedriver/downloads
  * and for chrome you have to pick the version that matches the installed version of chrome you have.
  
  
* write tests
  * create directory: `test`
  * create file: `WonderProxyTest.js`
    * see repo for content.
* run tests
  * `npm test`


* more docs:
  * Selenium/WebDriver:
    * https://www.selenium.dev/documentation/

  * CSS Selectors:
    * https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
    * https://www.checklyhq.com/learn/headless/basics-selectors/
    * https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector


* Integrating Wonder Proxy
  * Proxy servers must be added in the WP portal before running the test
  * Setting proxy
    * Add `--proxyserver=http://<server_address>:<port>` to the `args` array when launching Puppeteer
    * See the `runWithProxiedDriver` function for an example of this.
  * Authenticating to proxy
    * is done with the help of ProxyChain
      * https://www.npmjs.com/package/proxy-chain
      * https://blog.apify.com/how-to-make-headless-chrome-and-puppeteer-use-a-proxy-server-with-authentication-249a21a79212/
    * Username and password are taken from the environment, set these in the environment before running the test
      * This is to keep them from being checked in to source control.
      * when setting credentials in IDE configuration make sure that is not being checked into source control.
  * Note that Venice and Amsterdam have cookie acceptance dialogs that obscure the buttons, so while the buttons are there they are not visible to a human user until the dialog is accepted.

  
