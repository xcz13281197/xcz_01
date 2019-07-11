from appium import webdriver

from time import sleep

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

print(driver.device_time)
print(driver.get_window_size())

# 加大音量
for i in range(3):
    print("i:", i)
    driver.keyevent(24)
    sleep(1)

sleep(3)

# 减小音量
for i in range(3):
    print("i:", i)
    driver.keyevent(25)
    sleep(1)
sleep(3)
# 打开通知栏
# driver.open_notifications()
# sleep(2)
# #点击 包含“注意！”的新闻
# driver.find_element_by_xpath("//*[contains(@text,'注意！')]").click()
# driver.close_app()
#获取网络类型
print(driver.network_connection)
#设置网络类型
driver.set_network_connection(4)
#获取设置后的网络类型
print(driver.network_connection)

sleep(3)
driver.quit()
