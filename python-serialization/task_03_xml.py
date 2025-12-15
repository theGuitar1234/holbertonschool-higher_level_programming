import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    try:
        root = ET.Element("data")
        
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        
        return True
    except Exception as e:
        print(f"Error during serialization: {e}")
        return False

def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        
        result = {}
        for child in root:
            result[child.tag] = child.text
        
        return result
    except Exception as e:
        print(f"Error during deserialization: {e}")
        return None

if __name__ == "__main__":
    def main():
        sample_dict = {
            'name': 'John',
            'age': '28',
            'city': 'New York'
        }

        xml_file = "data.xml"
        success = serialize_to_xml(sample_dict, xml_file)
        if success:
            print(f"Dictionary serialized to {xml_file}")

        deserialized_data = deserialize_from_xml(xml_file)
        print("\nDeserialized Data:")
        if deserialized_data:
            print(deserialized_data)
        else:
            print("Failed to deserialize data.")

    main()
