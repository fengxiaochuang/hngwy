# python
# -*- coding: utf-8 -*-
import logging
import os


def save_file(dirname, data):
    """ save file to local
    :param dirname: 路径
    :param data: 数据
    """

    path, file_name = os.path.split(dirname)
    if not os.path.isdir(path):
        os.makedirs(path)
    filename = open(dirname, 'w')
    try:
        filename.write(data)
    except Exception as e:
        logging.error("%s,%s SaveFileError" % (format(e), dirname))
    finally:
        filename.close()


def createPath(path):
    """创建路径"""
    if not os.path.isdir(path):
        os.makedirs(path)
