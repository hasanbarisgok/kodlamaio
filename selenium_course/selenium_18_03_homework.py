from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class test_saudemo:
    
    error_area_xpath : str = "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"
    
    def __init__(self):
        
        self.go_page()
        
        self.page_elements()
        
    def page_elements(self):
        
        self.usernameArea = self.driver.find_element(By.ID, "user-name")
        
        self.passwordArea = self.driver.find_element(By.ID, "password")
        
        self.loginButton = self.driver.find_element(By.ID,"login-button")
    
    def go_page(self):
        
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        self.driver.maximize_window()
        
        self.driver.get("https://www.saucedemo.com/")
        
        
    def refresh(self):
        
        self.driver.refresh()
        
        self.page_elements()    
        
    
    def click(self):
        
        self.loginButton.click()    
    
        
    def wrong_id_or_password(self):
                
        self.usernameArea.send_keys("username")
        
        self.passwordArea.send_keys("password")
        
        self.click()
        
        self.error_message = self.driver.find_element(By.XPATH, test_saudemo.error_area_xpath)
        
        print(self.error_message.text)
        
        sleep(2)
        
    
    def fill_id_empty_password(self):
        
        self.refresh()
        
        self.usernameArea.send_keys("username")
        
        self.passwordArea.send_keys("")
        
        self.click()
        
        self.error_message = self.driver.find_element(By.XPATH, test_saudemo.error_area_xpath)
        
        print(self.error_message.text)
        
        sleep(2)
        
    def special_selection(self):
        
        self.refresh()
        
        self.usernameArea.send_keys("locked_out_user")
        
        self.passwordArea.send_keys("secret_sauce")
        
        self.click() 
        
        self.error_message = self.driver.find_element(By.XPATH, test_saudemo.error_area_xpath)
        
        print(self.error_message.text)

        sleep(2)
        
    def true_information(self):
        
        self.refresh()
        
        self.usernameArea.send_keys("standard_user")
        
        self.passwordArea.send_keys("secret_sauce")
        
        self.click()
        
        self.products_num = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        
        print(f"There are products are in total: {len(self.products_num)}")
        
        sleep(100)
        

instance = test_saudemo()
instance.wrong_id_or_password()
instance.fill_id_empty_password()
instance.special_selection()
instance.true_information()       
