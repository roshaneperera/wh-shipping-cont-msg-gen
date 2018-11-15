import argparse
import csv
import os
import shutil
import xml.etree.ElementTree as ET

from shipping_container_msg_builder import ShippingContainerRequestBuilder

output_dir = './target/%s'
file_name_prefix = "%s.xml"


class BgColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


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


def generate_shipping_container_msgs(data_list):
    for data in data_list:
        builder = ShippingContainerRequestBuilder()
        element = builder.build(data)
        # result = ET.tostring(element=element, encoding="unicode", method="xml", short_empty_elements=False)
        file_name = (file_name_prefix % data[0])
        destination_file = output_dir % file_name
        ET.ElementTree(element) \
            .write(os.path.abspath(destination_file), encoding="unicode", xml_declaration=True, method="xml")
        print(BgColors.BOLD, BgColors.OKGREEN, "✓", file_name, BgColors.ENDC)


parser = argparse.ArgumentParser(description="generate shippingContainer upload message")
parser.add_argument('location', type=str, nargs=1, help="[csv data file location]")

if __name__ == '__main__':
    initialize()
    args = parser.parse_args()
    fileLocation = args.location[0]
    print('loading data from ', BgColors.UNDERLINE + BgColors.BOLD, fileLocation, BgColors.ENDC)
    generate_shipping_container_msgs(load_csv_data(fileLocation))
