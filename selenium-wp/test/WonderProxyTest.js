// noinspection JSUnusedLocalSymbols
const should = require('chai').should();

const {Builder, By} = require('selenium-webdriver');
const {NoSuchElementError} = require('selenium-webdriver/lib/error');
const chrome = require('selenium-webdriver/chrome');

const ProxyChain = require('proxy-chain')

describe('Selenium WebDriver tests', function () {
  this.timeout(20000);  // increase Mocha's default timeout

  describe('WonderProxy website - Puppeteer basics', function () {
    describe('Home Page', function () {
      describe('Title', function () {
        it('should be "Localization testing with confidence - WonderProxy"', async function () {
          await runWithDriver(async function (driver) {
            await driver.get('https://wonderproxy.com');
            const title = await driver.getTitle();
            title.should.equal('Localization testing with confidence - WonderProxy');
          });
        });
      });
    });

    describe('Status Page', function () {
      describe('Title', function () {
        it('should be "Server Status - WonderProxy"', async function () {
          await runWithDriver(async function (driver) {
            await driver.get('https://wonderproxy.com/servers/status');
            const title = await driver.getTitle();
            title.should.equal('Server Status - WonderProxy');
          });
        });
      });

      describe('Server status is up', function () {
        const serverNames = ['lansing', 'nuremberg', 'koto'];
        for (const serverName of serverNames) {
          it(`should show "up" status for ${serverName}`, async function () {
            await runWithDriver(async function (driver) {
              await driver.get('https://wonderproxy.com/servers/status');

              const status = await getServerStatus(driver, serverName);

              // assert status
              status.should.equal('Status: up');
            });
          });
        }
      });
    });
  });

  // Wonder Proxy and Chrome integration:
  describe('Google.com world tour', function () {
    // Note: Servers must be added in the WP portal before running the test
    const locations = [
      { location: 'Lansing', server: 'lansing.wonderproxy.com', searchButtonText: 'Google Search', luckyButtonText: 'I\'m Feeling Lucky' },
      { location: 'Amsterdam', server: 'amsterdam.wonderproxy.com', searchButtonText: 'Google zoeken', luckyButtonText: 'Ik doe een gok' },
      { location: 'Venice', server: 'venice.wonderproxy.com', searchButtonText: 'Cerca con Google', luckyButtonText: 'Mi sento fortunato' },
      { location: 'Tokyo', server: 'tokyo.wonderproxy.com', searchButtonText: 'Google 検索', luckyButtonText: 'I\'m Feeling Lucky' },
    ];

    for (const location of locations) {
      it(`should have location specific text for ${location.location}`, async function () {
        await runWithProxiedDriver(location.server, 10000, async function(driver) {
          await driver.get('http://google.com');

          const inputElements = await driver.findElements(By.css('input[type="submit"]'));
          const inputList = await Promise.all(inputElements.map(i => i.getAttribute('value')));

          // This will get better failure messages indicating expected and actual results
          inputList[0].should.equal(location.searchButtonText);
          inputList[1].should.equal(location.luckyButtonText);

          // This is more robust, will not break if the buttons are re-arranged.
          inputList.should.contain(location.searchButtonText);
          inputList.should.contain(location.luckyButtonText);
        });
      });
    }
  });
});


async function runWithDriver(testFn, options = new chrome.Options()) {
  const screen = {
    width: 640,
    height: 480
  };
  options.headless().windowSize(screen);
  const driver = new Builder()
    .forBrowser('chrome')
    .setChromeOptions(options)
    .build();
  try {
    await testFn(driver);
  } finally {
    await driver.quit();
  }
}

async function runWithProxiedDriver(proxyServer, proxyPort, testFn) {
  const username = process.env.PROXY_USER;
  const password = process.env.PROXY_PASS;

  const wonderProxyUrl = `http://${username}:${password}@${proxyServer}:${proxyPort}`;
  const internalProxyUrl = await ProxyChain.anonymizeProxy(wonderProxyUrl);
  const options = new chrome.Options()
    .addArguments(`--proxy-server=${internalProxyUrl}`);
  await runWithDriver(async function (driver) {
    await testFn(driver);
  }, options);
  await ProxyChain.closeAnonymizedProxy(internalProxyUrl, true);
}

async function getServerStatus(driver, serverName) {
  try {
    await scrollServerIntoView(driver, serverName);
    const serverStatusElement = await driver.findElement(By.xpath(`//a[@href='/servers/${serverName}']/ancestor::li/span[5]`));
    return await serverStatusElement.getText();
  } catch (error) {
    if (error instanceof NoSuchElementError) {
      return `Unable to locate server: '${serverName}' on page`;
    }
    throw error;
  }
}

async function scrollServerIntoView(driver, serverName) {
  const serverStatusLink = await driver.findElement(By.xpath(`//a[@href='/servers/${serverName}']`));
  await driver.executeScript('arguments[0].scrollIntoView(true);', serverStatusLink);
}
