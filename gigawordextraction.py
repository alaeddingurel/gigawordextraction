#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 11:48:32 2019

@author: user
"""
"""
from lxml import etree
import re
"""



import codecs
import pandas as pd

file = codecs.open("afp_eng_199407", "r").read()
"""
xmlparser = etree.XMLParser()
tree = etree.XML(file, xmlparser)

import xml.etree.ElementTree as ET
root = ET.parse('afp_eng_199407').getroot()

with open("afp_eng_199407") as f:
    xml = f.read()
tree = ET.fromstring(re.sub(r"(<\?xml[^>]+\?>)", r"\1<root>", xml) + "</root>")
"""


from bs4 import BeautifulSoup

soup = BeautifulSoup(file, 'html.parser')



df = pd.DataFrame("documentID", "text")
all_docs = soup.find_all('doc')


row_list = []
for elem in all_docs:
    row_dict = {}
    document_id = elem['id']
    paragraphs = elem.find('text').find_all('p')
    all_text = ""
    for paragraph in paragraphs:
        all_text = all_text + " " + paragraph
    row_dict['id'] = document_id
    row_dict['text'] = all_text
    row_list.append(row_dict)

"""
Paragraphs
soup.find_all('doc')[0].find('text').find_all('p')
Document ID
soup.find_all('doc')[0]['id']
"""
