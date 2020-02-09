from selenium import webdriver
import sys
#from selenium.webdriver import Google


"""
    
    Funciton name : store_results
    Return        : -
    Params        : results, query
        results   : a list / tuple of results of the search
        query     : Type - str, required, the query string that is serached
        
"""
def store_results(results, query):
    """
        For storing search results
    """
    file_name = query.replace(" ", "_") + "_text.txt"

    with open(file_name, 'a', encoding='utf-8') as f:
        # results = results[1:11]
        for result in results:
            f.write(" , ".join(result.text.split('\n')))
            f.write("\n")
    
    file_name = query.replace(" ", "_") + "_innerHTML.txt"

    with open(file_name, 'a', encoding='utf-8') as f:
        # results = results[1:11]
        for result in results:
            f.write(str(result.get_attribute("innerHTML")) + "\n")
            f.write("\n")


"""
    
    Funciton name  : search
    Return         : -
    Params         : driver, query, ishomepage
        driver     : Type - webdriver object, required
        query      : Type - str, required, the query string that is serached
        ishomepage : Type - int, default 0, to know if the current page on browser is homepage or not.

"""
def search(driver, query, ishomepage=0):
    """
        For searching on duckduckgo
    """
    if ishomepage:
        # Finding the search field
        search_field = driver.find_element_by_id("search_form_input_homepage")

    else :
        # Finding the search field
        search_field = driver.find_element_by_id("search_form_input")
    
    # Clearing the input field
    search_field.clear()

    # Make search
    search_field.send_keys(str(query))
    search_field.submit()

    # Extract result and display it
    lists = driver.find_elements_by_class_name("result")

    print("Found " + str(len(lists)) + " searches for " + query)
    # for i in lists:
    #     print(i.text.split('\n'))
    
    store_results(lists, query)
    return


"""
    
    This section of the code is called when __main__ needs to be executed
    i.e. default this snipped is executed

"""
# Setting up chrome driver
driver = webdriver.Chrome(executable_path='D:/programs/python/project/bot/chromedriver.exe')

# Window maximized
driver.maximize_window()

# Opening DuckDuckGo home page
driver.get('https://duckduckgo.com')

ishomepage = 1

# Making the search
i = 1
for i in range(1,len(sys.argv)):
    # print(sys.argv[i])
    try :
        search(driver=driver, query=str(sys.argv[i]), ishomepage=ishomepage)
        ishomepage = 0
    except e as Exception:
        pass

# Closing browser window
driver.close()