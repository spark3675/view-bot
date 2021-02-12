from selenium import webdriver
import time

#time to refresh page
Timer = 10 #10(seconds)

#youtube video link
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

#number of views
views = 10

driver = webdriver.Chrome(executable_path = "/Users/new/Downloads/chromedriver_win32/chromedriver.exe")
driver.get(link)

for i in range(views):
    time.sleep(Timer)
    driver.refresh()