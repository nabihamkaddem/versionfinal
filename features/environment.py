import os

import allure
from allure_commons._allure import attach
from allure_commons.types import AttachmentType


from selenium import webdriver
from os import getcwd

from pages.mypage import dragandsidebar


def before_scenario(context,scenario):
    path=os.getcwd()

    option=webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_argument("headless")

    print(path)
   # context.browser = webdriver.Chrome(executable_path=path+'\\driver\\chromedriver.exe')
   ## context.browser = webdriver.Chrome(executable_path=dir+path, chrome_options=option)
    context.browser = webdriver.Chrome(executable_path=path + '\\driver\\chromedriver.exe', chrome_options=option)
    #context.browser.maximize_window()
    context.dd=dragandsidebar(context.browser)
def after_scenario(context,scenario):
    context.browser.close()

def after_step(context, step):
        if step.status == "failed":
           context.browser.save_screenshot('c://b/screenshot.png')
           attach(
               context.browser.get_screenshot_as_png(),
               name="Screenshot",attachment_type=AttachmentType.PNG)