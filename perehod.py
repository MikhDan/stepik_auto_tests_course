import unittest
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

class MyPerehod(unittest.TestCase):
    def test_perehod(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)
        button = browser.find_element(By.TAG_NAME, "button")
        button.click()
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
        x_element = browser.find_element(By.ID, "input_value")
        x = x_element.text
        y = calc(x)
        input1 = browser.find_element(By.ID, "answer")
        input1.send_keys(y)
        button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
        button.click()
        time.sleep(3)



if __name__ == '__main__':
    unittest.main()
