from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# setup driver
options = Options()
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# open Google
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# enter search text
search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
search_box.clear()
search_box.send_keys("Car")

# press Enter instead of clicking button (more reliable)
search_box.submit()

# wait for results page
wait.until(EC.presence_of_element_located((By.ID, "search")))

# validation
assert "car" in driver.title.lower(), f"Expected 'car' in title, got {driver.title}"
print("✅ Test Passed")

driver.quit()
