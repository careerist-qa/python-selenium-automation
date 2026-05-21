# Created by willi at 5/13/2026
Feature: Target Loop
  # Enter feature description here

  ##Homework 5

# Wait for color airpod to load
color_airpods = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='colorairpod']"))
)

print(f"Found {len(color_airpods)} colors")

for index in range(len(color_airpods)):
    # Re-locate elements each loop (React re-renders DOM)
    airpods = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "[data-test='colorairpod']"))
    )

    airpod = airpods [index]
    color_name = airpod.get_attribute("aria-label")

    wait.until(EC.element_to_be_clickable(airpod)).click()