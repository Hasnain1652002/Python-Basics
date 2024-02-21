from res import DT, ID, arith_op, integer, floating_point_number, cond_op, logic_op


def operand_tokens(expression_list):
    print(expression_list)

    operators = ['+', '-', '*', '/', '^', '//', '%', '==', '!=', '<', '>', '<=', '>=', '&', '||', "and", "or"]
    new_list = []
    for item in expression_list:
        found_operator = False
        for operator in operators:
            if item == operator:
                new_list.append(item)
                found_operator = True
                break
        
        if not found_operator:
            l = []
            operand = ""
            for char in item:
                if char not in operators:
                    operand += char
                else:
                    if len(operand) != 0:
                        l.append(operand)
                    l.append(char)
                    operand = ""
            
            if len(operand) != 0:
                l.append(operand)
            
            new_list.extend(l)
    
    return new_list





def init_parser(string):
    print("initialization")
    tokens = operand_tokens(string.split())
    print(tokens)

    # first token must be datatype
    if (DT(tokens[0])):
        expression_string = ""
        # rest of the tokens are part of the expression
        for token in tokens[1:]:
            expression_string += token
            expression_string += " "
        # check if expression is correct
        expression_parser(expression_string[:-1])

    else:
        raise ValueError("Invalid Datatype")
    


def expression_parser(string):
    print("expression")
    tokens = operand_tokens(string.split())
    print(tokens)

    # length of an expression is always odd.
    if len(tokens)%2 == 1:

        for i in range(len(tokens)):
            
            if i%2==0: # even numbers are operand
                if not ID(tokens[i]) and not integer(tokens[i]) \
                    and not floating_point_number(tokens[i]): # if invalid operand

                    raise SyntaxError("Invalid Operand.")
                
            elif i==1: # 2nd token must be the assignment operator
                if tokens[i] != '=':
                    raise SyntaxError("Assignment operator '=' missing in expression.")
                
            else: # odd numbers are operators
                if not arith_op(tokens[i]): # if invalid operator
                    raise SyntaxError("Invalid operator in statement.")
                
    else:
        raise SyntaxError("Invalid Expression.")



def conditions_parser(string):
    print("conditional statements")

    tokens = operand_tokens(string.split())
    print(tokens)
        

    if (len(tokens)%2)==1:        

        num_of_conditions = len(tokens)//3
        i = 0
        for j in range(num_of_conditions):
            
            if not ID(tokens[i]):
                raise SyntaxError("Invalid ID syntax in condition.")
            i = i+1
                

            if not cond_op(tokens[i]):
                raise SyntaxError("Invalid 'Comparision Operator' in condition.")
            i = i+1
                

            if not ID(tokens[i]) and not (integer(tokens[i]) or floating_point_number(tokens[i])):
                raise SyntaxError("Invalid operand in condition.")
            i = i+1 
                

            if (j != num_of_conditions-1):
                if not logic_op(tokens[i]):
                    raise SyntaxError("Invalid 'Logical Operator' in condition.")
                i = i+1
            
       


    else:
        raise SyntaxError("Invalid conditional statement.")



def inc_dec_parser(string):
    expression_parser(string)



def loop_parser(string):

    def check_extras(sub_string):
        if (len(sub_string.strip()) > 0):
            raise SyntaxError("Invalid Loop Syntax")

    # checking iterative keyword
    string = string.strip()
    iterate_keyword = string[:7]
    if iterate_keyword != "iterate":
        raise SyntaxError("Expected 'iterate' keyword")
    
    # checking opening paranthesis
    i = string.find('(')
    if i == -1: # no "(" present
        raise SyntaxError("Expected 'Left Paranthesis *(*' after 'iterative' keyword")
    
    # checking if there are garbage values between iterate and (
    if i-7>=1:
        check_extras(string[7:i])
        
    # checking closing paranthesis
    j = string.find(')')
    if j == -1: # no "(" present
        raise SyntaxError("Expected 'Right Paranthesis *)*' after 'inc/dec' statement")
    

    # seperating loop statements
    loop_statements = string[i+1:j]
    statements = loop_statements.split(',')
    
    if len(statements)!=3:
        raise SyntaxError(f"Expected 3 loop statements, got only {len(statements)}")
    

    init_statement, cond_statement, inc_dec_statement = statements

    # for loop's initialization/expression statement
    if DT(init_statement.split()[0]):
        init_parser(init_statement)

    else:
        expression_parser(init_statement)



    # for loop's conditional statement
    conditions_parser(cond_statement)


    # for loop's conditional statement
    inc_dec_parser(inc_dec_statement)



    # separating main statements

    # checking opening bracket
    i = string.find('[')
    if i == -1: # no "(" present
        raise SyntaxError("Expected 'Left Square Bracket *[*' after loop statements")
    
    # checking if there are garbage values between ) and [
    if i-j>1:
        check_extras(string[j+1:i])

    
    # checking closing bracket
    if string[-1] != ']': # no "(" present
        raise SyntaxError("Expected 'Right Square Bracket *]*' at the end")
    

    statements = [statement.strip() for statement in string[i+1:-1].split('\n') if statement.strip()]
    for statement in statements:
        tokens = statement.split()
        if tokens[0]
    





if __name__ == '__main__':

    input_string = """
        iterate (int a = 157 + d, a <= 3 and z != g, a = d + e) [
            float xy = 12.4
            int z = k
        ]"""
    
    tokens = loop_parser(input_string)

