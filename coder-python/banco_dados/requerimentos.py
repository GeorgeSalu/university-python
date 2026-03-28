#!/usr/local/bin/python3
try:
    from mysql import connector
except ModuleNotFoundError:
    print("MYSQL Connector não instalado")
else:
    print("MYSQL Connector instalado")