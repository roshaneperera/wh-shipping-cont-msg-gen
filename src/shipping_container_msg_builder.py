import random
import uuid
import xml.etree.ElementTree as ET
from time import strftime, gmtime

from util import ContainerMsgType
from work_inst_tag_builder import WorkInstructionMsgBuilder
from xml_definitions import XMLDefinitions


class ShippingContainerRequestBuilder:

    def __init__(self, msg_type):
        if msg_type == ContainerMsgType.MOPT:
            self.shippingContainerXML = ET.fromstring(XMLDefinitions.shippingContainerMOPTXML)
        else:
            self.shippingContainerXML = ET.fromstring(XMLDefinitions.shippingContainerSOPTXML)

    @staticmethod
    def gen_scale_event_date():
        return strftime("%Y-%m-%dT%H:%M:%S", gmtime())

    @staticmethod
    def gen_shipping_container_id(number):
        s = "%20s" % number
        return s.replace(' ', '0')

    @staticmethod
    def gen_uuid():
        return uuid.uuid4()

    def get_element(self, tag):
        return self.shippingContainerXML.get(tag)

    def build(self, data):
        self.shippingContainerXML.set('generatedAt', self.gen_scale_event_date())

        self.shippingContainerXML.find('ShippingContainer') \
            .set('id', self.gen_shipping_container_id(data[0]))

        self.shippingContainerXML.set('id', str(self.gen_uuid()))

        w_unit = self.shippingContainerXML.find('ShippingContainer').find('WorkUnit')
        num_of_units = int((len(data) - 1) / 3)
        w_unit.set('instructionCount', str(num_of_units))

        for i in range(num_of_units):
            q_index = (i + 1) * 3
            element = WorkInstructionMsgBuilder(XMLDefinitions.workInstructionXML) \
                .set_quantity(str(data[q_index])) \
                .set_location(data[q_index - 2]) \
                .set_id(str(random.randint(1, 10000))) \
                .set_item(str(data[q_index - 1])) \
                .build()
            w_unit.append(element)

        return self.shippingContainerXML
