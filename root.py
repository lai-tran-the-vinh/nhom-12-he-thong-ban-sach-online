from lxml import etree
import os

currentDirectory = os.path.dirname(os.path.abspath(__file__))
xmlFilename = os.path.join(currentDirectory, 'root.xml')
xml = etree.parse(xmlFilename)

xml = etree.parse("root.xml")
xsl = etree.parse("root.xsl")
transform = etree.XSLT(xsl)
result = transform(xml)

with open("result.html", "wb") as f:
    f.write(etree.tostring(result, pretty_print=True, method="html"))

print("Đã tạo file result.html — mở file này để xem kết quả.")
