# Generated from YAPL2.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPL2Parser import YAPL2Parser
else:
    from YAPL2Parser import YAPL2Parser

# This class defines a complete generic visitor for a parse tree produced by YAPL2Parser.
from tables.AttributeTable import *
from tables.TypesTable import *
from tables.ClassTable import *
from tables.FunctionTable import *

attributeTable = AttributeTable()
typesTable = TypesTable()
classTable = ClassTable()
functionTable = FunctionTable()
currentScope = 1 
currentClass = "Debugg" 
currentMethod = "Debugg" 

class YAPL2Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPL2Parser#program.
    def visitProgram(self, ctx:YAPL2Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#programBlock.
    def visitProgramBlock(self, ctx:YAPL2Parser.ProgramBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#classDEF.
    def visitClassDEF(self, ctx:YAPL2Parser.ClassDEFContext):
        global currentClass
        global currentMethod
        global currentScope
        className = ctx.TYPEID()[0]
        entry = ClassTableEntry(className)
        classTable.addEntry(entry)
        currentClass = className
        currentMethod = None
        currentScope = 1
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#MethodDef.
    def visitMethodDef(self, ctx:YAPL2Parser.MethodDefContext):
        global currentMethod
        global currentScope
        global currentClass
        functionName = ctx.OBJECTID()
        type = ctx.TYPEID()
        entry = FunctionTableEntry(functionName, type,None, currentScope, currentClass)
        functionTable.addEntry(entry)
        currentMethod = functionName
        currentScope = 2
        return self.visitChildren(ctx)



    # Visit a parse tree produced by YAPL2Parser#FeactureDecalration.
    def visitFeactureDecalration(self, ctx:YAPL2Parser.FeactureDecalrationContext):
        global currentMethod
        global currentScope
        global currentClass
        featureName = ctx.OBJECTID()
        featureType = ctx.TYPEID()
        entry = AttributeTableEntry(featureName, featureType, currentScope, currentClass, currentMethod)
        attributeTable.addEntry(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#formal.
    def visitFormal(self, ctx:YAPL2Parser.FormalContext):
        global currentMethod
        global currentClass
        global currentScope
        featureName = ctx.OBJECTID()
        featureType = ctx.TYPEID()
        entry = AttributeTableEntry(featureName, featureType, currentScope, currentClass, currentMethod)
        attributeTable.addEntry(entry)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#newExpr.
    def visitNewExpr(self, ctx:YAPL2Parser.NewExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#divideExpr.
    def visitDivideExpr(self, ctx:YAPL2Parser.DivideExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#FunctionExpr.
    def visitFunctionExpr(self, ctx:YAPL2Parser.FunctionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#integerExpr.
    def visitIntegerExpr(self, ctx:YAPL2Parser.IntegerExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#trueExpr.
    def visitTrueExpr(self, ctx:YAPL2Parser.TrueExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#MethodExpr.
    def visitMethodExpr(self, ctx:YAPL2Parser.MethodExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#DeclarationExpression.
    def visitDeclarationExpression(self, ctx:YAPL2Parser.DeclarationExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#ifElseExpr.
    def visitIfElseExpr(self, ctx:YAPL2Parser.IfElseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#lessExpr.
    def visitLessExpr(self, ctx:YAPL2Parser.LessExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#BraketedExpr.
    def visitBraketedExpr(self, ctx:YAPL2Parser.BraketedExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#multiplyExpr.
    def visitMultiplyExpr(self, ctx:YAPL2Parser.MultiplyExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#letExpr.
    def visitLetExpr(self, ctx:YAPL2Parser.LetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#stringExpr.
    def visitStringExpr(self, ctx:YAPL2Parser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#lessEqualExpr.
    def visitLessEqualExpr(self, ctx:YAPL2Parser.LessEqualExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#notExpr.
    def visitNotExpr(self, ctx:YAPL2Parser.NotExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#whileExpr.
    def visitWhileExpr(self, ctx:YAPL2Parser.WhileExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#addExpr.
    def visitAddExpr(self, ctx:YAPL2Parser.AddExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#isVoidExpr.
    def visitIsVoidExpr(self, ctx:YAPL2Parser.IsVoidExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#objectIdExpr.
    def visitObjectIdExpr(self, ctx:YAPL2Parser.ObjectIdExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#substractExpr.
    def visitSubstractExpr(self, ctx:YAPL2Parser.SubstractExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#falseExpr.
    def visitFalseExpr(self, ctx:YAPL2Parser.FalseExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#parenthExpr.
    def visitParenthExpr(self, ctx:YAPL2Parser.ParenthExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPL2Parser#equalExpr.
    def visitEqualExpr(self, ctx:YAPL2Parser.EqualExprContext):
        return self.visitChildren(ctx)



del YAPL2Parser