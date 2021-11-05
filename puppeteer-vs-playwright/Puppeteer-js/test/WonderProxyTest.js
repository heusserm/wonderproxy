// noinspection JSUnusedLocalSymbols
const should = require('chai').should();
const puppeteer = require('puppeteer');

describe('Puppeteer vs Playwright tests - Login', function () {
  this.timeout(20000);  // increase Mocha's default timeout

  it('should be present and error message when given bad credentials', async function () {

    // Launch browser
    const browser = await puppeteer.launch({headless: false});
    // Use this instead of previous line to turn off headless and slow things down:
    // const browser = await puppeteer.launch({ headless: false, slowMo: 250 });

    // Find the first tab
    const pages = await browser.pages();
    const page = pages[0];

    // Navigate to the Wonder Proxy login page
    await page.goto('https://wonderproxy.com/login');

    // Fill in fields and click login button
    await page.type('#user-username', 'fake-user');
    await page.type('#user-password', 'wrong-password');
    await page.click('#login-form > button');

    // Wait for message
    await page.waitForSelector('#login-form > p');

    // Capture message content
    const errorMessageHandle = await page.$('#login-form > p');
    const errorMessageContent = await errorMessageHandle.evaluate(node => node.innerHTML);

    await browser.close();

    // Assert message content
    errorMessageContent.should.contain('There was a problem with your username and/or password.');
  });
});
