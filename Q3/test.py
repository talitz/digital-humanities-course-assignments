#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
html = etree.Element("html")
body = etree.SubElement(html, "body")
body.text = u'היי קוראים לי יוסי'
br = etree.SubElement(body, "br")
br.text = "TAIL"
br.tail =u'בדיקה'
et = etree.ElementTree(html)
et.write("test.txt", pretty_print=True, encoding='utf-8')