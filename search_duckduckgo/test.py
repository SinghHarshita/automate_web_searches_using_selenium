from selenium import webdriver
#from selenium.webdriver import Google

# Setting up chrome driver
driver = webdriver.Chrome(executable_path='D:/programs/python/project/bot/chromedriver.exe')

# Window size
driver.maximize_window()

# Opening web page
driver.get('https://duckduckgo.com')

# Finding the search field
search_field = driver.find_element_by_id("search_form_input_homepage")
search_field.clear()

# Search
search_field.send_keys("Web Automation using python scripts")
search_field.submit()

lists = driver.find_elements_by_class_name("result")

# Printing the results
print("Found " + str(len(lists)) + " searches!")

for i in lists:
    print(i.text.split('\n'))

driver.close()