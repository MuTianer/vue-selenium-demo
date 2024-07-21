

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def initialize_browser(width: int, height: int) -> webdriver.Chrome:
    """初始化浏览器并设置固定分辨率"""
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"--window-size={width},{height}")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    return driver

def take_screenshot(driver: webdriver.Chrome, screenshot_name="screenshot.png"):
    """截取整个页面的截图"""
    path = f'images/{screenshot_name}.png'
    driver.save_screenshot(path)
    print(f"截屏已保存到 {path}")