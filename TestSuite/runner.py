# 学   员：jiangwei
# 开发时间：2021/7/14 10:50
from page.ticket_test import MyTestCase

leave = '成都'
leave_date = "2021-8-20"
arrive = '武汉'
arrive_date = '2021-8-21'
aa = MyTestCase()
aa.test_buy(leave,leave_date,arrive,arrive_date)

'''操作结果发现，此py文件放在T252同级目录下，cmd命令
D:\PyCharm数据文件\pythonProject>python runner.py才能执行成功
原本放在单独文件夹T252/PO模式练习/run下，执行报错'''