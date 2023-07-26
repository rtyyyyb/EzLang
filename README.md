# EzLang
a high level version of my assembly like language (EzASM) that shouldnt* be that hard to compile down to assembly

## syntax:
### operators:
---math---
" + " : add      : adds 2 values (int, float, str(concatination))
" - " : subtract : subtracts 2 values (int, float)
" * " : multiply : multiplys 2 values (int, float)
" / " : divide   : divides the first value by the second (int, float)
" ^ " : power    : raises the first values to the power of the second (int, float)
" % " : modulus  : does the first balue mod the second (int,float)
---logic---
" or "   : or   : does bitwise or to 2 interger values (int)
" and "  : and  : does bitwise and to 2 interger values (int) 
" xor "  : xor  : does bitwise xor to 2 interger values (int)
" nor "  : nor  : does bitwise nor to 2 interger values (int)
" nand " : nand : does bitwise nand to 2 interger values (int)
" xnor " : xnor : does bitwise xnor to 2 interger values (int)
### types:
int: 
conversion function "int()" acceptable values (str, float, bool)
bool  :
conversion function "bool()" acceptable values (int(takes the value of the first bit 1 = True, 0 = False)) 
str   :
conversion function "str()" acceptable values (int, float, bool)
float :
conversion function "float()" acceptable values (int, str, bool)

