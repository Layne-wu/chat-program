#!/usr/bin/env python
# -*- coding:uft-8 -*-
# Author:Wwl


import socket
udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server.bind(('127.0.0.1',8081))

while True:
    qq_msg,addr = udp_server.recvfrom(1024)

    print('来自[%s:%s]的一条消息：%s'%(addr[0],addr[1],qq_msg.decode('utf-8')))
    back_qq_msg = input('请输入：').strip()
    udp_server.sendto(back_qq_msg.encode('utf-8'),addr)