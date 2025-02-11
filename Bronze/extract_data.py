from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

letters = ['a']

source =  "https://www.webmd.com/vitamins/alpha/"

ul = "/html/body/div[1]/div/main/div/div[2]/div/div/div/div/div/div[2]/aside/ul"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait_time = WebDriverWait(driver,2)



def check_viewMore():
    try:
        loadmore = "/html/body/div[1]/div/main/div/div[2]/div/div/div/div/div/div[3]/span"
        btn_load = driver.find_element(By.XPATH, loadmore)
        if btn_load.is_displayed():
            btn_load.click()
            return True
    except Exception as ex:
        return False
    
    return False

def main():
    for let in letters:        
        url = source + let
        driver.get(url)
    
        while check_viewMore():
            wait_time.until(lambda driver: len(driver.find_elements(By.XPATH, ul)) > 0)
            
        ul_element = driver.find_element(By.XPATH, ul)
        li_element = ul_element.find_element(By.TAG_NAME, 'li')
        
        #for index, li in enumerate(li_element, start=1):
            #a_element = li_element.find_element(By.TAG_NAME,)
            #print(li.text)
         
#driver.quit

if __name__ == "__main__":
    print("test")
    main()    
    