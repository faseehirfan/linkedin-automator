from selenium import webdriver
from selenium.webdriver.common.by import By
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

sendInvite(selected_profiles[0], note_template)