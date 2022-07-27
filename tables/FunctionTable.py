class FunctionTable:
    def __init__(self):
        self.entries = []

    def addEntry(self, FunctionTableEntry):
        if self.findEntry(FunctionTableEntry.name, FunctionTableEntry.params, FunctionTableEntry.scope, FunctionTableEntry.type, FunctionTableEntry.belongsTo) is None:
            self.entries.append(FunctionTableEntry)
        else:
            print("Function {0} already exists".format(FunctionTableEntry.name))
            return False

    def findEntry(self, name, params, scope, type, belongsTo):
        for entry in self.entries:
            if entry.name == name and entry.params == params and entry.scope == scope and entry.type == type and entry.belongsTo == belongsTo:
                return entry
            else:
                return None

class FunctionTableEntry:
    def __init__(self,name, type, params= None, scope = None,  belongsTo = None):
        self.name = name
        self.params = params
        self.scope = scope
        self.type = type
        self.belongsTo = belongsTo
    def __str__(self):
        return '{0} {1} {2} {3} {4}'.format(self.name, self.type, self.params, self.scope, self.belongsTo)

class FunctionParams:
    def __init__(self, type, name):
        self.type = type
        self.name = name
