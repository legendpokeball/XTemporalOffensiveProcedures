import os
try:
  from selenium_stealth import stealth
except ImportError:
  os.system("pip install selenium_stealth")
  from selenium_stealth import stealth

try:
  from seleniumbase import SB
except ImportError:
  os.system("pip install seleniumbase")
  from seleniumbase import SB

from seleniumbase import SB
from selenium_stealth import stealth
import random


def apply_stealth_to_tab(driver):
  stealth(
      driver,
      languages=["en-US", "en"],
      vendor="Google Inc.",
      platform="Win32",
      webgl_vendor="Intel Inc.",
      renderer="Intel Iris OpenGL Engine",
      fix_hairline=True,
  )
  # stealth(
  #     sb.driver,
  #     user_agent=
  #     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36',
  #     languages=["en-US", "en"],
  #     vendor="Google Inc.",
  #     platform="Win32",
  #     webgl_vendor="Intel Inc.",
  #     renderer="Intel Iris OpenGL Engine",
  #     fix_hairline=True,
  #     run_on_insecure_origins=True,
  # )
  tz_params = {'timezoneId': 'America/New_York'}
  driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)


def perform(url, method):
  with SB(uc=True, headed=True) as sb:
    apply_stealth_to_tab(sb.driver)
    sb.driver.get("https://bot.sannysoft.com/")
    sb.sleep(random.randint(4, 7))

    apply_stealth_to_tab(sb.driver)
    sb.driver.get(url)
    if method == 'ld':
      sb.driver.uc_click('a')

    sb.sleep(random.randint(2, 4))
    sb.click('button:contains("Download")')
    print('Clicked download button')
    print("waiting 50-60 secs")
    sb.sleep(random.randint(30, 55))
    sb.driver.quit()
    return True


