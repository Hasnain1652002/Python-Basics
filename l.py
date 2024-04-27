import nltk

# Define the CFG production rules
grammar = nltk.CFG.fromstring("""
<for-loop> -> for ( <init-statement> ; <condition> ; <iteration-expression> ) ;

<init-statement> -> <declaration> | <simple-expression> | ε

<declaration> -> <type> <identifier> = <initializer>

<type> -> int | float | double | char | bool | ...

<identifier> -> [A-Za-z_][A-Za-z0-9_]*

<initializer> -> <expression>

<simple-expression> -> <expression>

<expression> -> <term> | <expression> <additive-operator> <term>

<term> -> <factor> | <term> <multiplicative-operator> <factor>

<factor> -> <primary-expression> | <unary-operator> <factor>

<primary-expression> -> <identifier> | <literal> | ( <expression> )

<literal> -> <integer-literal> | <float-literal> | <char-literal> | <string-literal> | ...

<additive-operator> -> + | -

<multiplicative-operator> -> * | / | %

<unary-operator> -> ++ | --

<condition> -> <expression> | ε

<iteration-expression> -> <expression> | ε

""")

# Example input
input_code =" for (int i = 0; i < 10; i++) ;"

# Create a parser from the CFG
parser = nltk.ChartParser(grammar)

# Tokenize the input code
tokens = input_code.split()

# Parse the input code
for tree in parser.parse(tokens):
    tree.pretty_print()
