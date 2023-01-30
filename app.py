# coding: utf-8

import sys
from string import Template

import tornado.escape
import tornado.ioloop
import tornado.web

sys.path.append("")
import session

from base import BaseHandler


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            cookie_secret="e446976943b4e8442f099fed1f3fea28462d5832f483a0ed9a3d5d3859f==78d",
            session_secret="3cdcb1f00803b6e78ab50b466a40b9977db396840c28307f428b25e2277f1bcc",
            session_timeout=60,
            store_options={
                # redis host
                'redis_host': 'localhost',
                # redis port
                'redis_port': 6379,
                # redis password
                'redis_pass': '',
            },
        )

        handlers = [
            (r"/", MainHandler),
            (r"/login", LoginHandler),
            (r"/logout", LogoutHandler)
        ]

        tornado.web.Application.__init__(self, handlers, **settings)
        self.session_manager = session.SessionManager(settings["session_secret"],
                                                      settings["store_options"],
                                                      settings["session_timeout"])


class MainHandler(BaseHandler):
    def get(self):
        username = self.get_current_user()
        session_id = self.session_id
        print('session_id: {} username: {}'.format(session_id, username))
        if username and session_id:
            s = Template('session_id ${session_id} username ${username}')
            self.write(s.safe_substitute(session_id=session_id, username=username))
        else:
            self.write('error: username is None or session_id is None')


class LoginHandler(BaseHandler):
    def get(self):
        username = self.get_argument("username")
        self.session["user_name"] = username
        if username:
            self.session.save()
            s = Template('save username ${username} to session')
            self.write(s.safe_substitute(username=username))
        else:
            self.write('error: username is None')


class LogoutHandler(BaseHandler):
    def get(self):
        username = self.get_current_user()
        session_id = self.session_id
        print('session_id: {} username: {}'.format(session_id, username))
        self.session.clear()
        if username and session_id:
            s = Template('clear session. session_id ${session_id} username ${username}')
            self.write(s.safe_substitute(session_id=session_id, username=username))
        else:
            self.write('clear session already')


if __name__ == "__main__":
    app = Application()
    port = 8080
    app.listen(port)
    print('start on port {}'.format(port))
    tornado.ioloop.IOLoop.instance().start()
