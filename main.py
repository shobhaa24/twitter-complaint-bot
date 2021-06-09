from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\Development\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = "sarahmatheww2000@gmail.com"
TWITTER_PASSWORD = "Sarah@123"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go = self.driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        go.click()
        time.sleep(65)
        self.down = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down)
        print(self.up)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        email = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        password = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 150down/10up?")
        time.sleep(3)
        tweet_button = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()








