#coding:utf-8
"""
@file:      task_manager
@author:    IsolationWyn
@contact:   genius_wz@aliyun.com
@python:    3.5.2
@editor:    PyCharm
@create:    2017/7/1 1:22
@description:
            --
"""
from gevent import monkey

from utils.logger import get_logger

monkey.patch_all()

import sys
import time
import gevent

from gevent.pool import Pool
from gevent.queue import Queue
#from multiprocessing import Queue, Process, Value
from utils.timer import Timer
import random
from ScholarConfig.europepmc_rule import CRWAL_POOL_SIZE
from utils.proxy_manager import ProxyManager
class Taskmanager(object):
    logger = None
    def __init__(self,logging_name):
        Taskmanager.logger = get_logger(logging_name)
        #self.interval = WATCH_INTERVAL
        self.crawl_pool = Pool(size=CRWAL_POOL_SIZE)
        self.page_queue = Queue()
        self.info_queue = Queue()
        self.proxy_manager = ProxyManager("../utils/1.txt",Taskmanager.logger)
        #self.timer = Timer(random.randint(0,2),self.interval)
        self.proxys = self.proxy_manager.get_proxy()
        
        
    def run(self):
        pass
    
    def reload_proxies(self):
        self.proxy_manager.reload_proxies()
        
    def _feed_page_queue(self,base_url):
        pass
    
    def _page_loop(self):
        while 1:
            page_url=self.page_queue.get(block=True)
            gevent.sleep(4)
            self.crawl_pool.spawn(self._feed_info_queue,page_url)
    
    def _feed_info_queue(self,url):
        pass
    
    def _item_loop(self):
        while 1:
            item_url=self.info_queue.get(block=True)
            gevent.sleep(4)
            self.crawl_pool.spawn(self._crawl_info,item_url)
            
    def _crawl_info(self,item_url):
        pass
        
    
        
    
    
    
    
    