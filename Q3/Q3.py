#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
from xml.etree import ElementTree
from xml.dom import minidom

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def seperate_file_to_paragraph(filename):
	file = open(filename,"rb")
	text = file.read().split('\n')
	return [p for p in text if len(p) > 3]
	
print(seperate_file_to_paragraph("LexiconDetails.txt")[0]);	
print(seperate_file_to_paragraph("LexiconDetails.txt")[1]);
print(seperate_file_to_paragraph("LexiconDetails.txt")[2]);
print(seperate_file_to_paragraph("LexiconDetails.txt")[3]);
print(seperate_file_to_paragraph("LexiconDetails.txt")[4]);

top = Element('TEI')

############# teiHeader #############

teiHeader = SubElement(top, 'teiHeader')

fileDesc = SubElement(teiHeader, 'fileDesc')

titleStmt = SubElement(fileDesc, 'titleStmt')


title = SubElement(titleStmt,'title')
title.text = seperate_file_to_paragraph("lex.txt")[-1]

author = SubElement(titleStmt,'author')
author.text = seperate_file_to_paragraph("LexiconDetails.txt")[0]

publicationStmt = SubElement(fileDesc, 'publicationStmt')

publicationStmt_p = SubElement(publicationStmt, 'p')
publicationStmt_p.text = 'Publication Information - None'

sourceDesc = SubElement(fileDesc, 'sourceDesc')
sourceDesc_p = SubElement(sourceDesc,'p')
sourceDesc_p.text = 'https://he.wikipedia.org/wiki/%D7%9C%D7%A7%D7%A1%D7%99%D7%A7%D7%95%D7%9F_%D7%94%D7%A7%D7%A9%D7%A8%D7%99%D7%9D_%D7%9C%D7%A1%D7%95%D7%A4%D7%A8%D7%99%D7%9D_%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99%D7%9D'

############# text #############

text = SubElement(top, 'text')

body = SubElement(text, 'body')
body.text = 'body'

file = open('Q3.xml', 'w');
file.write(prettify(top));
   

