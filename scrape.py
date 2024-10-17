# Selenium class/modules - to scrape the data from the website
# Control our web browser using the Selenium WebDriver
import platform
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time


def scrape_website(website):
    print("Launching chrome browser...")

    # Get the system architecture
    system_arch = platform.machine()

    # Define the ChromeDriver path based on the system architecture
    if system_arch == 'x86_64':
        chrome_driver_path = "./chromedriver_linux64"  # For 64-bit Linux
    elif system_arch == 'aarch64':
        chrome_driver_path = "./chromedriver_arm64"  # For ARM 64-bit
    elif system_arch == 'arm64':
        chrome_driver_path = "./chromedriver_mac_arm64"  # For Mac ARM
    elif system_arch == 'x86':
        chrome_driver_path = "./chromedriver_win_32.exe"  # For 32-bit Windows
    elif system_arch == 'amd64':
        chrome_driver_path = "./chromedriver_win_64"  # For 64-bit Windows
    elif system_arch == 'Darwin':
        chrome_driver_path = "./chromedriver_mac_x64"  # For macOS x64
    else:
        raise ValueError("Unsupported architecture: " + system_arch)

    # Passing no options but some include headless mode, ignore images, etc.
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(
        chrome_driver_path), options=options)

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()
        print("Browser closed...")
