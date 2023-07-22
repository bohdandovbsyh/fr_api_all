import xml.etree.ElementTree as ET

tree = ET.parse('films.xml')
root = tree.getroot()

# for child in root:
#     print(child.tag, child.attrib)
#     print('___________________________')
# res = [elem.tag for elem in root.iter()]
# print(res)
# res = ET.tostring(root, encoding='utf8').decode('utf8')
# print(type(res))
# for movie in root.iter('movie'):
#     print(movie.attrib)
# for description in root.iter('description'):
#     print(description.text)
# #     print('***************************************')
# for movie in root.findall("./genre/decade/movie/[year='1992']"):
#     print(movie.attrib)

# b2tf = root.find("./genre/decade/movie[@title='Back to the Future']")
#
# b2tf.attrib["favorite"] = "True"
# tree.write('films.xml')

# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

# import re
#
# for form in root.findall("./genre/decade/movie/format"):
#     # Search for the commas in the format text
#     match = re.search(',', form.text)
#     if match:
#         form.set('multiple', 'Yes')
#     else:
#         form.set('multiple', 'No')
#
# # Write out the tree to the file again
# tree.write("films.xml")
#
# tree = ET.parse('films.xml')
# root = tree.getroot()
#
# for form in root.findall("./genre/decade/movie/format"):
#     print(form.attrib, form.text)

# for decade in root.findall("./genre/decade"):
#     print(decade.attrib)
#     for year in decade.findall("./movie/year"):
#         print(year.text, '\n')
# for movie in root.findall("./genre/decade/movie/[year='2000']"):
#     print(movie.attrib)
action = root.find("./genre[@category='Action']")
new_dec = ET.SubElement(action, 'decade')
new_dec.attrib["years"] = '2000s'

# print(ET.tostring(action, encoding='utf8').decode('utf8'))
xmen = root.find("./genre/decade/movie[@title='X-Men']")
dec2000s = root.find("./genre[@category='Action']/decade[@years='2000s']")
dec2000s.append(xmen)
dec1990s = root.find("./genre[@category='Action']/decade[@years='1990s']")
dec1990s.remove(xmen)

tree.write('films.xml')
# print(ET.tostring(action, encoding='utf8').decode('utf8'))