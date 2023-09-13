import sys

def lex(expr):
        # lexer
    exseptions = ["+","-","*","/","%","^","(",")","[","]","{","}",":"]
    index = 0
    inquote = False
    while index != len(expr)-1: #adding spaces bettwen tokens
        if expr == "":
            break
        if inquote == False:
            if expr[index] != " ": # diffrence cases
                if expr[index].isnumeric() and not expr[index+1].isnumeric():
                    expr = "".join((expr[:index+1]," ",expr[index+1:]))
                elif expr[index].isalpha() and not expr[index+1].isalpha() and expr[index+1] != "_":
                    expr = "".join((expr[:index+1]," ",expr[index+1:]))
                elif expr[index] in exseptions:
                    expr = "".join((expr[:index+1]," ",expr[index+1:]))  
                elif expr[index] == "\"":
                    inquote = True  
                elif expr[index] == "#":
                    expr = expr[:index]
                    break
            elif expr[index+1] == " ": # removing unneccary spaces
                expr = expr[:index] + expr[index+1:]
                index -= 1
        elif inquote == True and expr[index] == "\"" and expr[index-1] != "\\":
            inquote = False
            expr = "".join((expr[:index]," ",expr[index+1:]))
        elif inquote == True and expr[index] == " ":
            expr = expr[:index] + "_" + expr[index+1:]
        index += 1   
    expr = expr.split(" ") # spliting based on spaces
    while "" in expr:
        expr.remove("") # removing errors
    inquote = False
    for index in range(len(expr)-1):
        if expr[index] == "\"":
            inquote = True  
        elif inquote == True and expr[index] == "\"" and expr[index-1] != "\\":
            inquote = False
        if "_" in expr[index] and inquote == True:
            expr[index] = expr[index].replace("_"," ") # exceptions for strings
    return expr

def evaluate(expr):
    expr = lex(expr)
    for index in range(len(expr)-1):        
        if expr[index] in tokens:
            if tokens[expr[index]]["type"] != "func": # replacing tokens with there values
                expr[index] = str(tokens[expr[index]]["value"])
    return expr

def error(etype:str, line:str, index:int, msg:str, start:int=256, end:int=256,semistart:int=256,semiend:int=256):
    print("ERROR: "+etype+" at line "+str(index+1)+", "+msg)
    print(line[:-1])
    temp = []
    for i in range(len(line)):
        if i >= start and i <= end:
            temp.append("^")
        elif i >= semistart and i <= semiend:
            temp.append("~")
        elif i >= start and i <= semiend:
            temp.append("~")
        elif i >= semistart and i <= end:
            temp.append("~")
        else:
            temp.append(" ")
    print("".join(temp))
    sys.exit()

def makevar(line, locality):
    if len(line) != 4:
        value = 0
    else:
        value = line[3]
    token = {
        "type" : line[0],
        "value" : value,
        "scope" : locality
    }
    return token

tokens = {}

def startup():
    inp = input().split(" ")
    if inp[0] == "rf":
        with open(inp[1]) as tmpfile:
            program = tmpfile.readlines()
        scope = ["global"]
        for index, d in enumerate(program):
            line = lex(d[:-1])
            if len(line) >= 1:
                match line[0]:
                    case "var":
                        if line[3] in tokens:
                            start = len(" ".join(line[:2]))+1
                            end = len(line[3])+start-1
                            error("Name resolution error",d,index,"name: \""+line[3]+"\" already in use",start,end)    
                        temp = makevar(line[1:],scope[-1])
                        tokens[line[3]] = temp
                    case "func":
                        if line[1] in tokens:
                            start = len(line[0])+1
                            end = len(line[1])+start-1
                            semiend = len(d[:-1])-2
                            error("Name resolution error",d,index,"name: \""+line[1]+"\" already in use",start,end,semiend=semiend)
                        token = {
                            "type" : "func",
                            "scope" : scope[-1],
                            "start" : index,
                            "end" : ""
                        }
                        tokens[line[1]] = token
                        scope.append(line[1])
                        args = line[3:-2]
                        for i,arg in enumerate(args):
                            if arg in ["int","str","bool","list"]:
                                tokens[args[i+2]] = makevar(args[i:i+2],scope[-1])
                    case "}":
                        if len(scope) >= 1:
                            scope = scope[:-1]
                
                        



                        

startup()
print(tokens)

