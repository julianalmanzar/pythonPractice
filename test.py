import json
import xml.etree.ElementTree as ET

##Leer archivo JSON y hacerlo diccionario o String
# archivo = open('test_data.json')
# data = json.load(archivo)
# print(type(data[0]))
# print(data[0]['fields'].keys())
# cute_json = json.dumps(data[0], indent=8)
# print(type(cute_json))

##Leer string en JSON y hacerlo diccionario o imprimirlo bonito
#json_str = '{ "name":"John el Esquisofrenico", "age":30, "cities": ["New York", "Masachussets", "Doral"]}'
#json_conv = json.loads(json_str)
#print(json.dumps(json_conv, indent=4))
#print(type(json_conv))


#Leer archivo XML y manipularlo
xmltree = ET.parse('test_data.xml')
root = xmltree.getroot()
result = root.find('empleado')
for element in root[0].iter():
    print("", element.tag)
# print(type(root))
# print(root[0][0].text)
# print(root[0][1].text)
# print(root[0][4].text)
# print(ET.tostring(root))


# for child in root:
#     print(child.tag, child.attrib)
#     #print(element.get('cedula'))
#     #print(element.find('nombre').text)
# print([elem.tag for elem in root.iter()])
for element in root.findall("./empleado/[@cedula='40200499362']"):
    print(element.find('departamento').text)
