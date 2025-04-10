from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

recipientid="kushalsharmacse@gmail.com"
subject="Your facebook account has been deactivated !!"
message="Dear Facebook User, \n We are sorry to state that your facebook account has been deactivated for some security reasons. \n To again re-activate your account please verify your account thorugh this link : \n XYZ.COM"


path='D:\\PROJECTS\\Email_bot\\chromedriver.exe'
driver= webdriver.Chrome(path)
#driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2Fusers%2Fstory%2Fcurrent%27")


'''
#driver.find_element_by_xpath('').click()


driver.get("https://mail.google.com/mail/u/4/")
sleep(2)
count=2
for i in range(count):
    driver.get("https://mail.google.com/mail/u/8/#inbox?compose=new")
    sleep(2)
    driver.find_element_by_class_name("vO").send_keys(recipientid)
    driver.find_element_by_class_name("aoT").send_keys(subject)
    driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys(message)
    driver.find_element_by_xpath("//div[text()='Send']").click()
    sleep(2)

print("********************************************************************************************************************************************************************")
print(" ")
print("The Spamming Was Sucessful ;) ")
print(" ")

'''