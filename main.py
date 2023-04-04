# Imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

# Login Screen
def login():
    key = "keep"
    while key == "keep":
        options = int(input("""
        Press 1 for test blank.
        Press 2 for test no password
        Press 3 for locked user
        Press 4 for successful entry
        Press 5 for exit
        """))
        if options == 5:
            exit()
            key = "exit"
        
        elif options == 1:
            testSauce.test_blank()

        elif options == 2:
            testSauce.test_no_password()

        elif options == 3:
            testSauce.test_locked()

        elif options == 4:
            testSauce.test_successful()
        else:
            print("Invalid action please try again.")

# Exit
def exit():
    print("Exiting now...")

# Classes
class test_sauce:

    # No username and no password
    def test_blank(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        passWord = driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("")
        passWord.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        errorBlank = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResultBlank = errorBlank.text == "Epic sadface: Username is required"
        print(f"Test Result: {testResultBlank}")
    
    # no password
    def test_no_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        passWord = driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        passWord.send_keys("")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        errorNoPassword = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResultNoPassword = errorNoPassword.text == "Epic sadface: Password is required"
        print(f"Test Result: {testResultNoPassword}")
        closeButton = driver.find_element(By.CLASS_NAME, "error-button")
        closeButton.click()
        sleep(5)

    # wrong username and wrong password
    def test_invalid_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        passWord = driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("1")
        passWord.send_keys("1")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        errorInvalidLogin = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResultInvalidLogin = errorInvalidLogin.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Result: {testResultInvalidLogin}")

    # locked username
    def test_locked(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        passWord = driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("locked_out_user")
        passWord.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        errorLocked = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResultLocked = errorLocked.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result: {testResultLocked}")

    # Successfull entry
    def test_successful(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        userName = driver.find_element(By.ID, "user-name")
        passWord = driver.find_element(By.ID, "password")
        sleep(2)
        userName.send_keys("standard_user")
        passWord.send_keys("secret_sauce")
        sleep(2)
        loginButton = driver.find_element(By.ID, "login-button")
        loginButton.click()
        sleep(5)
        inventoryFind = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"There are {len(inventoryFind)} products on this website.")

testSauce = test_sauce()
login()