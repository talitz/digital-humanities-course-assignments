--------------------------------------------------------------
Question 1:
--------------------------------------------------------------
We decided to devide the whole text to parts:

1. MetaData (<title>, <author>, <sourceDesc>) which is described in the <teiHeader>.

2. Content - all paragraphs mentioned in the text is seperated by <p></p>, and all content is inside a <div> tag with type = content.
Inside the content, we tagged <persName> like "����� ����" and "���� ����", with the relevant <surname> and <forename>,
We also tagged cities/countries like "�����" or "����" with <placeName> and organizations like "���������� �� ������" or "���������� �� ����" with <orgName>.
We tagged dates like years/months - "2008" or "�����", with <date>. Book names were tagged with <name type="..."></name>, and movies were tagged with type="movie".

3. Bibliography part - a list of all bibliography details, using <listBibl> for all bibliography, and each seperated information with <bibl>.
Each piece of <bibl> information consists of <title>, <publisher>, <date>.


