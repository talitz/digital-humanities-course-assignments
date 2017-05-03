#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import datetime
from xml.etree import ElementTree
from xml.dom import minidom
from lxml import etree
import xml.etree.ElementTree as ET

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
	
def get_gender(filename):
	string = open(filename,'rb').read()
	if 'נולד ' in string:
		return 'male'
	elif 'נולדה ' in string:	
		return 'female'
	else:
		return 'unknown'
	
file_path = "LexiconDetails.txt"
		
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

education = SubElement(person, 'education')
education.text = " "
############# <div type="content"> #############
div = SubElement(body, 'div')
div.set('type','content')
div.text = "Yael Netzer is onFire!"

############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############

############# </div> #############

############# <div type="content"> #############
div = SubElement(body, 'div')
div.set('type','bibliography')
div.text = "Totah!!!"

############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############
############# COMPLETE HERE!!! #############

############# </div> #############


############# </text> #############

ET.ElementTree(top).write("Q3.XML",encoding="UTF-8",xml_declaration=True)
tree = etree.parse("Q3.XML")
tree.write("Q3.XML", pretty_print=True, encoding='utf-8')