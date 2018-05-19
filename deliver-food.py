from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



LOGIN_EMAIL = ''
LOGIN_PASSWORD = ''

driver = webdriver.Firefox()

def wait_for(css):
  return WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css)))

# Go to Jollibee Delivery Homepage and Login
driver.get("https://jollibeedelivery.com/")
elem = wait_for("input[placeholder='Email Address']")
time.sleep(2)
elem.send_keys(LOGIN_EMAIL)
time.sleep(2)
driver.find_element_by_css_selector("input[placeholder='Password']").send_keys(LOGIN_PASSWORD)
time.sleep(2)
driver.find_elements_by_css_selector("button[data-event='Login']")[0].click()

time.sleep(10)

driver.find_element_by_css_selector(".check_address_modal").click()
time.sleep(3)

driver.find_element_by_css_selector("button.general-btn.arrow-button.confirm_delivery_address_book_first_step").click()

time.sleep(10)
driver.find_element_by_css_selector("button.general-btn.margin-top-15.no-rta-confirm").click()

# # Order as Guest
# driver.get("https://jollibeedelivery.com/index.php/order/second_step")
# assert "Jollibee Delivery" in driver.title

# Choose Yum Burger category
elem = wait_for(".menu > .category > a[data-event='Yum Burgers']")
time.sleep(5)
elem.click()
time.sleep(3)

############################################################################
# Click Order now button for Yum Burger
elems = driver.find_elements_by_css_selector("#mCSB_4_container > .menu-item > .order-now")
elems[1].click()
time.sleep(3)
elem = elems[1].find_element_by_xpath('..') # Parent Element

elem.find_element_by_css_selector("label[data-event='Solo']").click()

# Add to Cart
elem.find_elements_by_css_selector(".footer.darker > button")[1].click()
time.sleep(3)


############################################################################
# Order Yum Burger Meal
elems[2].click()
time.sleep(3)
elem = elems[2].find_element_by_xpath('..') # Parent Element


# Add to Cart
elem.find_elements_by_css_selector(".footer.darker > button")[1].click()
time.sleep(3)

# Choose Desserts & Drinks category
elem = wait_for(".menu > .category > a[data-event='Desserts & Drinks']")
elem.click()
time.sleep(3)

############################################################################
# Click Order now button for Salted Caramel Choco sundae
elems = driver.find_elements_by_css_selector("#mCSB_11_container > .menu-item > .order-now")
elems[8].click()
time.sleep(3)
elem = elems[8].find_element_by_xpath('..') # Parent Element

order_elem = elem.find_element_by_css_selector(".item-ordering")
time.sleep(3)

# Add 1 orders
plus = order_elem.find_element_by_css_selector(".darker a[data-event='Order plus']")
plus.click()
time.sleep(3)

# Add to Cart
elem.find_elements_by_css_selector(".footer.darker > button")[1].click()
time.sleep(3)


############################################################################
# Click Order now button for Choco sundae
elems[9].click()
time.sleep(3)
elem = elems[9].find_element_by_xpath('..') # Parent Element

order_elem = elem.find_element_by_css_selector(".item-ordering")
time.sleep(3)

# Add 1 orders
plus = order_elem.find_element_by_css_selector(".darker a[data-event='Order plus']")
plus.click()
time.sleep(3)

# Add to Cart
elem.find_elements_by_css_selector(".footer.darker > button")[1].click()
time.sleep(3)


############################################################################
# Click Order now button for Pineapple Juice
elems[10].click()
time.sleep(3)
elem = elems[10].find_element_by_xpath('..') # Parent Element

order_elem = elem.find_element_by_css_selector(".item-ordering")
time.sleep(3)

# Add to Cart
elem.find_elements_by_css_selector(".footer.darker > button")[1].click()
time.sleep(3)

############################################################################
# Process Order
driver.find_elements_by_css_selector("button[data-event='Show order cart']")[0].click()
time.sleep(3)
driver.find_element_by_css_selector(".process-order-new").click()
time.sleep(3)

elem = wait_for("input[name='change_for']")
time.sleep(2)
elem.clear()
time.sleep(2)
elem.send_keys("1000")
time.sleep(2)

driver.find_element_by_css_selector("label[for='agreement1']").click()
time.sleep(2)

driver.find_element_by_css_selector("textarea[name='remarks']").send_keys("Extra ketchup please. Thank you!")

time.sleep(10)

# driver.find_elements_by_css_selector("button.btn-confirm")[1].click()


time.sleep(60)

driver.close()
