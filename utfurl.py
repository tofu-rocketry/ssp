#!/usr/bin/python
# -*- coding: utf8 -*-

import os, sys
import urlparse, urllib

def fixurl(url):
    # turn string into unicode
        if not isinstance(url,unicode):
            url = url.decode('utf8')
        
        # parse it
        parsed = urlparse.urlsplit(url)
        
        # divide the netloc further
        userpass,at,hostport = parsed.netloc.rpartition('@')
        user,colon1,pass_ = userpass.partition(':')
        host,colon2,port = hostport.partition(':')
        
        # encode each component
        scheme = parsed.scheme.encode('utf8')
        user = urllib.quote(user.encode('utf8'))
        colon1 = colon1.encode('utf8')
        pass_ = urllib.quote(pass_.encode('utf8'))
        at = at.encode('utf8')
        host = host.encode('idna')
        colon2 = colon2.encode('utf8')
        port = port.encode('utf8')
        path = '/'.join( # could be encoded slashes!
            urllib.quote(urllib.unquote(pce).encode('utf8'),'')
            for pce in parsed.path.split('/')
        )
        query = urllib.quote(urllib.unquote(parsed.query).encode('utf8'),'=&?/')
        fragment = urllib.quote(urllib.unquote(parsed.fragment).encode('utf8'))
        
        # put it back together
        netloc = ''.join((user,colon1,pass_,at,host,colon2,port))
        return urlparse.urlunsplit((scheme,netloc,path,query,fragment))

# examples
# print fixurl('http://\xe2\x9e\xa1.ws/\xe2\x99\xa5')
# print fixurl('http://\xe2\x9e\xa1.ws/\xe2\x99\xa5/%2F')
# print fixurl(u'http://Åsa:abc123@➡.ws:81/admin')
# print fixurl(u'http://➡.ws/admin')
# print fixurl(u'http://www.somewebsite.com/моето-име-е-ърл')
# print fixurl(u'http://ecorpbg.com/bg/content/референции')
# print fixurl(u'http://ecorpbg.com/bg/content/партньори')
