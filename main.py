from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request

# Set up the webdriver
driver = webdriver.Chrome()

# Navigate to the Instagram profile
driver.get("http://www.instagram.com/username")

# Find the image elements
images = driver.find_elements(By.CSS_SELECTOR, "div.KL4Bh img")

# Iterate through the images and download them
for image in images:
    src = image.get_attribute("src")
    urllib.request.urlretrieve(src, "image.jpg")

# Close the webdriver
driver.close()
