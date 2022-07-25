# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPL2Parser import YAPL2Parser
else:
    from YAPL2Parser import YAPL2Parser

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.

class YAPL2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPL2Parser#program.
    def visitProgram(self, ctx:YAPL2Parser.ProgramContext):
        print(self.visitChildren(ctx))
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#programBlock.
    def visitProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#classDEF.
    def visitClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#feature.
    def visitFeature(self, ctx:YAPL2Parser.FeatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#formal.
    def visitFormal(self, ctx:YAPL2Parser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#expr.
    def visitExpr(self, ctx:YAPL2Parser.ExprContext):
        children = ctx.children
        print("Father:", ctx.getText())
        print("Children:")
        for child in children:
            print(" ",child.getText())

        return self.visitChildren(ctx)



del YAPL2Parser