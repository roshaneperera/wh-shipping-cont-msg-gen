import xml.etree.ElementTree as ET


class WorkInstructionMsgBuilder:
    _quantityTag = "Quantity"
    _locationTag = "Location"
    _workInstructionTag = "WorkInstruction"
    _itemTag = "Item"
    _xmlObj = None

    def __init__(self, xml):
        self._xmlObj = ET.fromstring(xml)

    def __element(self, tag):
        return self._xmlObj.find(tag)

    def set_id(self, value):
        tag = self._xmlObj
        tag.set('id', value.strip(' '))
        return self

    def set_location(self, value):
        location = self._xmlObj.find(self._locationTag)
        location.text = value.strip(' ')
        return self

    def set_quantity(self, value):
        quantity = self._xmlObj.find(self._quantityTag)
        quantity.text = value.strip(' ')
        return self

    def set_item(self, value):
        item = self._xmlObj.find(self._itemTag)
        item.text = value.strip(' ')
        return self

    def build(self):
        return self._xmlObj
