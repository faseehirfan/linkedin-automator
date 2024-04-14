from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import config
import sendInvite

# Example usage
selected_profiles = [
    {'first_name': 'John', 'profile_url': 'https://www.linkedin.com/in/john-doe'},
    {'first_name': 'Jane', 'profile_url': 'https://www.linkedin.com/in/jane-smith'}
]

note_template = "Hi {first_name}, I found your profile and would like to connect with you."

# for profile in selected_profiles:
#     sendInvite(profile, note_template)

profile_url = 'https://www.linkedin.com/'
    
driver = webdriver.Chrome()
driver.get(profile_url)

emailBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_key")))
emailBox.send_keys(config.username)

passwordBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "session_password")))
passwordBox.send_keys(config.password)
passwordBox.send_keys(Keys.ENTER)

searchBar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
searchBar.send_keys("tom sunil")
searchBar.send_keys(Keys.ENTER)

messageButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[1]/div/ul/li/div/a/div/div[2]/div[1]/div/div/button")))
messageButton.click()

chatBox = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "msg-form__contenteditable")))
# chatBox.clear()
chatBox.send_keys("u mallu")
chatBox.send_keys(Keys.CONTROL + Keys.RETURN)


input("Press Enter to close the WebDriver window...")

driver.quit()
# sendInvite.sendInvite(selected_profiles[0], note_template)