from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")

    def tearDown(self):
        self.browser.quit()

        #Brian gets a master caution with an ECAM in flight. He runs through the non-normal flow, which eventually directs him to the landing performance tables.
        #He opens his laptop and clicks on the VappWithFailure shortcut on his home screen.
    def test_can_open_application_home_page_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        #He notices the title and knows he's pulled up the right app
        self.assertIn('A320 Landing Performance Web Application', self.browser.title)

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')








