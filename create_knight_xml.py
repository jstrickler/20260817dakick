import lxml.etree as et

FILE_PATH = 'DATA/knights.txt'

root = et.Element('knights')
with open(FILE_PATH) as knights_in:
    for raw_record in knights_in:
        name, title, color, quest, comment = raw_record.rstrip().split(':')
        knight_tag = et.SubElement(root, 'knight', title=title)
        name_tag = et.SubElement(knight_tag, 'name')
        name_tag.text = name
        et.SubElement(knight_tag, 'color').text = color
        et.SubElement(knight_tag, 'quest').text = quest
        et.SubElement(knight_tag, 'comment').text = comment


xml_doc = et.tostring(root, pretty_print=True, xml_declaration=True)  # to BYTES (binary) string
print(xml_doc.decode())
# print(xml_doc)