# -*- coding: UTF-8 -*-
# import needed modules/libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from secretpw import pw   #import password from other file
from random import randint

# Create a class, we're creating an Instagram 'bot'
class Bot():

    links = []

    comments = [
        'Great post!', 'Amazing work!', 'Your posts are awesome!', 
        'What a nice post, great job!', 'Well done!', 'Your posts are amazing!', 
        'Keep up the great work!', 'Fantastic work!', 'Great job!'
    ]

    def __init__(self):
        self.login('3853212847')  #login credentials ()
        self.like_comment_by_hashtag('technology') #hashtag we'll search for, looping through posts

    # Creating a login function, assigning webdriver to varibles
    def login(self, username):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com/') #webdriver will find this URL
        sleep(5)
        username_id = self.driver.find_element_by_xpath("//*[@name='username']")
        username_id.send_keys(username)  #calling our Username credentials
        sleep(3)
        password_id = self.driver.find_element_by_xpath("//*[@name='password']")
        password_id.send_keys(pw) #calling Password credentials
        password_id.submit()
        sleep(3)
        # # //TAGNAME[ATTRIBUTE NAME(any in that tag) and then whatever the Attribute Equals]  -- Relative XPATHS
        # Answering NO 'Save username and password?' question:
        Not_now = self.driver.find_element_by_xpath("//button[@class='sqdOP yWX7d    y3zKF     ']")
        Not_now.click()
        sleep(3)
        # Answering NO to turning on Notifications:
        noti = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        noti.click()
        sleep(3)
    # Clicking SEARCH box, entering technology hashtag, following its hyperlink
    def like_comment_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath("//input[@placeholder='Search']")
        search_box.send_keys('#'+hashtag)
        sleep(4)
        self.driver.find_element_by_xpath("//a[@href='/explore/tags/technology/']").send_keys(Keys.ENTER)
        sleep(5)
        # Scrolling to the END of page and back, in order to load enough link elements
        body_elem = self.driver.find_element_by_tag_name('body')
        
        for _ in range(30):
            body_elem.send_keys(Keys.END)
            sleep(3)
            body_elem.send_keys(Keys.HOME)
            sleep(3)
        # Loading more link elements
        self.driver.implicitly_wait(30)
        # Creating a loop through posts, grabbing the 'a' tag (URL's will open each post in a new window)
        links = self.driver.find_elements_by_tag_name('a')
        def condition(link):
            return '.com/p/' in link.get_attribute('href') #getting links attached to the href attribute
        valid_links = list(filter(condition, links))
        # Grab at least 40 links, loop through them
        for i in range(40):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link) #Adding links we haven't found to our list 
        # LIKE
        for link in self.links:
            self.driver.get(link)
            xpath = ("(//button[@class='wpO6b  '])[2]")
            IP_CLICK = self.driver.find_element_by_xpath(xpath)
            IP_CLICK.click()
            sleep(3)
        # COMMENT
            self.driver.find_element_by_xpath("//div[@class='RxpZH']").click()
            sleep(1)
            self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0,8)])
            sleep(2)
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            sleep(2)

        # XPATH to heart LIKE buttons: <button class="wpO6b  " type="button"><div class="QBdPU "><span class="FY9nT"><svg aria-label="Like" 
# xpath = "(//span[text()='Gi2/0/20'])[Matching index number goes here]";
# IP_CLICK = browser.find_element_by_xpath(xpath);
# IP_CLICK.click();
        

def main():
    while True: #Restart app one hour after it finishes
        myBot = Bot()
        sleep(60*60) #one hour

if __name__ == '__main__':
    main()

