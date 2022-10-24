# function(tag,content,keyvalues)
##build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ")
#                   "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"


def build_xml_element2(tag, content, **kwargs):
    string = "<" + tag+" "
    for element in kwargs:
        string = string + element + "=\"" + kwargs[element]+"\""
    string= string+ ">"+content+ "</" + tag + ">"
    return string


def main():

    print(build_xml_element2("a", "Hello there", href="http://python.org", _class =" my-link ", id= " someid "))


main()
