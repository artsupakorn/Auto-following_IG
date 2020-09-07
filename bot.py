import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class Intargram:
    """docstring for Intargram."""
    def __init__(self, username , password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.BaseUrl = "https://www.instagram.com/"

    def Login(self):
        #open Browser
        self.driver.get(f"{self.BaseUrl}accounts/login/")
        # deley time เพื่อให้หน้า load เสร็จก่อน
        time.sleep(2)
        #ค้นหา element แบบ xpath พร้อมกับส่งค่า username ไป
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(self.username)
        #ค้นหา element แบบ xpath พร้อมกับส่งค่า password
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(self.password + Keys.ENTER)
        time.sleep(3)
        #ค้นหา element ที่เป็น button  ที่ชื่อว่า Not Now ทำการ คลิก
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Not Now')]")[0].click()

        #กำหนด url ที่ใช้ในการทำ auto
    def Nav_user(self,user):
        #เมื่อ login เข้ามาแล้ว กำหนดให้วิ่งไปที่ URL ของ user ที่ต้องการห่า
        self.driver.get(f"{self.BaseUrl}{user}")
        time.sleep(2)

        #function ที่ใช้ในการกด follow
    def follow_user(self,user):
        #เรียกใช้ function Nav_user
        self.Nav_user(user)
            #ค้นหา element ที่เป็น button  ที่ชื่อว่า follow ทำการ คลิก
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0].click()
        time.sleep(3)

        #function ที่ใช้ในการกด unfollow
    def unfollow_user(self,user):
        #เรียกใช้ function Nav_user
        self.Nav_user(user)
        #ค้นหา element ที่ เป็น class name
        self.driver.find_elements_by_class_name("_5f5mN.-fzfL._6VtSN.yZn4P")[0].click()
        time.sleep(2)
        #ค้นหา element ที่ เป็น button text unfollow
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Unfollow')]")[0].click()

        #function ค้นหา hashtag
    def Search_Tag(self,hashtag):
        self.driver.get(f"{self.BaseUrl}explore/tags/{hashtag}")
        time.sleep(2)
        #function like photo
    def Like_photo(self,count):
        #ค้นหา element ที่ เป็น class name
        self.driver.find_element_by_class_name('eLAPa').click()
        i = 1
        while i <= count:
            time.sleep(1.5)
            #ค้นหา element ที่ เป็น class name
            self.driver.find_element_by_class_name('wpO6b').click()
            time.sleep(1.5)
            #ค้นหา element ที่ เป็น class name
            self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            time.sleep(1.5)
            i += 1
        if i >= count:
            #ค้นหา element ที่ เป็น class name 
            self.driver.find_element_by_class_name('wpO6b').click()
            time.sleep(1)




MYBOT = Intargram("bubbabluebu" , "Supakorn143")
MYBOT.Login()

hash = open("hashtag.txt", "r")
hashlist = []
for data in hash:
     hashlist.append(data)


for i in hashlist:
     MYBOT.Search_Tag(i)
     MYBOT.Like_photo(5)


# MYBOT.Search_Tag("car")
# MYBOT.Like_photo(10)

# MYBOT.follow_user('leomessi')
# MYBOT.unfollow_user()


#-- loop unfollow and follow ig --#
# txt = open("top.txt" , "r")
# mylist = []
# for data in txt:
#     mylist.append(data)
#
# for i in mylist:
#      MYBOT.follow_user(i)
