# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPL2Parser import YAPL2Parser
else:
    from YAPL2Parser import YAPL2Parser

# This class defines a complete listener for a parse tree produced by YAPL2Parser.
class YAPL2Listener(ParseTreeListener):

    # Enter a parse tree produced by YAPL2Parser#program.
    def enterProgram(self, ctx:YAPL2Parser.ProgramContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#program.
    def exitProgram(self, ctx:YAPL2Parser.ProgramContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#programBlock.
    def enterProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#programBlock.
    def exitProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#classDEF.
    def enterClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#classDEF.
    def exitClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#feature.
    def enterFeature(self, ctx:YAPL2Parser.FeatureContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#feature.
    def exitFeature(self, ctx:YAPL2Parser.FeatureContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#formal.
    def enterFormal(self, ctx:YAPL2Parser.FormalContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#formal.
    def exitFormal(self, ctx:YAPL2Parser.FormalContext):
        pass


    # Enter a parse tree produced by YAPL2Parser#expr.
    def enterExpr(self, ctx:YAPL2Parser.ExprContext):
        pass

    # Exit a parse tree produced by YAPL2Parser#expr.
    def exitExpr(self, ctx:YAPL2Parser.ExprContext):
        pass



del YAPL2Parser