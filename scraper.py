"""
Automated Web Scraper & Data Extractor
This script automates browser interaction, handles dynamic scrolling,
extracts target data using XPath, and exports clean data to a CSV file.
"""
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# 1. Initialize WebDriver and Navigate to Target URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://en.wikipedia.org/")
time.sleep(2)

# 2. Locate Search Box via XPath and Execute Search
search_box = driver.find_element(By.XPATH, "//input[@name='search']")
search_box.send_keys("Artificial intelligence")
search_box.send_keys(Keys.ENTER)
time.sleep(3)

# 3. Handle Lazy Loading by Scrolling the Page
for _ in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# 4. Extract Data using XPath
headings = driver.find_elements(By.XPATH, "//h2")

# 5. Export Extracted Data to a Clean CSV File
with open("extracted_data.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Heading Title"])
    
    for idx, heading in enumerate(headings, start=1):
        clean_text = heading.text.strip()
        if clean_text:
            writer.writerow([idx, clean_text])

driver.quit()
