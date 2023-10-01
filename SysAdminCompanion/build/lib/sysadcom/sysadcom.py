import google.generativeai as palm
import os
import json
import time

palm.configure(api_key='') # Replace with your api key, Go here : https://developers.generativeai.google/tutorials/setup
response = palm.generate_text(
    prompt=input("Your wish is my command(No pun intended): "))
time.sleep(5)
output = response.result
stripped_output = output.strip('`')
os.system(stripped_output)
