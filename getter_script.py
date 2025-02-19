import os
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

logging.basicConfig(filename='out.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def get_linkedin_profile_image(username, password):
    try:
        print(f"Password: {password}")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")


        options.binary_location = "/usr/bin/google-chrome"

        driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        driver.get("https://www.linkedin.com/login")

        print(f"Password: {password}")
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )

        email_field.send_keys(username)
        password_field.send_keys(password)

        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[3]/div[1]/form/div[4]/button"))
        )
        login_button.click()

        print("Logging in...")

        time.sleep(5)

        try:
            profile_image = WebDriverWait(driver, 30).until(  # Increased timeout
                EC.presence_of_element_located((By.XPATH, "//img[contains(@class, 'profile-card-profile-picture') and contains(@class, 'ember-view')]"))
            )
            image_url = profile_image.get_attribute("src")
            print(f"Image URL: {image_url}")

            response = requests.get(image_url, stream=True)
            if response.status_code == 200:
                with open("linkedin_profile.jpg", "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                logging.info("LinkedIn profile image downloaded successfully.")
            else:
                logging.error(f"Failed to download LinkedIn profile image: {response.status_code}")
        except Exception as e:
            logging.error(f"Error getting LinkedIn profile image: {e}")

        driver.quit()
        return True
    except Exception as e:
        logging.error(f"Error logging in to LinkedIn: {e}")
        return False

if __name__ == '__main__':
    email = os.getenv("LINKEDIN_EMAIL")
    password = os.getenv("LINKEDIN_PASSWORD")

    print(f"Email: {email}")  # Debugging output
    print(f"Password: {password}")

    get_linkedin_profile_image(email, password)