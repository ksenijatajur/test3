from selenium import webdriver

def before_scenario(context, scenario):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    #options.add_argument('--window-size=1920,1080')
    
    #context.driver = webdriver.Chrome(options=options)
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    

def after_scenario(context, scenario):
    try:
        if context.driver:
            context.driver.quit()
            print("WebDriver quit successfully")
    except Exception as e:
        print(f"Error quitting WebDriver: {e}")
    