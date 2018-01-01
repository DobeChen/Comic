# -------------------------------------------------------------------
# @author DobeChen
# @copyright (C) 2018
# @doc
# 程序配置
# @end
# Created : 01. 一月 2018 下午5:28
# -------------------------------------------------------------------
import os

# search comic url
SEARCH_COMIC_PATH = 'http://s.acg.dmzj.com/comicsum/search.php'
SEARCH_BASE_URL = 'http://v2.api.dmzj.com/'
# search chapter url
SEARCH_CHAPTER_URL = SEARCH_BASE_URL + 'comic/'
# search chapter image url
SEARCH_CHAPTER_IMG_URL = SEARCH_BASE_URL + 'chapter/'
PATH_PARAM = '.json?channel=Android&version=2.7.003'
# image base url
IMAGE_BASE_URL = 'http://images.dmzj.com/'
# download image path
IMAGE_BASE_SAVE_PATH = os.getcwd() + '/../data'
