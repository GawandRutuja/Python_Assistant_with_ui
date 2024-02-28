from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Define a class named 'music'
class music():
    # Constructor method (__init__) to initialize the webdriver
    def __init__(self):
        # Provide the path to the ChromeDriver executable, not the Chrome browser executable 
        s=Service("C:\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)

    # Method 'play' to search and play a video on YouTube
    def play(self, query):
        # Store the search query in the instance variable 'query'
        self.query = query

         # Open the YouTube search results page for the given query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        # Find the search input field and send keys
        video = self.driver.find_element("xpath", '//*[@id="video-title"]/yt-formatted-string')
        video.click()

# Create an instance of the 'music' class and play a video
#assist = music()
#assist.play('dynamite by bts')
