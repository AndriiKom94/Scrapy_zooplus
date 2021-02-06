from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv



def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.zooplus.de/')
    driver.implicitly_wait(10)
    if driver.find_element_by_id('onetrust-reject-all-handler'):
        btn_elem = driver.find_element_by_id('onetrust-reject-all-handler')
        btn_elem.click()
    btn_elem2 = driver.find_element_by_xpath('//a[@href="/tierarzt"]')
    btn_elem2.click()
    enter_element = driver.find_element_by_class_name('form-control--search-bar')
    enter_element.send_keys('a')
    element_find = driver.find_element_by_class_name('btn--search-bar-submit')
    element_find.click()
    delete_element = driver.find_element_by_class_name('form-control--search-bar')
    delete_element.send_keys(Keys.CONTROL, 'a')
    delete_element.send_keys(Keys.BACK_SPACE)
    element_find2 = driver.find_element_by_class_name('btn--search-bar-submit')
    element_find2.click()
    element_hunde = driver.find_element_by_xpath('//*[@id="app"]/div/main/div/div[4]/div[1]/section/div[1]/fieldset/div/div[1]/div[1]/label')
    element_hunde.click()
    elements = []
    all_elems = driver.find_elements_by_class_name('result-intro__details')
    for elem in all_elems:
        try:
            elements.append(
                    {
                        'name': elem.find_element_by_class_name('result-intro__header').text,
                        'time': elem.find_element_by_class_name('daily-hours__range').text,
                        'discrpition': elem.find_element_by_class_name('result-intro__address').text,
                        'rate': elem.find_element_by_class_name('result-intro__rating__note').text,
                    }
                )
        except NoSuchElementException:
            pass
    print(elements)




    time.sleep(5)

if __name__=='__main__':
    main()