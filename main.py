import sys
import os
from antlr4 import *
from YAPL2Lexer import YAPL2Lexer
from YAPL2Parser import YAPL2Parser
from YAPL2Visitor import YAPL2Visitor
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
    print(Trees.toStringTree(tree,None,parser))
    print("Tokens:")
    for token in stream.tokens:
        print(" ",token.text, ':', token.type)
    comand = 'grun YAPL2 program %s -gui'%file
    os.system(comand)
        

if __name__ == "__main__":
    main()