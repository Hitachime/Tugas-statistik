#!/usr/bin/env python
from web.user import User
from web.note import Note
import cherrypy
import os.path
root = Note()
root.user = User()
tutconf = os.path.join(os.path.dirname(__file__), 'note.conf')
if __name__ == '__main__':
  cherrypy.quickstart(root, config=tutconf)
else:
  cherrypy.tree.mount(root, config=tutconf)