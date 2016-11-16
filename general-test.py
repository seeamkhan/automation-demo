from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


# def setUp(self):
def start():
    # create a new chrome session
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate to homepage
    base_url = 'https://www.amazon.com/'
    driver.get(base_url)

    # Homepage testing
    regional_modal_id = "redir-overlay"
    opt_out_id = "redir-opt-out"
    stay_current_site_id = "redir-stay-at-www"

    try:
        driver.find_element_by_id(opt_out_id).click()
        driver.find_element_by_id(stay_current_site_id).click()
    except:
        pass

    # Search functionality
    # search_field = "//input[contains (@name, 'field-keywords')]"
    search_field = 'field-keywords'
    driver.find_element_by_name(search_field).clear()
    driver.find_element_by_name('field-keywords').send_keys('earphone')
    driver.find_element_by_name(search_field).submit()
    # search_submit_link_element = "//div[contains (@class, 'nav-search-submit')]//input[contains (@type, 'submit')]"
    # driver.find_element_by_xpath(search_submit_link_element).click()

    # Search result page testing:
    all_product_list = []
    search_result_link = "//li[contains (@id, 'result_1')]//a[contains (@class, 's-access-detail-page')]"
    for i in driver.find_elements_by_xpath(search_result_link):
        # print i.get_attribute("href")
        all_product_list.append(i.get_attribute("href"))
    # print all_product_list
    driver.get(all_product_list[0])

    # Product detail page testing:
    buy_box_id = "buybox_feature_div"
    add_to_cart_button_id = "add-to-cart-button"
    proceed_to_checkout_1 = "//a[contains (text(), 'Proceed to checkout (1 item)')]"
    cart_link_id = "hlb-view-cart-announce"
    product_title_in_cart = "//span[contains (@class, 'a-size-medium sc-product-title')]"

    assert driver.find_element_by_id(buy_box_id)
    driver.find_element_by_id(add_to_cart_button_id).click()
    assert driver.find_element_by_xpath(proceed_to_checkout_1)
    assert driver.find_element_by_id(cart_link_id)
    driver.find_element_by_id(cart_link_id).click()
    prod_title = driver.find_element_by_xpath(product_title_in_cart).text
    # print prod_title


    print "Your product '%s' has been Successfully added in your cart!" % prod_title

    time.sleep(3)


# def tearDown():
#     # Close the browser window
#     webdriver.quit()

start()

# tearDown()
