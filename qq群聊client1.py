#!/usr/bin/env python
# -*- coding:uft-8 -*-
# Author:Wwl

import socket

udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

qq_name_dict = {
    'Taylor': ('127.0.0.1', 8081),
    'lana': ('127.0.0.1', 8081),
    'Sia': ('127.0.0.1', 8081)
}
while True:
    qq_name = input('请选择你要聊天的对象：').strip()
    while True:
        msg = input('请输入信息').strip()
        if msg == 'q': break
        udp_client.sendto(msg.encode('utf-8'), qq_name_dict[qq_name])

        back_msg, addr = udp_client.recvfrom(1024)
        print('收到来自%s %s 的消息%s' % (addr[0], addr[1], back_msg.decode('utf-8')))

udp_client.close()