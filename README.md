# compiladores-Lab0

## Requirements

-ANTlR4 -> You can find it [here](https://www.antlr.org/download.html)

-Python 3 ANTLR runtime -> You can find it [here](https://pypi.org/project/antlr4-python3-runtime/)

## Testing

Before testing this proyect you need to run the following commands the the directory of the YAPLS2.g4 file

```
antlr4 YAPL2.g4
javac YAPLS2.g4
antlr4 -Dlanguage=Python3 YAPL2.g4

```

Then you can run the command:

```
python main.py <test program>  
```
