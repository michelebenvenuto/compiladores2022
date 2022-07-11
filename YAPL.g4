//Define a grammar called YAPL
grammar YAPL;

//Basic Definitions

number : '0'|'1'|'2'|'3'|'4'|'5'|'6'|'7'|'8'|'9' ;
upercase : 'A'|'B'|'C'|'D'|'E'|'F'|'G'|'H'|'I'|'J'|'K'|'L'|'M'|'N'|'O'|'P'|'Q'|'R'|'S'|'T'|'U'|'V'|'W'|'X'|'Y'|'Z';
lowercase : 'a'|'b'|'c'|'d'|'e'|'f'|'g'|'h'|'i'|'j'|'k'|'l'|'m'|'n'|'o'|'p'|'q'|'r'|'s'|'t'|'u'|'v'|'w'|'x'|'y'|'z';
simboles : '!';
letter : upercase|lowercase;

//Reserved words

class: 'class'|'CLASS';
else: 'else' | 'ELSE';
false: 'false';
fi : 'fi'|'FI';
if : 'if'|'IF';
in : 'in'|'IN';
inherits : 'inherits'|'INHERITS' ;
isvoid : 'isvoid'|'ISVOID';
loop : 'loop' | 'LOOP';
pool : 'pool' | 'POOL';
then : 'then' | 'THEN';
while : 'while' | 'while';
new : 'new' | 'NEW';
not : 'not' | 'NOT';
true: 'true';
self: 'self';
SELF_TYPE : 'SELF_TYPE';
whiteSpace : '\b'| '\t'|'\f'|' ';
endOfLine : '\n';
whiteSpaces : whiteSpace|endOfLine|'\r';
//IDs
typeIdent : upercase (lowercase|upercase|'_')* ;
objectIdent : lowercase  (lowercase|upercase|'_')* ;

//Operators
arithmeticOperators : '+'|'-'|'/'|'*'|'@'|'.';
logicOperators : '<'| '>'|'<='|'>='|'='|'~'|not;
asignOpp : '<-';


strings : '"' (letter|number|whiteSpace|endOfLine|simboles)* '"';
integer : (number)+;
singleLienComment : '--' (letter|number|whiteSpace)* endOfLine;
multyLineComment : '(*' (letter|number|whiteSpace|endOfLine)* '*)';

program : 
    (classDEF)+;

classDEF : 
    class typeIdent (inherits typeIdent)? '{' (feature ';')* '}';

feature : 
    (objectIdent) '(' (formal (','formal)*)? ')' ':' typeIdent '{' expr '}'
    | objectIdent ':' typeIdent (asignOpp expr);

formal:
    objectIdent ':' typeIdent;
expr :
    objectIdent asignOpp expr
    | expr ('@' typeIdent) '.' objectIdent '(' (expr (',' expr)*)? ')'
    | objectIdent '(' (expr (',' expr)*)?
    | if expr then expr else expr fi
    | while expr loop expr pool
    | '{' (expr ';')* '}'
    | 'let' objectIdent ':' typeIdent (asignOpp expr)? (',' objectIdent ':' typeIdent (asignOpp expr)?)* in expr
    | new typeIdent
    | isvoid expr
    | expr '*' expr
    | expr '/' expr
    | expr '+' expr
    | expr '-' expr
    | '~' expr
    | expr '<' expr
    | expr '<=' expr
    | expr '=' expr
    | not expr
    | '(' expr ')'
    | objectIdent
    | integer
    | strings
    | true
    | false
    ;
    