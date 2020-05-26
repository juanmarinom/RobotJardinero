# -*- coding: utf-8 -*-
"""
Created on Sun May 17 18:00:03 2020

@author: miguel
"""

import ServerClass
s=ServerClass.Server(8000)
while True :
    data=s.rec (s.all_connections[0])
    print(data) 
    s.send(s.all_connections[0],"237-555-111")