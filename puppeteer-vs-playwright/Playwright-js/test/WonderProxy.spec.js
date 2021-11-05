const { test, expect } = require('@playwright/test');

test('Puppeteer vs Playwright tests - Login', async ({ page }) => {
  // Navigate to the Wonder Proxy login page
  await page.goto('https://wonderproxy.com/login');

  // Fill in fields and click login button
  await page.fill('#user-username', 'fake-user');
  await page.fill('#user-password', 'wrong-password');
  await page.click('#login-form > button');

  // Get locator
  const errorMessageLocator = await page.innerText('#login-form > p');

  // Assert message content
  expect(errorMessageLocator).toEqual(expect.stringContaining('There was a problem with your username and/or password.'));
});
