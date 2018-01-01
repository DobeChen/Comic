# -------------------------------------------------------------------
# @author DobeChen
# @copyright (C) 2018
# @doc
# 数据转换模块
# @end
# Created : 01. 一月 2018 下午5:28
# -------------------------------------------------------------------
import json


def trans_comic_data(comic_data):
    return json.loads(comic_data)


def trans_chapter_data(chapter_data):
    data = json.loads(chapter_data)
    chapters = data['chapters']
    return chapters[0]
