#!/usr/bin/env python
# -*- coding: utf-8 -*-
###### global imports ######
import re
from lxml import etree
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
from xml.etree import ElementTree

###### classes ######
class TaggedWords(object):
	"""docstring for words"""
	def __init__(self, word , ner):
		self.word = word
		self.ner = ner

class BiblElement(object):
	"""docstring for words"""
	def __init__(self, str):
		help = str.split('. ')	
		self.firstname = help[0].split(', ')[1].decode('utf-8')
		self.surename = help[0].split(', ')[0].decode('utf-8')
		self.title = help[1].decode('utf-8')
		self.publisher = help[2].decode('utf-8')
		self.date = help[3].decode('utf-8')
		self.pages = help[4].decode('utf-8')

###### functions ######

def prettify():
	from bs4 import BeautifulSoup
	x = open("Q4.XML","rb")
	print(BeautifulSoup(x, "xml").prettify())


def split_file_to_tagged_sentences(filename):
	file = open(filename, 'rb')
	seperated_text = file.read().split('\n')
	ret = [[]]
	index = 0
	for line in seperated_text:
		if len(line) == 0:
			index = index +1
			ret.append([])
		else:
			ret[index].append(line)

	return [x for x in ret if len(x) != 0]

def split_to_words(string):
	return string.split(' ')

def get_ner_only(elm):
	return elm[-1].replace('\t','').replace('null','')

def get_place_in_setence_only(elm):
	return elm[0].replace('\t','').replace('null','')

def get_word_only(elm):
	return elm[3].replace('\t','').replace('null','')

def ner_tag_to_tei_tag(elm):
	ners = ['I_LOC','I_PERS','I_ORG','I_DATE']
	tei = ['placeName','placeName','orgName','date']
	return tei[ners.index(elm)]

def get_dic_of_word_and_ner(list):
	dic = {}
	for x in list:
		if x.ner and x.ner[:2] != 'I_':
			continue;
		if x.word in dic and x.ner[:2] == 'I_':
				dic[x.word].append(x.ner)
		elif x.ner[:2] == 'I_':
			dic[x.word] = [x.ner]
	return dic

def seperate_file_to_paragraph(filename):
	file = open(filename,"rb")
	text = file.read().split('\n')
	return [p for p in text if len(p) > 3]

def get_bibl_of_lex(lex):
	return lex[-2].split(';')

def get_all_brackets(string):
	return re.findall(r'"(.*?)"',string)

def tag_word(word,tag):
	return '<' + tag + '> ' + word + ' </' + tag + '>'

def create_paragraph(string,dic):
	xml_string = '<p> ' + string + ' </p>'
	ret_string = ''
	for word in xml_string.split(' '):
		if word.replace('.','').replace(',', '').replace('?', '') in dic:
			ret_string = ret_string + tag_word(word,ner_tag_to_tei_tag(dic[word.replace('.','').replace(',','')][0])) + ' '
		else:
			ret_string = ret_string + word + ' '

	root = etree.fromstring(ret_string)
	ET.ElementTree(root).write("Q3.XML",encoding="UTF-8",xml_declaration=True)
	tree = etree.parse("Q4.XML")
	tree.write("Q4.XML", pretty_print=True, encoding='utf-8')

def create_xml_bibl_element(bibl):
	top2 = Element('xml')
	top = Element('bibl')
	persName = SubElement(top, 'persName')
	forename = SubElement(persName, 'forename')
	surename = SubElement(persName, 'surename')
	forename.text = bibl.firstname
	surename.text = bibl.surename
	title = SubElement(top, 'title')
	title.text = bibl.title
	publisher = SubElement(top, 'publisher')
	publisher.text = bibl.publisher
	date = SubElement(top, 'date')
	date.text = bibl.date
	biblScope = SubElement(top, 'biblScope')
	biblScope.set('unit','page')
	biblScope.text = bibl.pages.replace('.','')
	top2.append(top)
	ET.ElementTree(top2).write("Q3.XML",encoding="UTF-8",xml_declaration=True)
	tree = etree.parse("Q3.XML")
	tree.write("Q3.XML", pretty_print=True, encoding='utf-8')

def get_gender(filename):
	string = open(filename,'rb').read()
	if 'נולד ' in string:
		return 'male'
	elif 'נולדה ' in string:	
		return 'female'
	else:
		return 'unknown'

#print get_gender('lex2.txt')

###### main  ######
"""
list_of_tuples = []
tagged_sentences = split_file_to_tagged_sentences('output.txt')
for sentence in tagged_sentences:
	for parsed_word in sentence:
		list_of_tuples.append(TaggedWords(get_word_only(split_to_words(parsed_word)) , get_ner_only(split_to_words(parsed_word))))

dic =  get_dic_of_word_and_ner(list_of_tuples)

lex = seperate_file_to_paragraph("lex2.txt")

create_paragraph(lex[4],dic)
"""

#for x in  get_bibl_of_lex(lex):
#	create_xml_bibl_element(BiblElement(x))


"""	
for word in lex[5].split(' '):
	print word
	if word.replace('.','').replace(',', '').replace('?', '') in dic:
		print dic[word.replace('.','').replace(',','')] , word
"""
"""
print "###"
for x in lex:
	for z in get_all_brackets(x):
		print z
"""

"""

"""


"""

"""


