# -*- coding: utf-8 -*-

import obtenertoken
import configuracion
import accion
import argparse

if configuracion.ConfigSectionMap("Estado")['configurado'] != "1":
    obtenertoken.main()

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tweet", help="Publica Tweet, main.py -t mensaje.")
parser.add_argument("-b", "--buscar", help="Busca cadena, main.py -b palabraclave. Si va a buscar un hashtag, por favor use comillas.")
parser.add_argument("-c", "--cantidad", type=int, help="Cantidad de resultados (Por omision:30), main.py -c cantidad.")
parser.add_argument("-a", "--amigos", help="Lista Amigos.",
                    action="store_true")
args = parser.parse_args()

if args.tweet:
    accion.tweet(args.tweet)

if args.buscar:
    if args.cantidad:
        accion.busqueda(args.buscar, args.cantidad)
    else:
        accion.busqueda(args.buscar, 30)

if args.amigos:
    accion.amigos()

#else:
#    print "Para ver ayuda: python main.py -h"


