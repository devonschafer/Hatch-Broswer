#DevonDataStructure
#v1.0.0
import os


class DDS():
    
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

    #does not account for lines already there, needs to scan and not copy lines already existing
    #is I get this working, this should serve as a save function too.
    def writeFile(filename, option, values):
        saveFile = open(filename, 'w')
        if isinstance(option, str) and values == 'save':
            saveFile.write('%s' % option)
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
            if '::' in line[option[0]-1]:
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
    
