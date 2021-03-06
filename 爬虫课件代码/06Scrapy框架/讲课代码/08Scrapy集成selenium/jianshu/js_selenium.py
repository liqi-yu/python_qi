from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path=r"D:\ProgramApp\chromedriver\chromedriver.exe")

url = "https://www.jianshu.com/p/7e2b63ed0292"
driver.get(url)

WebDriverWait(driver,5).until(
    EC.element_to_be_clickable((By.XPATH,"//section[position()=2]/div/div"))
)

while True:
    try:
        next_btn = driver.find_element_by_xpath("//section[position()=2]/div/div")
        driver.execute_script("arguments[0].click();",next_btn)
    except Exception as e:
        break

subjects = driver.find_elements_by_xpath("//section[position()=2]/div[position()=1]/a")
for subject in subjects:
    print(subject.text)
