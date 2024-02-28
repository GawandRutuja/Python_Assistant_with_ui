from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class music():
    def __init__(self):
        # Provide the path to the ChromeDriver executable, not the Chrome browser executable 
        s=Service("C:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
                
    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        # Find the search input field and send keys
        video = self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()

#assist = music()
#assist.play('dynamite by bts')
