grammar YAPL2;
program : 
   programBlock EOF
   ;
programBlock:
   classDEF ';' programBlock
   | EOF
   ;
classDEF : 
    CLASS TYPEID (INHERITS TYPEID)? '{' (feature ';')* '}';
feature : 
    (OBJECTID) '(' (formal (','formal)*)? ')' ':' TYPEID '{' expr '}'
    | OBJECTID ':' TYPEID (ASIGNOPP expr)?;
formal:
    OBJECTID ':' TYPEID;
expr :
    expr ('@' TYPEID)? '.' OBJECTID '(' (expr (',' expr)*)? ')'
    | OBJECTID '(' (expr (',' expr)*)? ')'
    | IF expr THEN expr ELSE expr FI
    | WHILE expr LOOP expr POOL
    | '{' (expr ';')* '}'
    | 'let' OBJECTID ':' TYPEID (ASIGNOPP expr)? (',' OBJECTID ':' TYPEID (ASIGNOPP expr)?)* IN expr
    | NEW TYPEID
    | ISVOID expr
    | expr '*' expr
    | expr '/' expr
    | expr '+' expr
    | expr '-' expr
    | '~' expr
    | expr '<' expr
    | expr '<=' expr
    | expr '=' expr
    | NOT expr
    | '(' expr ')'
    | OBJECTID
    | INTEGERS
    | STRINGS
    | TRUE
    | FALSE
    | OBJECTID ASIGNOPP expr
    ;
//Palabras reservadas
CLASS
   : C L A S S
   ;

ELSE
   : E L S E
   ;

FALSE
   : 'false'
   ;

FI
   : F I
   ;

IF
   : I F
   ;

IN
   : I N
   ;

INHERITS
   : I N H E R I T S
   ;

ISVOID
   : I S V O I D
   ;

LET
   : L E T
   ;

LOOP
   : L O O P
   ;

POOL
   : P O O L
   ;

THEN
   : T H E N
   ;

WHILE
   : W H I L E
   ;

NEW
   : N E W
   ;

NOT
   : N O T
   ;

TRUE
   : 'true'
   ;

//Tipos primitivos

STRINGS
   : '"' (ESC | ~ ["\\])* '"'
   ;
INTEGERS
   : [0-9]+
   ;
TYPEID
   : [A-Z] [_0-9A-Za-z]*
   ;
OBJECTID
   : [a-z] [_0-9A-Za-z]*
   ;
ASIGNOPP
    : '<-'
    ;
fragment A
   : [aA]
   ;
fragment C
   : [cC]
   ;
fragment D
   : [dD]
   ;
fragment E
   : [eE]
   ;
fragment F
   : [fF]
   ;
fragment H
   : [hH]
   ;
fragment I
   : [iI]
   ;
fragment L
   : [lL]
   ;
fragment N
   : [nN]
   ;
fragment O
   : [oO]
   ;
fragment P
   : [pP]
   ;
fragment R
   : [rR]
   ;
fragment S
   : [sS]
   ;
fragment T
   : [tT]
   ;
fragment U
   : [uU]
   ;
fragment V
   : [vV]
   ;
fragment W
   : [wW]
   ;
fragment ESC
   : '\\' (["\\/bfnrt] | UNICODE)
   ;
fragment UNICODE
   : 'u' HEX HEX HEX HEX
   ;
fragment HEX
   : [0-9a-fA-F]
   ;
// Comentarios y espacios en blanco 
   
OPEN_COMMENT
   : '(*'
   ;
CLOSE_COMMENT
   : '*)'
   ;
COMMENT
   : OPEN_COMMENT (COMMENT | .)*? CLOSE_COMMENT -> skip
   ;
ONE_LINE_COMMENT
   : '--' (~ '\n')* '\n'? -> skip
   ;

WHITESPACE
   : [ \t\r\n\f]+ -> skip
   ;
   