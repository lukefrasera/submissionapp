import elementtree.ElementTree as et

root = et.Element("doc")
root.set("name", "sd1_prn")
root.set("type", ".doc")

_file = et.SubElement(root, "file")
_file.set("name", "Nameing_Convention")
_file.set("type", ".doc")

title = et.SubElement(root, "title")
title.set("font", "Arial")
title.set("size", "22")
title.set("style", "bold")
title.text = "gameName"

credits = et.SubElement(root, "credits")
credits.set("font", "Arial")
credits.set("size", "18")

creditsList = et.SubElement(credits, "list")
creditsList.set("delimiter", ",")
creditsList.text = "credits"

percentages = et.SubElement(root, "percentages")
percentages.set("font", "Arial")
percentages.set("size", "18")

percentageList = et.SubElement(percentages, "list")
percentageList.set("delimiter", "/")
percentageList.text = "percentages"

tree = et.ElementTree(root)
tree.write("test.css.xml")