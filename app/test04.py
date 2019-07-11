from appium import webdriver
from time import sleep

# server 启动参数
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el_1 = driver.find_element_by_xpath("//*[@text='更多']")
el_2 = driver.find_element_by_xpath("//*[@text='电池']")
driver.drag_and_drop(el_2,el_1)
# TouchAction(driver).press(el_2).wait(2000).move_to(el_1).release().perform()
el_3 = driver.find_element_by_xpath("//*[@text='安全']")
el_3.click()
sleep(5)
el_4 = driver.find_element_by_xpath("//*[@text='屏幕锁定方式']")
el_4.click()
sleep(5)
el_5 = driver.find_element_by_xpath("//*[@text='图案']")
el_5.click()
TouchAction(driver).press(x=239,y=851).wait(100).move_to(x=719,y=851).wait(100).\
    move_to(x=1199,y=851).wait(100).move_to(x=719,y=1331).wait(100).\
    move_to(x=239,y=1811).wait(100).move_to(x=719,y=1811).wait(100).\
    move_to(x=1199,y=1811).release().perform()

sleep(5)
driver.quit()
