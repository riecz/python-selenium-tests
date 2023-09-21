import os
import json
import xml.etree.ElementTree as ET


def read_json_file(file_path):
    """
    This function reads the data from a json file.
    """

    # Get the path of the file
    rel_path = os.path.relpath(file_path)

    # Check if the JSON file exists
    if not os.path.exists(rel_path):
        raise FileNotFoundError(
            "File '{path}' does not exist.".format(path=rel_path))

    # Open and read the JSON file
    with open(rel_path, 'r', encoding='utf-8') as file:
        file_data = json.loads(file.read())

    return file_data


def read_xml_file(file_path):
    """
    This function reads the data from a xml file.
    """

    # Get the path of the file
    rel_path = os.path.relpath(file_path)

    # Check if the XML file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            "File '{path}' does not exist.".format(path=file_path))

    # Open and read the XML file
    with open(rel_path, 'r', encoding='utf-8') as file:
        file_data = file.read()

    return file_data


def read_expected_xml_message(file_path, replacement_elements: dict = {}):
    """
    This function reads the data from xml file
    and returns into a dictionary format.
    """

    # Check if the expected response file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            "File '{path}' does not exist.".format(path=file_path))

    else:
        tree = ET.parse(file_path)
        root = tree.getroot()
        # print("Xml:", root.tag)

        data = {}  # Dictionary to store extracted XML data

        def traverse_element(element, parent_path):
            path = parent_path + '/' + element.tag
            text = element.text.strip() if element.text else ''
            attributes = element.attrib

            if text or attributes:
                # print('Path:', path)

                if text:
                    # print('Text:', text)
                    # Store the element text in the dictionary
                    data[path] = text

                if attributes:
                    # print('Attributes:', attributes)
                    # Store the element attributes in the dictionary
                    data[path + '/@'] = attributes

            for child in element:
                traverse_element(child, path)

        traverse_element(root, '')

        data.update(replacement_elements)
        return data


def read_actual_xml_message(actual_message, replacement_elements: dict = {}):
    """
    This function reads the data from xml content
    and returns into a dictionary format.
    """

    if not actual_message:
        raise Exception("No actual Message received.")

    else:
        root = ET.fromstring(actual_message)
        # print("Xml:", root.tag)

        data = {}  # Dictionary to store extracted XML data

        def traverse_element(element, parent_path):
            path = parent_path + '/' + element.tag
            text = element.text.strip() if element.text else ''

            # Extract element attributes
            attributes = element.attrib

            if text or attributes:
                # print('Path:', path)

                if text:
                    # print('Text:', text)
                    # Store the element text in the dictionary
                    data[path] = text

                if attributes:
                    # print('Attributes:', attributes)
                    # Store the element attributes in the dictionary
                    data[path + '/@'] = attributes

            for child in element:
                traverse_element(child, path)

        traverse_element(root, '')

        data.update(replacement_elements)
        return data


def compare_xml_attributes(xml_file_1, xml_file_2, attribute_1, attribute_2):
    """
    This function compares 2 attributes in 2
    distinct xml messages and returns a boolean value.
    """

    # Extract the attributes
    attribute_1_value = get_attribute_value_from_xml_string(
        xml_file_1, attribute_1)
    print("attribute_1_value: ", attribute_1_value)
    attribute_2_value = get_attribute_value_from_xml_string(
        xml_file_2, attribute_2)
    print("attribute_2_value: ", attribute_2_value)

    # Check if attributes are found and compare their values
    if attribute_1_value and attribute_2_value:
        return attribute_1_value == attribute_2_value
    else:
        return False


def get_attribute_value_from_xml_string(xml_string, path):
    """
    Use XPath to find the value of the desired attribute from XML string.
    """
    try:
        tree = ET.fromstring(xml_string)
        element = tree.find(path)
        result = element.text.strip()
        return result if element is not None and element.text else None
    except ET.ParseError:
        print("Error parsing XML content.")
        return False
