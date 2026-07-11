from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_selenium_ui():
    """
    Exactly 1 automated UI test using Python-Selenium.
    Launches a headless Chrome browser, navigates to https://www.example.com,
    and verifies that the page loads correctly by checking the title and h1 tag.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    # Initialize the Chrome webdriver. 
    # Selenium 4+ automatically manages the driver download using Selenium Manager.
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.example.com")
        
        # Verify the page title
        assert "Example Domain" in driver.title
        
        # Verify the main header text
        h1_text = driver.find_element(By.TAG_NAME, "h1").text
        assert h1_text == "Example Domain"
        
        print("UI Test Passed: Example Domain page loaded successfully.")
    finally:
        driver.quit()
