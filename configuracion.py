# -*- coding: utf-8 -*-

import ConfigParser

configuracion = ConfigParser.ConfigParser()
configuracion.read("config")

def ConfigSectionMap(section):
    dict1 = {}
    options = configuracion.options(section)
    for option in options:
        try:
            dict1[option] = configuracion.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def grabar(section, parametro, valor):
    cfgfile = open("config",'w')
    configuracion.set(section, parametro, valor)
    configuracion.write(cfgfile)
    cfgfile.close()
