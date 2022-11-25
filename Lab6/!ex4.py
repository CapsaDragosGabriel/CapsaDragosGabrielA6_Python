import re


def get_xml_matches(path_to_xml, attrs):
    fd = open(path_to_xml, "r")
    line = fd.readline()
    valid_lines = []
    while line:
        all_match = all(list(map(lambda item: re.search(rf'{item[0]}="{item[1]}"', line), attrs.items())))
        if all_match:
            line = line.strip()
            valid_lines.append(line)
        line = fd.readline()
    return valid_lines


if __name__ == '__main__':
    print(get_xml_matches("valeu.xml", attrs={"class": "url", "name": "url-form", "data-id": "item"}))
