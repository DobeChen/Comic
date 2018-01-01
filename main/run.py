# -------------------------------------------------------------------
# @author DobeChen
# @copyright (C) 2018
# @doc
# @end
# Created : 01. 一月 2018 下午5:28
# -------------------------------------------------------------------
import os
import logging
import config.config as c
import search.searchtool as searchtool
import transdata.transdatatool as transtool

logging.basicConfig(
    filename='Log.log',
    level=logging.DEBUG,
    format='%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s-%(message)s',
    filemode='a'
)
# logging.disable(logging.DEBUG)


def check_file_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

    return path


def main():
    logging.debug('start')

    while True:
        try:
            # input comic name
            print('Please input comic name:')
            name = input()

            params = {'s': name}
            comic_name = searchtool.search_comic(c.SEARCH_COMIC_PATH, params, False)
            if comic_name == '':
                print('No this comic, place try again.')
                continue

            # comic find result
            print('Find those comics:')
            data_list = transtool.trans_comic_data(comic_name)
            for i in range(len(data_list)):
                data = data_list[i]
                print(str(i + 1) + ' : ' + data['name'])

            # choose comic name in result
            print('please choose:')
            choose_num = int(input())

            choose_comic = data_list[choose_num - 1]
            comic_id = str(choose_comic['id'])
            search_chapter_path = c.SEARCH_CHAPTER_URL + comic_id + c.PATH_PARAM

            # chapters find result
            print('Find those chapters:')
            chapter_data = searchtool.search_chapter(search_chapter_path, {}, False)
            chapters = transtool.trans_chapter_data(chapter_data)
            chapter_list = chapters['data']
            for i in range(len(chapter_list)):
                chapter = chapter_list[i]
                print(str(i + 1) + ' : ' + chapter['chapter_title'])

            # choose chapter in result
            print('please choose:')
            chapter_num = int(input())

            choose_chapter = chapter_list[chapter_num - 1]
            chapter_id = str(choose_chapter['chapter_id'])
            chapter_image_path = c.SEARCH_CHAPTER_IMG_URL + comic_id + '/' + chapter_id + c.PATH_PARAM
            image_data = searchtool.search_chapter_image(chapter_image_path, {}, False)

            # get comic images url and download images
            image_urls = transtool.trans_comic_data(image_data)
            image_url_list = image_urls['page_url']
            pars = {'Referer': c.IMAGE_BASE_URL}
            file_path = c.IMAGE_BASE_SAVE_PATH + '/' + choose_comic['name'] + '/' + choose_chapter['chapter_title']
            save_path = check_file_path(file_path) + '/'
            for image_url in image_url_list:
                searchtool.search_download_image(image_url, pars, True, save_path)

            print('download finished')
            print(save_path)

            print('search again (y/n):')
            choose_again = input()
            if choose_again.lower() == 'n':
                break
        except Exception as error:
            logging.debug(error)
            print('try again')

main()
