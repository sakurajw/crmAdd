import unittest
from page.Base import base
from page_object.Search import Searchpage
import time
import pyautogui
class MyTestCase(unittest.TestCase):
    def __init__(self):
        self.dk = Searchpage()
    def test_buy(self,leave,leave_data,arrive,arrive_data):
        time.sleep(5)
        #点击火车
        self.dk.search().click()
        time.sleep(1)
        #点击往返
        self.dk.search1().click()
        #输入起点位置
        self.dk.search2().send_keys(leave)
        time.sleep(2)
        #输入出发发时间
        self.dk.search3().send_keys(leave_data)
        time.sleep(2)
        #输入终点站
        self.dk.search4().send_keys(arrive)
        time.sleep(2)
        #输入到达时间
        self.dk.search5().send_keys(arrive_data)
        time.sleep(2)
        #输入返程日期后，搜索按钮被日期框遮挡，此时点击空白处，让日期框消失
        pyautogui.moveTo(359, 551)
        pyautogui.click()
        time.sleep(2)
        #点击搜索
        self.dk.search6().click()
    # def tearDown(self) -> None:
    #     self.dk.quit()

if __name__ == '__main__':
    unittest.main()