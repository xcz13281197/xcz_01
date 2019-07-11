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
#将应用切换到后台5秒
driver.background_app(5)
sleep(5)


#滑动   (318,2319)----->(318,931)
sleep(5)
driver.swipe(318,2319,318,931,duration=5000)
sleep(5)
#滚动   从x_1滚动到 x_2
x_1 = driver.find_element_by_xpath("//*[@text='安全']")
x_2 = driver.find_element_by_xpath("//*[@text='电池']")
driver.scroll(x_1,x_2)
sleep(5)
# 拖拽  从y_1拖拽到y_2
y_1 = driver.find_element_by_xpath("//*[@text='语言和输入法']")
y_2 = driver.find_element_by_xpath("//*[@text='日期和时间']")
driver.drag_and_drop(y_1,y_2)
sleep(5)
y_1 = driver.find_element_by_xpath("//*[@text='语言和输入法']")
print(y_1.location)
x = y_1.location.get('x')
y = y_1.location.get('y')
TouchAction(driver).tap(x=x,y=y).perform()
sleep(5)
y_1 = driver.find_element_by_xpath("//*[@text='语言']")
TouchAction(driver).press(y_1).release().perform()
sleep(5)
driver.close_app()
sleep(5)
driver.start_activity('com.android.settings','.Settings')
sleep(5)
wlan = driver.find_element_by_xpath("//*[@text='WLAN']")
wlan.click()
SSID = driver.find_element_by_xpath("//*[contains(@text,'SSID')]")
TouchAction(driver).long_press(SSID,2000).release().perform()
driver.close_app()
sleep(5)
driver.start_activity('com.android.settings','.Settings')
sleep(5)
wlan = driver.find_element_by_xpath("//*[@text='WLAN']")
wlan.click()
SSID = driver.find_element_by_xpath("//*[contains(@text,'SSID')]")
TouchAction(driver).press(SSID).wait(2000).release().perform()
sleep(5)
driver.close_app()
sleep(5)
driver.start_activity('com.android.settings','.Settings')
sleep(5)
x_1 = driver.find_element_by_xpath("//*[@text='显示']")
x_2 = driver.find_element_by_xpath("//*[@text='电池']")
TouchAction(driver).press(x_2).wait(2000).move_to(x_1).release().perform()
sleep(5)
driver.quit()









