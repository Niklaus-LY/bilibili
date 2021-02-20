#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""
@File: test.py
@Description: 
@Author: Niklaus
@Date: 2021/01/18 20:58
"""

import requests
from bilibili_api import video


v = video.get_video_info(bvid="BV13v411v7Zo")
print(v)
djmakus = video.get_danmaku(bvid="BV13v411v7Zo")
for d in djmakus:
    print(str(d).split(",")[-1].strip())
print(len(djmakus))