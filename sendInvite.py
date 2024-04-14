from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Function to send connection invite with personalized note
def sendInvite(profile, note_template):
    # Extract first name from profile
    first_name = profile['first_name']
    
    # Replace placeholder with first name in the note template
    personalized_note = note_template.replace('{first_name}', first_name)
    
    # Extract LinkedIn profile URL
    # profile_url = profile['profile_url']
    profile_url = 'https://www.linkedin.com/in/tomsunil'
    
    driver = webdriver.Chrome()
    driver.get(profile_url)

    # try:
    #     # Open LinkedIn profile URL
    #     driver.get(profile_url)
        

    #     # Click on the "login" button
    #     connect_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]")))
    #     connect_button.click()
        
    #     # Click on the "Connect" button
    #     connect_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Connect')]")))
    #     connect_button.click()
        
    #     # Click on "Add a note"
    #     add_note_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add a note')]")))
    #     add_note_button.click()
        
    #     # Input personalized note
    #     note_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@name='message']")))
    #     note_input.send_keys(personalized_note)
        
    #     # Click on the "Send now" button
    #     send_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Send now')]")))
    #     send_button.click()
        
    #     print(f"Invite sent to {first_name} with personalized note.")
    
    # except Exception as e:
    #     print(f"Error sending invite to: {str(e)}")
    
    # finally:
    #     # Close the WebDriver
    #     driver.quit()