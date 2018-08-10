from selenium import webdriver

browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

#Brian gets a master caution with an ECAM in flight. He runs through the non-normal flow, which eventually directs him to the landing performance tables.
#He opens his laptop and clicks on the VappWithFailure shortcut on his home screen.
browser.get('http://localhost:8000')




browser.quit()
