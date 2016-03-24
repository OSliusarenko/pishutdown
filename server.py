import tornado.ioloop
import tornado.web
import time
import datetime
import subprocess
#from io import StringIO, BytesIO

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("hello.html")


class ActHandler(tornado.web.RequestHandler):
    def get(self, arg=1):
        if arg == 'shutdown_pi':
            msg = 'off'
            self.render("shutdown_msg.html", msg=msg)
            subprocess.call(['sudo', 'poweroff'])
        elif arg == 'reboot_pi':
            msg = 'ready'
            self.render("shutdown_msg.html", msg=msg)
            subprocess.call(['sudo', 'reboot'])
        else:
            self.write("unknown option")




application = tornado.web.Application([
  (r"/", MainHandler),
  (r"/act", ActHandler),
  (r"/act/(.*)", ActHandler),
  ])

if __name__ == "__main__":
  application.listen(8888)
  tornado.ioloop.IOLoop.instance().start()

