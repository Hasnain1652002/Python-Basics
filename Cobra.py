from regularExpressions import *
import re


def parseVariableDeclaration(declaration):
    
    match = re.match(patternValidVariable, declaration)
    
    if not match:
        print("Error: Invalid Syntax :(")
        return ("","","")
    
    varDataType = match.group(1)
    varName     = match.group(2)
    varValue    = match.group(3)

    if not re.match(patternVariableName, varName):
        
        print("Error: Invalid variable name :(")
        return ("","","")
    
    elif varName in reservedWords:
        print("Error: Variable name cannot be a reserved word :(")
        return ("","","")
    
    if varDataType == 'int':
        
        if not re.match(patternInt, varValue):
            print("Error: Invalid integer literal :(")
            return ("","","")

    elif varDataType == 'float':
        if not re.match(patternFloat, varValue):
            print("Error: Invalid float literal :(")
            return ("","","")

    elif varDataType == 'string':
        if not re.match(patternString, varValue):
            print("Error: Invalid string literal :(")
            return ("","","")
        varValue = varValue.strip('"')
    
    elif varDataType == 'bool':
        if not re.match(patternBool, varValue):
            print("Error: Invalid boolean literal :(")
            return ("","","")
        varValue = varValue == 'true'
    
    return (varDataType,varName, varValue)



def parseForLoop(code):

    match = re.search(forLoopRE, code,flags=re.DOTALL)

    if not match:
        print("Error : Syntax Error :(")
        return "", "", "", "","","","","",""

    initializerDataType,initializerVariable, initializerValue, conditionVariable, conditionOperators,conditionValue, INCDECVariable, INCDECOperators, loopBody = match.groups()

    match = re.search(r"int", initializerDataType)
    if not match:
        print("Error : Invalid initializer data type :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternVariableName, initializerVariable.strip())
    if not match or initializerVariable.strip()  in reservedWords:
        print("Error : Invalid initializer variable name :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternVariableName, conditionVariable.strip())
    if not match or conditionVariable.strip()  in reservedWords:
        print("Error : Invalid condition variable name :(")
        return "", "", "", "","","","","",""

    match = re.search(patternVariableName, INCDECVariable.strip())
    if not match or INCDECVariable.strip()  in reservedWords:
        print("Error : Invalid inc/dec variable name :(")
        return "", "", "", "","","","","",""
    
    if initializerVariable.strip() != conditionVariable.strip() or initializerVariable.strip() != INCDECVariable.strip():
        print("Error : initializer variable name,condition variable name and inc/dec variable name dont match  :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternInt, initializerValue)
    if not match:
        print("Error : Initializer Value is an invalid integer literal :(")
        return "", "", "", "","","","","",""
    
    match = re.search(patternInt, conditionValue)
    if not match:
        print("Error : Condition Value is an invalid integer literal :(")
        return "", "", "", "","","","","",""

    if conditionOperators not in ['!=', '<', '<=', '>', '>='] :
        print("Error : Invalid Condition Operator :(")
        return "", "", "", "","","","","",""


    return initializerDataType,initializerVariable,initializerValue, conditionVariable ,conditionOperators, conditionValue, INCDECVariable,INCDECOperators, loopBody
