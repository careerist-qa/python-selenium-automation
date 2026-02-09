# Create your account
driver.find_element(By.XPATH, "//h1[@class='flex--item fs-headline1 fw-bold lh-xs mb8 ws-nowrap']")

# 'Terms of service' paragraph
driver.find_element(By.XPATH, "//div[@class='flex--item js-terms fs-caption fc-black-400 ta-left']")

# Email
driver.find_element(By.ID, "email")

# Password
driver.find_element(By.ID, "password")

# Sign- Up Button
driver.find_element(By.ID, "submit-button")

# Sign-up w/ button
diver.find_element(By.XPATH, "//button[@data-provider='google']")

# Sign -up w/ GitHub
driver.find_element(By.XPATH, "//button[@data-provider='github']")

# Get Stack Overflow for Teams
driver.find_element(By.XPATH, "//a[text()='Get Stack Overflow Internal free for up to 50 users']")
