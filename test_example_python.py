# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver

success = True
wd = WebDriver(r"myDir\chromedriver.exe")
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("http://localhost:5002/")
    wd.find_element_by_xpath("//div[@class='container']//button[.='Send bug']").click()
    wd.find_element_by_name("team_id").click()
    wd.find_element_by_name("team_id").clear()
    wd.find_element_by_name("team_id").send_keys("123")
    wd.find_element_by_name("bug_content").click()
    wd.find_element_by_name("bug_content").clear()
    wd.find_element_by_name("bug_content").send_keys("test1")
    wd.find_element_by_id("send-button").click()
    if not ("Team with id: '123' was not found." in wd.find_element_by_tag_name("html").text):
        success = False
        print("verifyTextPresent failed")
    wd.find_element_by_xpath("//div[@class='container']//button[.='Go back']").click()
    wd.find_element_by_xpath("//div[@class='container']//button[.='Go back']").click()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
