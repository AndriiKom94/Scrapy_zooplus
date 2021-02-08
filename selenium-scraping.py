from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import csv


# main function
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # enter to the main page of site
    driver.get('https://www.zooplus.de/')
    # checking of cookies request
    driver.implicitly_wait(10)
    if driver.find_element_by_id('onetrust-reject-all-handler'):
        btn_elem = driver.find_element_by_id('onetrust-reject-all-handler')
        btn_elem.click()
    # enter tierarzt page
    btn_tierarzt = driver.find_element_by_xpath('//a[@href="/tierarzt"]')
    btn_tierarzt.click()
    # enter search word
    search_element = driver.find_element_by_class_name('form-control--search-bar')
    search_element.send_keys('a')
    btn_find = driver.find_element_by_class_name('btn--search-bar-submit')
    btn_find.click()
    # delete search word
    delete_element = driver.find_element_by_class_name('form-control--search-bar')
    delete_element.send_keys(Keys.CONTROL, 'a')
    delete_element.send_keys(Keys.BACK_SPACE)
    btn_find2 = driver.find_element_by_class_name('btn--search-bar-submit')
    btn_find2.click()
    # choose 'Hunde' checkbox
    element_hunde = driver.find_element_by_xpath(
        '//*[@id="app"]/div/main/div/div[4]/div[1]/section/div[1]/fieldset/div/div[1]/div[1]/label')
    element_hunde.click()
    elements = []
    page_index = 3  # page index in xpath
    # scraping info page by page
    for i in range(3):
        all_elems = driver.find_elements_by_class_name('result-intro__details')
        for elem in all_elems:
            # exception NoSuchElementException error
            try:
                time_range = elem.find_element_by_class_name('daily-hours__range').text
            except NoSuchElementException:
                try:
                    time_range = elem.find_element_by_class_name('daily-hours__note').text
                except NoSuchElementException:
                    time_range = elem.find_element_by_class_name('daily-hours').text
                    continue
            # add info to list
            elements.append(
                {
                    'name': elem.find_element_by_class_name('result-intro__header').text,
                    'time': time_range,
                    'description': elem.find_element_by_class_name('result-intro__address').text,
                    'rate': elem.find_element_by_class_name('result-intro__rating__note').text,
                }
            )
        # add info to csv file
        with open('cards.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['Name', 'Time', 'Description', 'Rate'])
            for elem1 in elements:
                writer.writerow([elem1['name'], elem1['time'], elem1['description'], elem1['rate']])
        # next page
        next_page = driver.find_element_by_xpath(
            '//*[@id="search-results-pane-tab1"]/div[2]/nav/ul/li[' + str(page_index) + ']/a')
        next_page.click()
        int(page_index)
        page_index += 1


if __name__ == '__main__':
    main()
