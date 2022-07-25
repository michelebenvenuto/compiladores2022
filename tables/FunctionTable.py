class FunctionTable:
    def __init__(self):
        self.entries = []

    def addEntry(self, FunctionTableEntry):
        self.entries.append(FunctionTableEntry)

    def findEntry(self, name, params, scope, type, belongsTo):
        for entry in self.entries:
            if entry.name == name and entry.params == params and entry.scope == scope and entry.type == type and entry.belongsTo == belongsTo:
                return entry
            else:
                raise NameError("{0} Not declared in {1}".format(name,belongsTo))

class FunctionTableEntry:
    def __init__(self,name, params, scope, type, belongsTo):
        self.name = name
        self.params = params
        self.scope = scope
        self.type = type
        self.belongsTo = belongsTo

class FunctionParams:
    def __init__(self, type, name):
        self.type = type
        self.name = name
