#!/usr/bin/env python
# -*- coding:utf-8 -*-
  
import tornado.ioloop
import tornado.web
import requests
import time

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
		
class TimeHandler(tornado.web.RequestHandler):
    def get(self):
       # url = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
       # response = requests.get(url)
       # self.write(response.text)
       nowTime = time.time() *  1000
       respone = '{"data":{"t":' + str(nowTime) + '}}'
       self.write(respone)
  
application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/time", TimeHandler),
])
  
  
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
