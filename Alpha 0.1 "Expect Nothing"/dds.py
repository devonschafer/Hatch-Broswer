#DevonDataStructure
#v1.0.0
import os


class DDS():

    virtual_filename = '''title1::DDS,,Helvetica,,30
    title2::Devon Data Structure,,Helvetic,,20
    header1::A page to show the DDS documentation,,Helvetic,,10
    body1::Why was dds developed?. The vision is to create a data structure that is simple to write and understand. A data structure that can be read and written to from programs or by hand. In my years of working with other data structures and data sets, I wanted certain data structures to work differently. Hopefully others will see the value in dds too.,,Helvetic,,10
    body2::Welcome. This is vanilla dds. This uses python3, and the built-in tkinter library for the "docs & examples" gui(ddsdocs.py). Both the v1 dds module and the v1 "docs & examples" gui(ddsdocs.py) will not use modules or libraries other than those built-in to python3. The goal of dds is to keep things simple, no third party installations, dds.py is meant to be added to your python3 PATH or simply copied to your project's directory. Once copied to your project's directory you can import the module by "from dds import DDS". You do not have to interact with the "docs & examples" gui(ddsdocs.py), this is to show one way that dds can be used and to explain the documentation. dds_docs.dds contains the documentation in dds format. testdata.dds contains test data in dds format. dds.py is the module. ddsdocs.py is the documentation and examples gui built in python3-tkinter.,,Helvetic,,10
    body3::v1.0.0\nThird digit, increased by 2, is the version of the GUI(frontend)\nSecond digit, increased by 2, is the version of the dds module(backend)\nFirst digit, increased by 1, is the version of the entire project when the third, second, or both digits have reached 8 (or fourth revision).,,Helvetica,,10
    body4::DDS.readFile(filename, option, values)\nDDS.returnLine(filename, option, values)\nDDS.returnKey(filename, option, values)\nDDS.return Multiplekeys(filename, option, values)\nDDS.returnValue(filename, option, values)\nDDS.valuesToList(filename, option, values)\nDDS.returnSpecificValue(filename, option, values)\nDDS.appendFile(filename, option, values)\nDDS.searchByKey(filename, option, values)\nDDS.virtualFile(filename, option, values),,Helvetica,,10'''
    
    def readFile(filename, option, values):
        openFile = open(filename, 'r')
        if option == 'all' and values == None:
            readFile = openFile.read()
            return readFile
        openFile.close()

    def returnLine(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == None:
            line = openFile.readlines()
            return line[option-1]
        openFile.close()

    def returnKey(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, str) and values == 'key':
            line = openFile.readlines()
            for lines in line:
                if option in lines:
                    value = lines.split('::')
                    return value[0]
        elif isinstance(option, int) and values == 'key':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[0]
        openFile.close()

    def returnMultipleKeys(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and 0 not in option and values == 'key':
            i = []
            line = openFile.readlines()
            for k in range((option[0]-1), option[1]):
                skey = line[k].split('::')
                i.append(skey[0])
            return i
        openFile.close()

    def returnValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, str) and values == 'value':
            line = openFile.readlines()
            for lines in line:
                if lines.startswith(option):
                    value = lines.split('::')
                    return value[1]
        elif isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            return line[1]
        openFile.close()

    def valuesToList(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, int) and values == 'value':
            line = openFile.readlines()
            line = line[option-1].split('::')
            v = line[1].split(',,')
            return v
        openFile.close()

    def returnSpecificValue(filename, option, values):
        openFile = open(filename, 'r')
        if isinstance(option, tuple) and values == 'value':
            line = openFile.readlines()
            line = line[option[0]-1].split('::')
            opt = line[1].split(',,')
            return opt[option[1]-1]
        openFile.close()

    def appendFile(filename, option, values):
        saveFile = open(filename, 'a')
        if isinstance(option, str) and values == 'save':
            saveFile.write('\n%s' % option)
        saveFile.close()

    def virtualFile(filename, option, values):
        if option == None and values == 'key':
            return filename.split('::')[0]
        elif isinstance(option, int) and values == 'value':
            line = filename.split('::')[1]
            opt = line.split(',,')
            return opt[option-1]
        elif option == None and values == 'value':
            return filename.split('::')[1]

    def virtualRead(filename, option, values):
        line = filename.split('\n')
        if isinstance(option, tuple) and values == 'read':
            l = line[option[0]-1].split('::')
            opt = l[1].split(',,')
            return opt[option[1]-1]

    def countLines(filename, option, values):
        openFile = open(filename, 'r')
        if option == 'all' and values == 'count':
            line = openFile.readlines()
            return len(line)
        openFile.close()

    def virtualLines(filename, option, values):
        line = filename.split('\n')
        if option == 'all' and values == 'count':
            if '' in line:
                line.remove('')
            return len(line)
        openFile.close()

            
#t = DDS.readFile('testdata.dds', 'all', None)
#t = DDS.returnLine('DDS_page.dds', 3, None)
#t = DDS.returnKey('DDS_page.dds', 8, 'key')
#t = DDS.returnKey('testdata.dds', 'This works', 'key')
#t = DDS.returnMultipleKeys('testdata.dds', (1,8), 'key')
#t = DDS.returnValue('testdata.dds', 3, 'value')
#t = DDS.returnValue('testdata.dds', 'latte', 'value')
#t = DDS.valuesToList('testdata.dds', 3, 'value')
#t = DDS.returnSpecificValue(DDS.virtual_filename, (3,1), 'value')
#t = DDS.appendFile('testdata.dds', 'Testing Again::This is working', 'save')
#t = DDS.searchByKey('testdata.dds', 'Hello', (1,8))
#t = DDS.virtualFile(DDS.virtual_filename, None, 'key')
#t = DDS.virtualFile(DDS.virtual_filename, None, 'value')
#t = DDS.virtualFile(DDS.virtual_filename, None, 'value')
#t = DDS.virtualRead(DDS.virtual_filename, (2,3), 'read')
#t = DDS.countLines('DDS_page.dds', 'all', 'count')
#print(t)
    
