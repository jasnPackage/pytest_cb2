#coding:utf-8

import os

cmd = "pytest -v -m \"not webtest\""

cmd1 = "pytest -v -k \"not send_http\""

cmd2 = "pytest -v -k \"http or quick\""

os.system(cmd2)