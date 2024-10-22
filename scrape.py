# Selenium class/modules - to scrape the data from the website
# Control our web browser using the Selenium WebDriver
from config import AUTH
from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
# Bright Data proxy manager - Web Data Platform
SBR_WEBDRIVER = f'https://{AUTH}@zproxy.lum-superproxy.io:9515'


def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        # Captcha handling: If you're expecting a CAPTCHA on the target page, use the following code snippet
        print("Waiting for CAPTCHA to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            }
        )
        print('Captcha solve status:', solve_res['value']['status'])
        print('Navigated! Scraping page content...')
        html = driver.page_source
        return html
