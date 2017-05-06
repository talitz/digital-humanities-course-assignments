#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
from xml.etree import ElementTree
from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

def seperate_file_to_paragraph(filename):
	file = open(filename,"r")
	text = file.read().split('\n')
	return [p for p in text if len(p) > 3]
	
def get_gender(filename):
	string = open(filename,'rb').read()
	if 'נולד ב' in string:
		return 'male'
	elif 'נולדה ב' in string:	
		return 'female'
	else:
		return 'unknown'
            
            
def nextword(target, source):
        for i, w in enumerate(source):
            if w == target:
                return source[i+1]

def get_where_was_born():
	string = seperate_file_to_paragraph(file_path)[3].decode('utf-8')
	for word in string.split():
            if u'נולד' == word:
                return nextword(u'נולד',string.split())[1:]
            if u'נולדה' == word:
                return nextword(u'נולדה',string.split())[1:]
        return 'unknown'
    
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
	tei = ['placeName','persName','orgName','date']
	return tei[ners.index(elm)]

def get_dic_of_word_and_ner3(list):
	dic = {}
	for x in list:
		if x.ner and x.ner[:2] != 'I_':
			continue;
		if x.word in dic and x.ner[:2] == 'I_':
				dic[x.word].append(x.ner)
		elif x.ner[:2] == 'I_':
			dic[x.word] = [x.ner]
	return dic

def get_dic_of_word_and_ner(list):
	dic = {}
	for x in list:
		if not x.ner:
			x.ner = 0
		if x.word in dic:
			dic[x.word].append(x.ner)
		else:
			dic[x.word] = [x.ner]
	return dic


def read_languages_file(filename):
	file = open(filename,"rb")
	text = file.readlines()
	return list(map(get_string_without_last_char, text))

def get_string_without_last_char(string):
	return string[:-1]


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

def create_paragraph(string,dic,langs):
	xml_string = '<p> ' + string + ' </p>'
	ret_string = ''
	for word in xml_string.split(' '):
		if word.replace('.','').replace(',', '').replace('?', '') in dic:
			if dic[word.replace('.','').replace(',','')][0] in ['I_LOC','I_DATE','I_PERS','I_ORG']:
				ret_string = ret_string + tag_word(word,ner_tag_to_tei_tag(dic[word.replace('.','').replace(',','')][0])) + ' '
			else:
				if word.replace('.','').replace(',', '') in langs or word[1:].replace('.','').replace(',', '') in langs or word[2:].replace('.','').replace(',', '') in langs:
					ret_string = ret_string + tag_word(word,'lang') + ' '
				else:
					ret_string = ret_string + word + ' '
			del dic[word.replace('.','').replace(',','')][0]
		else:
			ret_string = ret_string + word + ' '

	ret_string = fix_same_follwing_tags(ret_string)

	root = etree.fromstring(ret_string)
	return root


def fix_same_follwing_tags(string):
	return string.replace('</orgName> <orgName>','').replace('</persName> <persName>','').replace('</placeName> <placeName>','')

def create_xml_bibl_element(bibl):
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
	return top

	
file_path = "lex2.txt"
		
top = Element('TEI')

############# <teiHeader> #############

teiHeader = SubElement(top, 'teiHeader')

fileDesc = SubElement(teiHeader, 'fileDesc')

titleStmt = SubElement(fileDesc, 'titleStmt')

############# <title> #############

title = SubElement(titleStmt,'title')
persName = SubElement(title,'persName')
forename = SubElement(persName,'forename')
str = seperate_file_to_paragraph(file_path)[0].decode('utf-8');
author_forename = str.split(', ',1)[1]; 
forename.text = author_forename;
surname = SubElement(persName,'surname')
author_surname = str.split(', ',1)[0];
surname.text = author_surname;

############# </title> #############

############# <author> #############

author = SubElement(titleStmt,'author')
persName = SubElement(author,'persName')
forename = SubElement(persName,'forename')
str = seperate_file_to_paragraph(file_path)[8].decode('utf-8');
forename.text = str.split(' ',1)[0];
surname = SubElement(persName,'surname')
surname.text = str.split(' ',1)[1];

############# </author> #############

############# <publicationStmt> #############

publicationStmt = SubElement(fileDesc, 'publicationStmt')

publicationStmt_p = SubElement(publicationStmt, 'p')
publicationStmt_p.text = 'Publication Information - None'

############# </publicationStmt> #############

############# <sourceDesc> #############

sourceDesc = SubElement(fileDesc, 'sourceDesc')
sourceDesc_p = SubElement(sourceDesc,'p')
sourceDesc_p.text = 'https://he.wikipedia.org/wiki/%D7%9C%D7%A7%D7%A1%D7%99%D7%A7%D7%95%D7%9F_%D7%94%D7%A7%D7%A9%D7%A8%D7%99%D7%9D_%D7%9C%D7%A1%D7%95%D7%A4%D7%A8%D7%99%D7%9D_%D7%99%D7%A9%D7%A8%D7%90%D7%9C%D7%99%D7%9D'

############# </sourceDesc> #############

############# </teiHeader> #############

############# <text> #############

text = SubElement(top, 'text')

body = SubElement(text, 'body')

############# <head> #############

head = SubElement(body, 'head')

############# <author> #############

persName = SubElement(head,'persName')
surname = SubElement(persName,'surname')
forename = SubElement(persName,'forename')
str = seperate_file_to_paragraph(file_path)[0].decode('utf-8');
forename.text = author_forename
forename.tail = "("
surname.tail = ', '
surname.text = author_surname;

############# <date> #############

date = SubElement(persName,'date')
str = seperate_file_to_paragraph(file_path)[1].decode('utf-8');
dob = str[1:-1]
date.set('when',dob)
date.text = dob
date.tail = ")"

############# </date> #############

############# </author> #############

############# <head> #############


listPerson = SubElement(body, 'listPerson')
person = SubElement(listPerson,'person')
role = seperate_file_to_paragraph(file_path)[2].decode('utf-8');
sex = get_gender(file_path)
where_was_born = get_where_was_born()
person.set('xml:id','dm')
person.set('role',role)
person.set('sex',sex)

persName = SubElement(person,'persName')
surname = SubElement(persName,'surname')
forename = SubElement(persName,'forename')
str = seperate_file_to_paragraph(file_path)[0].decode('utf-8');
forename.text = author_forename
surname.text = author_surname

birth = SubElement(person,'birth')
birth.set('when',dob)

placeName = SubElement(birth,'placeName')
settlement = SubElement(placeName,'settlement')
settlement.set('type','city')
settlement.text = where_was_born

education = SubElement(person, 'education')
education.text = " "
############# <div type="content"> #############
div = SubElement(body, 'div')
div.set('type','content')


###add params###
lex = seperate_file_to_paragraph(file_path)[3:-2]
list_of_tuples = []
tagged_sentences = split_file_to_tagged_sentences('output.txt')
for sentence in tagged_sentences:
	for parsed_word in sentence:
		list_of_tuples.append(TaggedWords(get_word_only(split_to_words(parsed_word)) , get_ner_only(split_to_words(parsed_word))))

langs = read_languages_file("langs")

dic =  get_dic_of_word_and_ner(list_of_tuples)

for x in lex:
	div.append(create_paragraph(x,dic,langs))
###end add params###


###add bibl###
div = SubElement(body, 'div')
div.set('type','bibliography')
listBibl = SubElement(div, 'listBibl')
lex = seperate_file_to_paragraph(file_path)
for x in  get_bibl_of_lex(lex):
	listBibl.append(create_xml_bibl_element(BiblElement(x)))
###end add bibl###


ET.ElementTree(top).write("Q3.XML",encoding="UTF-8",xml_declaration=True)
tree = etree.parse("Q3.XML")
tree.write("Q3.XML", pretty_print=True, encoding='utf-8')