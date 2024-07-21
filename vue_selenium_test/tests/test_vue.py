
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium_utils import initialize_browser, take_screenshot



# 初始化 WebDriver
driver = initialize_browser(1080, 768)

wait = WebDriverWait(driver=driver, timeout=10, poll_frequency=0.5, ignored_exceptions=None)

# 打开 Vue 应用
driver.get("http://localhost:5173")

# 等待页面加载
time.sleep(2)

# 查找并填写用户名
username_input = driver.find_element(By.XPATH, '//*[@placeholder="Enter your username"]')
username_input.send_keys("testuser")

# 查找并填写密码
password_input = driver.find_element(By.XPATH, '//*[@placeholder="Enter your password"]')
password_input.send_keys("password")

take_screenshot(driver, "login-input.png")

# 查找并点击登录按钮
login_button = driver.find_element(By.XPATH, '//button[span[text()="Login"]]')
login_button.click()

# 等待登录完成,如果跳转到了home画面,可以找到id=home-welcome的元素,说明登录成功
wait.until(EC.presence_of_element_located(((By.ID, 'home-welcome'))))

# Home 页面截图
take_screenshot(driver, "home.png")

# 查找并点击profile menu item
driver.find_element(By.XPATH, '//*[@itemid="profile-menu"]').click()

# 定位到目标h1 title标签
h1_element = driver.find_element(By.ID, 'page-title')

# 断言当前画面是否是Profile画面
assert h1_element.text == 'Profile', f"Expected text 'Profile', but got '{h1_element.text}'"

# profile 页面截图
take_screenshot(driver, "profile-menu.png")

# 查找并点击settings menu item
driver.find_element(By.XPATH, '//*[@itemid="settings-menu"]').click()

# 定位到目标h1 title标签
h1_element = driver.find_element(By.ID, 'page-title')

# 断言当前画面是否是Settings画面
assert h1_element.text == 'Settings', f"Expected text 'Settings', but got '{h1_element.text}'"

# setting 页面截图
take_screenshot(driver, "settings-menu.png")

# 浏览器执行js命令,弹出 测试完成 对话框
driver.execute_script("alert('测试+截图完成,五秒后自动关闭！');")

time.sleep(5)

# 关闭 WebDriver
driver.quit()

