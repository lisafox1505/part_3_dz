#1.
# import json
#
# user_profile = {
#     "username": "super_coder",
#     "level": 10,
#     "languages": ["Python", "English"],
#     "is_active": True
# }
#
# with open("my_dict.json", "w", encoding="utf-8") as f:
#     json.dump(user_profile, f, indent=4, ensure_ascii=False)
# with open("my_dict.json", "r", encoding="utf-8") as f:
#     result = json.load(f)
#     print(result)

#2.
import xml.etree.ElementTree as ET

user_profile = {
    "username": "super_coder",
    "level": 10,
    "languages": ["Python", "English"],
    "is_active": True
}

root = ET.Element("user_profile")
for key, value in user_profile.items():
    if isinstance(value, list):
        sub_elem = ET.SubElement(root, key)
        for i in value:
            sub_elem_item = ET.SubElement(sub_elem, "item")
            sub_elem_item.text = str(i)
    else:
        sub_elem = ET.SubElement(root, key)
        sub_elem.text = str(value)

tree = ET.ElementTree(root)
ET.indent(tree, space="    ", level=0)
tree.write("exercise_xml_tree.xml", encoding="utf-8", xml_declaration=True)

pars = ET.parse("exercise_xml_tree.xml")
root = pars.getroot()

username = root.find("username")
print(f"{username.tag}: {username.text}")

level = root.find("level")
print(f"{level.tag}: {level.text}")

all_items = root.findall("languages/*")
for i in all_items:
    print(f"{i.tag}: {i.text}")

is_active = root.find("is_active")
print(f"{is_active.tag}: {is_active.text}")

#3.
