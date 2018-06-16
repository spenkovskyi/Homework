from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://127.0.0.1/oxwall/admin")

driver.find_element_by_name('identity').send_keys("admin")

driver.find_element_by_name('password').send_keys("pass")

driver.find_element_by_class_name(' ow_positive').click()

driver.get("http://127.0.0.1/oxwall/")

driver.find_element_by_class_name("ow_newsfeed_status_input").send_keys("new status")
driver.find_element_by_class_name("ow_button").click()



# el = driver.find_element_by_class_name("logo_in")
# action = webdriver.ActionChains(driver)
# action.key_down(Keys.CONTROL)
# action.click(el)
# action.key_down(Keys.CONTROL)
# action.perform()
#
#
# print(driver.window_handles)
# # all_windows = driver.window_handles
# print(driver.current_window_handle)
# driver.switch_to.window(driver.window_handle[1])
# driver.close()
# driver.switch_to.window()