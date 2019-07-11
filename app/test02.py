from appium import webdriver

import time

# server 启动参数
desired_caps = {}
# 设备信息
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = '192.168.56.101:5555'
# app信息
desired_caps['appPackage'] = 'com.android.settings'
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)

element = driver.find_elements_by_id("com.android.settings:id/title")
print(len(element))
print(type(element))
time.sleep(10)
el = driver.find_element_by_xpath("//*[@text='更多']")
print(el.get_attribute('name'))
print(el.get_attribute('text'))
print(el.get_attribute('resourceId'))
print(el.get_attribute('className'))
print(el.location)
print("当前APP的包名：",driver.current_package)
print("当前页面的启动名：",driver.current_activity)
if driver.is_app_installed(""):
    driver.remove_app("")
    print("卸载成功")
else:
    try:
        driver.install_app("")
        print("下载成功")
    except:
        print("下载时间超过20秒")


driver.quit()