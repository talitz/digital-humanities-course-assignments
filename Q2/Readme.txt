--------------------------------------------------------------
Question 2:
--------------------------------------------------------------
1. Are there any mistakes in Meni's tagger?
--------------------------------------------------------------
- It tagged "�� ������ ����" as I_PERS, althouht �� ������ is really a person (and very important one), it is suppose to be tagged as an organization, because
it is a part of organization "���������� �� ������", like we tagged.
- It tagged "�����" as a location, althought it is a part of a person's name (surname).
- It tagged "�����" as I_PERS, althought it is not a person's name but a language.
- It tagged "����", which was part of a book's name as I_ORG, an organization.
--------------------------------------------------------------
2. How private names were tagged?
--------------------------------------------------------------
Private names, like ���� �����, were tagged with I_PERS.
--------------------------------------------------------------
3. How place's names were tagged?
--------------------------------------------------------------
Places like "�������" were tagged with I_LOC.
--------------------------------------------------------------
4. Did it tag private names on the same values we did?
--------------------------------------------------------------
Some names were tagged exactly like we did, for example: 
���� �����, �����, ���, are all tagged as persName, and I_PERS.
Others, due to ambiguity issues, were tagged in a wrong way, for example:
- "���� ����" is a name of a book, not a person's name (it might be, but with the text context it is a book's name).
