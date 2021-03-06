#coding:utf-8
"""
@file:      cs_ucsb
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    17-8-13 下午6:00
@description:
            --
"""
#学者列表入口
base_url = 'http://www.ece.ucsb.edu/directory/faculty/'
#特征训练示例学者入口
sample_url = 'https://engineering.ucsb.edu/people/rod-c-alferness'
#条目链接
item_url_rule = "//tr/td[1]/a/@href"
avatar_rule = "//*[@id='block-system-main']/div/div[2]/div/img/@src"
website_rule = "//a[text()='Personal Website']/@href"
email_rule ="//div[contains(@class,'email')]"
#示例数据
data = {
        "name":"Divyakant Agrawal",
        "title":"Professor",
        #"email":"agrawal@cs.ucsb.edu"
        #"website":"http://www.ndcl.ee.psu.edu/index.asp",
        #"cooperation":"Chang Family Professor of Engineering Innovation ",
        }

#组织名
organization = "University of California, Santa Barbara"

#主修专业
major = " Computer Science"

