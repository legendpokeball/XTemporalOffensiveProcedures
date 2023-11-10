import json
import subprocess
import fileinput
import time
import random
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime, timedelta

from workaround import update_executable_path
import os

ua = UserAgent().random
chromedriver_path = update_executable_path()

executable_path = chromedriver_path
os.system(f"chmod 700 {executable_path}")


def perform(url, method):

  options = uc.ChromeOptions()
  # options.add_argument(f'--user-agent={ua}')
  options.add_argument("--no-sandbox")
  options.add_argument('--profile-directory=Default')
  options.add_argument('--disable-plugins-discovery')
  options.add_argument('--start-maximized')
  options.add_argument("--disable-dev-shm-usage")
  options.add_argument("--disable-gpu")
  options.add_argument("--disable-extensions")
  options.add_argument("--disable-popup-blocking")
  options.add_argument("--disable-infobars")
  options.add_argument("--disable-notifications")
  # options.add_argument("--headless=False")
  # options.add_argument("--disable-web-security")
  # options.add_argument("--disable-features=VizDisplayCompositor")
  options.add_argument("--disable-features=NetworkService")
  # options.add_argument("--disable-features=VizHitTestSurfaceLayer")
  # options.add_argument("--disable-features=VizHitTestDrawQuad")
  # options.add_argument("--disable-features=VizHitTestDrawQuad")
  options.add_argument("--enable-javascript")
  options.add_argument("--disk-cache-size=0")
  count = 0
  exit_flag = False
  # driver = uc.Chrome(options=options)
  driver = uc.Chrome(options=options, driver_executable_path=executable_path)
  # driver.get(url)
  wait = WebDriverWait(driver, 20)
  # # wait = WebDriverWait(driver, 10)

  # wait_time = random.uniform(5, 15)
  # time.sleep(wait_time)

  try:
    print('1')
    driver.get(url)
    if method == 'ig':
      print('1')
      driver.find_element(
          By.CSS_SELECTOR,
          "body > div > div.page.-cx-PRIVATE-Page__body.-cx-PRIVATE-Page__body__ > div > div > p:nth-child(3) > button"
      ).click()
    elif method == 'ld':
      print('l')
      time.sleep(3)
      driver.find_element(By.CSS_SELECTOR, ".main > a").click()

    else:
      print("no method speccified method")
    time.sleep(random.uniform(5, 8))
    original_window = driver.current_window_handle

    # download_button = driver.find_element(By.ID, 'downloadbtn')
    print('1')
    element_locator = (By.ID, 'downloadbtn')
    while True:
      try:
        print('enter function')

        # Click anywhere on the page (body)
        driver.find_element(By.TAG_NAME, 'body').click()
        time.sleep(4)

        # Check if it redirects
        if len(driver.window_handles) > 1:
          driver.switch_to.window(driver.window_handles[-1])
          driver.close()
          driver.switch_to.window(original_window)
          print('Redirected, closing new window')
          continue

        # Try clicking the download button
        # element = driver.find_element(*element_locator)
        print('try')
        element = wait.until(EC.element_to_be_clickable(element_locator))
        element.click()

        print('Clicked download button')
        print("waiting 50-60 secs")
        time.sleep(random.randint(60, 80))
        driver.quit()
        return True

      except:
        print('Retry')

  except:
    print(Exception)
    return False
  finally:

    driver.quit()
