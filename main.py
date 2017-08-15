from bs4 import BeautifulSoup
import requests
import re
import progressbar
import time
from get_serp import *

#start page
url = "https://www.google.com.tw/search?biw=1152&bih=623&q=%E7%85%8E%E9%AD%9A%E5%B9%AB%E6%89%8B&oq=%E7%85%8E%E9%AD%9A%E5%B9%AB%E6%89%8B&gs_l=psy-ab.3..0i71k1l4.0.0.0.3263.0.0.0.0.0.0.0.0..0.0....0...1..64.psy-ab..0.0.0.E-wlFMQPPpM"

page_count = 0
bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength) 
serp_list = []

for page in range(0, 3):  #page1 ~ page2
    text = requests.get(url).text
    soup = BeautifulSoup(text, "html.parser")
    
    get_title(soup, serp_list)
    url = next_page(soup)
    page_count += 1
    bar.update(page_count)
    if page_count % 4 == 0:
        time.sleep(60*1) 
