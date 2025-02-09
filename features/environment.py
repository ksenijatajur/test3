from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_scenario(context, scenario):
    options = Options()

    #
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # headless mode
    #options.add_argument("--disable-gpu")  
    #options.add_argument("--headless=new")  

    # Set up WebDriver
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    
    context.driver.maximize_window()

def after_scenario(context, scenario):
    if hasattr(context, "driver"):  
        context.driver.quit()