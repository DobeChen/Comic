# -------------------------------------------------------------------
# @author DobeChen
# @copyright (C) 2018
# @doc
# 程序搜索模块
# @end
# Created : 01. 一月 2018 下午5:28
# -------------------------------------------------------------------
import logging
import requests

logging.basicConfig(
    filename='Log.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s',
    filemode='a'
)
# logging.disable(logging.DEBUG)


def common_search(url, pars, has_header):
    if has_header:
        response = requests.request('GET', url, headers=pars)
    else:
        if len(pars):
            response = requests.get(url, pars)
        else:
            response = requests.get(url)

    status_code = response.status_code

    if 200 != status_code:
        return ''
    return response


def search_comic(url, pars, has_header):
    comic_names = ''

    response = common_search(url, pars, has_header)
    if response != '':
        try:
            content = response.text

            start_index = content.find('[')
            end_index = content.rfind(']')
            if (end_index - start_index) == 1:
                return ''

            data = content[start_index: end_index + 1]
            comic_names = data
        except Exception as error:
            logging.debug(error)

    return comic_names


def search_chapter(url, pars, has_header):
    chapters = ''

    response = common_search(url, pars, has_header)
    if response != '':
        try:
            content = response.text
            chapters = content
        except Exception as error:
            logging.debug(error)

    return chapters


def search_chapter_image(url, pars, has_header):
    response = common_search(url, pars, has_header)
    if response != '':
        try:
            content = response.text
            return content
        except Exception as error:
            logging.debug(error)

    return ''


def search_download_image(url, pars, has_header, save_path):
    response = common_search(url, pars, has_header)
    if response != '':
        try:
            content = response.content

            start_index = url.rfind('/') + 1
            end_index = len(url) + 1
            file_name = url[start_index: end_index]

            file_path = save_path + file_name
            file = open(file_path, 'wb')
            file.write(content)
            file.close()
        except Exception as error:
            logging.debug(error)
