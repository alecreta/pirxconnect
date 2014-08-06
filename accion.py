# -*- coding: utf-8 -*-

import configuracion
import twitter
import json
import codecs
import getopt
import sys
import io
import urllib2
import webbrowser
import os
import re


def Save(xhtml, output):
  out = codecs.open(output, mode='a', encoding='ascii',
                    errors='xmlcharrefreplace')
  out.write(xhtml)
  out.close()

def Imagen(urlpost, id):
    opener1 = urllib2.build_opener()
    page1 = opener1.open(urlpost)
    pagina = page1.read()
    busqueda = re.compile('data-resolved-url-large="(.+?):large"')
    resultadobusq = busqueda.findall(pagina)
    if resultadobusq is not None:
        a = 0
        for i in resultadobusq:
            urlencontrada = i
            print urlencontrada
            opener2 = urllib2.build_opener()
            page2 = opener2.open(urlencontrada)
            imagen = page2.read()
            filename = id + str(a) + urlencontrada[-6:]
            fout = open(filename, "wb")
            fout.write(imagen)
            fout.close()
            a += 1


TEMPLATE = """
    <div class="twitter">
      <span class="twitter-user"><a href="http://twitter.com/%s">Twitter</a>: </span>
      <span class="twitter-text">%s</span>
      <span class="twitter-relative-created-at"><a href="http://twitter.com/%s/statuses/%s">Posted %s</a></span>
    </div>
    """


def tweet(message):
    consumer_key = configuracion.ConfigSectionMap("Datos")['consumer_key']
    consumer_secret = configuracion.ConfigSectionMap("Datos")['consumer_secret']
    access_key = configuracion.ConfigSectionMap("Datos")['access_token_key']
    access_secret = configuracion.ConfigSectionMap("Datos")['access_token_secret']

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_key, access_token_secret=access_secret)
    api.PostUpdate(message)

def busqueda(termino, cantidad):
    consumer_key = configuracion.ConfigSectionMap("Datos")['consumer_key']
    consumer_secret = configuracion.ConfigSectionMap("Datos")['consumer_secret']
    access_key = configuracion.ConfigSectionMap("Datos")['access_token_key']
    access_secret = configuracion.ConfigSectionMap("Datos")['access_token_secret']

    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_key, access_token_secret=access_secret)
    resultado = api.GetSearch(termino, count=cantidad)
    #json_size = len(resultado)
    #print json_size
    #print resultado[0]
    for s in resultado:
        urlpost = "http://twitter.com/" + s.user.screen_name + "/statuses/" + str(s.id)
        Imagen(urlpost, str(s.id))

        #xhtml = TEMPLATE % (s.user.screen_name, s.text, s.user.screen_name, s.id, s.relative_created_at)
        #output = "salidaresultado.html"
        #Save(xhtml, output)
