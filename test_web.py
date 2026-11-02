from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 1. 启动浏览器（路径保持你之前设置的桌面路径）
service = Service(executable_path=r"C:\edge版本\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# 2. 打开必应（Bing）
driver.get("https://cn.bing.com")

try:
    # 3. 等待必应的搜索框出现（必应搜索框的 id 叫 sb_form_q）
    wait = WebDriverWait(driver, 10)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "sb_form_q")))
    
    time.sleep(1)
    
    # 4. 输入文字并按回车
    search_box.send_keys("软件工程大二")
    search_box.send_keys(Keys.ENTER)
    print("✅ 成功输入并搜索")
    
    time.sleep(2) # 等搜索结果加载
    
    # 5. 断言检查
    assert "软件工程大二" in driver.title, "❌ 测试失败：网页标题里没有看到搜索词！"
    print("🎉 测试通过：页面成功跳转，且包含搜索词！")

except Exception as e:
    print(f"❌ 测试出错了: {e}")

finally:
    time.sleep(3)
    driver.quit()
