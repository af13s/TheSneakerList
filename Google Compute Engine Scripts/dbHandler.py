#//https://cloud.google.com/appengine/docs/python/getting-started/storing-data-datastore
#import webapp2

import sys
from google.appengine.ext import ndb

class dbShoeObj(ndb.Model):
   ## Sub model for representing a ShoeObj ##
    name = ndb.StringProperty(indexed=True)
    lprice = ndb.StringProperty(indexed=False)
    URL = ndb.StringProperty(indexed=False)
    imgURL = ndb.StringProperty(indexed=False)

class dbAccount(ndb.Model):
    username = ndb.StringProperty()
    userid = ndb.IntegerProperty()


def post():
    # We set the parent key on each 'Greeting' to ensure each guestbook's
    # greetings are in the same entity group.

    shoeobj = dbShoeObj(name = 'AIR JORDAN 12 RETRO "GYM RED"',
        lprice = '200',
        URL = 'http://www.flightclub.com/air-jordan-12-retro-gym-red-gym-red-white-black-012457?nosto=nosto-startpage-top',
        imgURL = 'http://www.flightclub.com/air-jordan-12-retro-gym-red-gym-red-white-black-012457?nosto=nosto-startpage-top')

    print "Hello World"

    shoeobj.put()


post()




