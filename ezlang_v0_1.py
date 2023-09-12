




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
                elif expr[index].isalpha() and not expr[index+1].isalpha():
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
    for index in range(len(expr)-1):
        if "_" in expr[index]:
            expr[index] = expr[index].replace("_"," ") # exceptions for strings
    return expr

def evaluate(expr):
    expr = lex(expr)
    for index in range(len(expr)-1):        
        if expr[index] in tokens:
            if tokens[expr[index]]["type"] != "func": # replacing tokens with there values
                expr[index] = str(tokens[expr[index]]["value"])
    return expr

def makevar(line, locality):
    if len(line) == 4:
        value = 0
    else:
        value = line
    token = {
        "type" : line[0],
        "value" : value,
        "locality" : locality
    }
    return token

tokens = {}

def startup():
    inp = input().split(" ")
    if inp[0] == "rf":
        with open(inp[1]) as tmpfile:
            program = tmpfile.readlines()
        for index, line in enumerate(program):
            line = lex(line[:-1])
            location = ["global"]
            if len(line) >= 1:
                match line[0]:
                    case "var":    
                        temp = makevar(line[1:],location[-1])
                        tokens[temp["name"]] = temp
                    case "func":
                        token = {
                            "type" : "func",
                            "locality" : location[-1],
                            "start location" : index
                        }

                        


startup()
print(tokens)