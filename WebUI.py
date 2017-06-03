# -*- coding: utf-8 -*-

import os
from bottle import route,run,static_file
from bottle import TEMPLATE_PATH, jinja2_template as template

# HTML生成用Templateディレクトリの指定
TEMPLATE_PATH.append("./views")
file_dir="./"


@route('/csv/')
def hello():
  files = os.listdir(file_dir)
  return template('index', files=files)

@route('/download/<file_path>')
def static(file_path):
    return static_file(file_path, root=file_dir, download=True)

# WebServer起動及び設定
run(host='localhost', port=80, debug=True, reloader=True)

