from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time

# Set up WebDriver
driver = webdriver.Chrome()

# Navigate to Amazon
driver.get("https://www.amazon.in/")

# Verify landing page (with adjusted wait)
correct_url = "https://www.amazon.in/"
correct_title = "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"
try:
    WebDriverWait(driver, 10).until(EC.title_is(correct_title))
except:
    time.sleep(5)  # Additional wait if needed
    assert driver.current_url == correct_url, "Incorrect landing page URL"
    assert driver.title == correct_title, "Incorrect landing page title"

# Perform login
login_link = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#nav-link-accountList"))
)
login_link.click()

# Fill in your Amazon email/phone and click Continue
email_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ap_email"))
)
email_input.send_keys("your-email")

continue_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "continue"))
)
continue_button.click()

# Fill in your Amazon password and click Sign In
password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "ap_password"))
)
password_input.send_keys("your-password")

signin_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "signInSubmit"))
)
signin_button.click()


# Print URL and title
print("URL:", driver.current_url)
print("Title:", driver.title)

# Search for "mobile"
search_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
)
search_box.send_keys("mobile")
search_box.submit()

# Filter by 4 stars and price range
rating_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"p_72/1318476031\"]/span/a/section/span"))
)
rating_filter.click()

price_filter = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'₹10,000 - ₹20,000')]"))
)
price_filter.click()

# Click on the first search result
first_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div/div[2]/div/div/div[1]/h2/a/span"))
)
first_result.click()

# Handle potential new window/tab
handles = driver.window_handles
driver.switch_to.window(handles[-1])  # Switch to the latest opened window/tab

# Add the phone to the cart
add_to_cart_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div[1]/div/div/div[2]/div/div[2]/div/form/div/div/div[37]/div[1]/span/span"))
)
add_to_cart_button.click()

driver.switch_to.active_element

# Click on the Go to cart button
go_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div[3]/div[3]/div/div[1]/div[3]/div[1]/div[2]/div[3]/form/span/span/input"))
)
go_to_cart_button.click()

# Keep the browser open for screenshots or further actions
input("Press any key to quit...")

# Close the browser
#driver.quit()
