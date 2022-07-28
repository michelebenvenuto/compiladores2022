import sys
import os
from antlr4 import *
from YAPL2Lexer import YAPL2Lexer
from YAPL2Parser import YAPL2Parser
from YAPL2Visitor import YAPL2Visitor, attributeTable, typesTable, classTable, functionTable
from antlr4.tree.Trees import Trees

def main():
    file = sys.argv[1]
    print(file)
    data = FileStream(file)
    #lexer
    lexer = YAPL2Lexer(data)
    stream = CommonTokenStream(lexer)
    #parser
    parser = YAPL2Parser(stream)
    tree = parser.program()
    comand = 'grun YAPL2 program %s -gui'%file
    os.system(comand)

    #Semantic analysis
    visitor = YAPL2Visitor()
    visitor.visit(tree)
    # Showing tables
    print("==============================SYMBOL TABLE==============================")
    print("==============================ATTRIBUTE TABLE==============================")
    for i in attributeTable.entries:
        print(i)
    print("==============================TYPES TABLE==============================")
    for i in typesTable.entries:
        print(i)
    print("==============================CLASS TABLE==============================")
    for i in classTable.entries:
        print(i)
    print("==============================FUNCTION TABLE==============================")
    for i in functionTable.entries:
        print(i)
    print("==============================END==============================")

if __name__ == "__main__":
    main()