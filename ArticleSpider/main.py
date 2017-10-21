__author__ = 'xuan'

from scrapy.cmdline import execute

import sys
import os
#获取当前目录
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(["scrapy","crawl","jobbole"])