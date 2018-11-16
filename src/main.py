import argparse
import csv
import os
import shutil
import xml.etree.ElementTree as ET
from util import BgColors, ContainerMsgType
from shipping_container_msg_builder import ShippingContainerRequestBuilder
from rabbit_client import RabbitClient

output_dir = './target/%s'
file_name_prefix = "%s.xml"


def create_stuff():
    a = ET.fromstring('<a></a>')
    b = ET.fromstring('<b></b>')
    b.text = 'hello world'
    a.append(b)
    ET.dump(a)


def load_csv_data(fileLocation):
    lines = []
    with open(fileLocation, mode='r') as csvFile:
        csv_reader = csv.reader(csvFile)
        for row in csv_reader:
            if (len(row) - 1) % 3 != 0:
                print(BgColors.FAIL + '\terror processing line ', row, BgColors.ENDC)
            else:
                lines.append(row)
    return lines


def initialize():
    is_target_exists = os.path.exists('./target')
    if is_target_exists:
        print('removing generated files')
        shutil.rmtree('./target')
    os.mkdir('./target')


def generate_shipping_container_msgs(data_list, msg_type):
    for data in data_list:
        builder = ShippingContainerRequestBuilder(msg_type)
        element = builder.build(data)
        file_name = (file_name_prefix % data[0])
        destination_file = output_dir % file_name
        ET.ElementTree(element) \
            .write(os.path.abspath(destination_file), encoding="unicode", xml_declaration=True, method="xml")
        print(BgColors.BOLD, BgColors.OKGREEN, 'Generated', "✓", file_name, BgColors.ENDC)
        return ET.tostring(element, "utf-8", "xml").decode("utf-8")


parser = argparse.ArgumentParser(description="generate shippingContainer upload message")
parser.add_argument('location', type=str, nargs=1, help="[csv data file location]")

if __name__ == '__main__':
    initialize()
    args = parser.parse_args()
    fileLocation = args.location[0]
    print('loading data from ', BgColors.UNDERLINE + BgColors.BOLD, fileLocation, BgColors.ENDC)Å
    # msg_type = ContainerMsgType.SOPT
    msg_type = ContainerMsgType.MOPT
    generated_msg = generate_shipping_container_msgs(load_csv_data(fileLocation), msg_type)

    client = RabbitClient("localhost", 15672, 'item-master-exchange-item-updated', 'guest', 'guest')
    # un-comment to publish the message to the queue
    client.publish_message('item-master-wh-item-data', generated_msg)
