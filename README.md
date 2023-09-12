# EzLang

## info

EzLang is is a high level proggraming language that is meant to have easy to learn syntax and to be easy to go from a idea to a program. it will mainly be interprited but i do plan on making a customisabe compiler compilers.
the offical discord server can be found here https://discord.gg/ez9FudnDxS where you can talk about anyhting your using EzLang for or any questions have about the lang and keep updated on the progress

## syntax 

this section will go over all the syntax you need to know to get started with programming EzLang

---

### variables

there are 2 kinds of variables. global and local. global variables are defined using the `var` keyword the the type with a `:` and the name of a variable with its value
examples:
```
var int:foo 108
var str:bar "hello"
var bool:dec True
var list:nub [1, 0, 4]
```
Unassigned variables have default values listed below:
- int : 0
- str : ""
- bool : False
- list : [ ]
  
global variables can be accessed and changed globaly no matter where its being changed or accessed like seen below::
```
var int:foo
# foo is global

func bar(int:x){
    ret: foo + x
}

var bool:done

while done == False{
    bar(foo)
    done = True
}

for i in [10]{
    foo += 1
}
```
locals can only be accessed and changed if it is in there local space and are created by: 
- defining a variable in a function
- any function argument
- the counter in a for loop
exsamples are shown below:
```
func bar(int:foo){
    var int:x 10
    # both variables x and foo are local to this function
}

for i in [1:5]{ 
    i += 1
    # i is local to the for loop
}
```









