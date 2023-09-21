'''
The XmlTransformer class contain functions to manipulate original xml files
'''
from xml.etree import ElementTree as et


class XmlTransformer():

    def replace(self, xml_text: str, path: str, value: str):
        '''
        This function takes an xml string and
        replaces the value for a certain field.
        Example:
        - xml_text:
          <a>
            <b>
              <c>Hello</c>
            </b>
          </<a>
        - key: '/a/b/c'
        - value: 'World'
        Running the replace function with above parameters
        should result in the following text:
          <a>
            <b>
              <c>World</c>
            </b>
          </<a>
        '''
        tree = et.fromstring(xml_text)
        tree.find(path).text = value
        return et.tostring(tree, encoding='utf-8').decode('utf-8')
