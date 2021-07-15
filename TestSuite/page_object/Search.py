# 学   员：jiangwei
# 开发时间：2021/7/14 9:55
from page.Base import base
from selenium.webdriver.common.by import By
import time
import pyautogui

# def find(self, *args):
#     try:
#         return self.driver.find_element(*args)
#     except:
#         print("定位失败")
class Searchpage(base):
    #找到“火车”位置
    def search(self):
        return self.find(By.XPATH,"/html/body/div[9]/div/ul/li[6]/b")
     #找到”往返“位置
    def search1(self):
        return self.find(By.ID,"roundTrip")
     #找到”起点“位置
    def search2(self):
        return self.find(By.ID,"notice01")
     #找到出发日期位置
    def search3(self):
        return self.find(By.ID,"DdateObj")
     #找到到达
    def search4(self):
        return self.find(By.ID,"notice02")
     #找到返程日期
    def search5(self):
        return self.find(By.ID,"AdateObj")
     #找到搜索按纽
    def search6(self):
        return self.find(By.ID,"searchTicket")