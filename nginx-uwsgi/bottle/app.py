#!/usr/bin/python
'''
A basic bottle app skeleton
'''
import bottle
from bottle import default_app, route


@route('/')
@route('/hello')
def hello():
    return 'Hello World! <br/><a href="/hi/guy">click me</a>'

@route('/hi/<id>')
def hi(id):
    return 'Salut  %s' % id;

application = app = default_app()

if __name__ == '__main__':
    bottle.debug(True)
    bottle.run(reloader=True)

