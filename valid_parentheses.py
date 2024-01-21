''' 
Dada una cadena s que sólo contiene los caracteres '(', ')', '{', '}', '[' y ']'
determina si la cadena de entrada es válida.

Una cadena de entrada es válida si

Los corchetes abiertos deben estar cerrados por el mismo tipo de corchetes.
Los corchetes abiertos deben cerrarse en el orden correcto.
Cada corchete cerrado tiene su correspondiente corchete abierto del mismo tipo.

'''
class Solution:
    def isValid(self, s: str) -> bool:
        l =[]
        for x in s:
            l.append(x)
            print(x)

            if x == "(" or x == "[" or x == "{":
                
                print(f"paso 1 {l}")

            elif len(l) > 1:

                if x == ")" and l[-2] == "(":
                    l.pop()
                    l.pop()
                    
                    print(f"paso 2 {l}")

                elif x == "]" and l[-2] == "[":
                    l.pop()
                    l.pop()

                    print(f"paso 2 {l}")

                elif x == "}" and l[-2] == "{":
                    l.pop()
                    l.pop()

                    print(f"paso 2 {l}")
                    
        print (f"Tamaño: {len(l)}")
        if len(l) == 0:
            return True
        else:
            return False 
        

print("\n** 1 **") 
nuevo = Solution()
print(nuevo.isValid("]"))

print("\n** 2 **")   
nuevo = Solution()
print(nuevo.isValid("()"))

print("\n** 3 **")    
nuevo = Solution()
print(nuevo.isValid("()[]{}"))