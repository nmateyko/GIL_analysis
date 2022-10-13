import xml.etree.ElementTree as ET

tree = ET.parse('DemultiplexingStats.xml')
root = tree.getroot()

barcodes = []

for barcode in root.iter('Barcode'):
  name = barcode.get('name')
  if name != "all":
    barcodes.append((name, int(barcode[0].find('BarcodeCount').text)))

barcodes = sorted(barcodes, key=lambda x: x[1], reverse=True)
print(barcodes)