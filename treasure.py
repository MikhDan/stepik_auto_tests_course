import unittest
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class MyTreasure(unittest.TestCase):
    def test_treasure(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        try:

            link = "http://suninjuly.github.io/get_attribute.html"
            browser = webdriver.Chrome()
            browser.get(link)
            x_element = browser.find_element(By.ID, "treasure")
            x = people_checked = x_element.get_attribute("valuex")
            y = calc(x)

            
            input1 = browser.find_element(By.ID, "answer")
            input1.send_keys(y)
            option1 = browser.find_element(By.ID, "robotCheckbox")
            option1.click()
            option2 = browser.find_element(By.ID, "robotsRule")
            option2.click()

            


            button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
            button.click()

           
            time.sleep(1)



        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == '__main__':
    unittest.main()
