from ParseXML import getTableHWPXML, getTableOOXML, getTextHWPXML, getTextOOXML
import os


def get_extension(self):
    extension = self.rpartition(".")[-1]

    # fn_ext[0] : directory except file_name
    # fn_ext[1] : file_name include extension
    # fn_ext[2] : extension
    fn_direc = os.path.split(self)
    fn_name = os.path.splitext(self)
    file_path = fn_name[0]+'.xml'

    if extension == 'doc' or extension == 'docx':
        global result_table
        result_table = getTableOOXML.return_result(file_path)

        global result_text
        result_text = getTextOOXML.return_result(file_path)

    elif extension == 'hwp':
        result_table = getTableHWPXML.return_result(file_path)

        result_text = getTextHWPXML.return_result(file_path)

    else:
        print("This file is not supported")
        exit(1)

    print('<result_table>\n'+result_table+'\n\n')
    print('<result_text>\n'+result_text+'\n\n')
