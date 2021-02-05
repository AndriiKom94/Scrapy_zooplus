from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.zooplus.de/')
    btn_elem = driver.find_element_by_id('onetrust-reject-all-handler')
    btn_elem.click()
    btn_elem2 = driver.find_element_by_name('Tierarztsuche')
    btn_elem2.click()
'/tierarzt'

if __name__=='__main__':
    main()