# -*- coding: utf-8 -*-

import os
from bottle import route,run
from bottle import TEMPLATE_PATH, jinja2_template as template

# HTML生成用Templateディレクトリの指定
TEMPLATE_PATH.append("./views")


@route('/csv/')
def hello():
  files = os.listdir('./')
  return template('index', files=files)

# WebServer起動及び設定
run(host='localhost', port=80)

