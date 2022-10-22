"""euler_9.py Proble 9

Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

from math import sqrt

def main():
    _search_product: int = 1000
    found: bool = False
    
    for _, a in enumerate(range(1,int(_search_product/2))):
        for _, b in enumerate(range(3,int(_search_product/3))):
            
            c: int = _search_product - a - b
            
            if ((a * a) + (b *b) == (c * c)):
                if( a + b + c == _search_product):
                    found = True
                    
                    if a > b:
                        temp = a
                        a = b
                        b = temp
                        
                    print("There exists exactly one Pythagorean triplet for which a + b + c = 1000.")
                    print(f"Pythagorean Triplet: {a} + {b} + {c} = 1000.")
            
            if found:
                break
        
        if found:
            break


if __name__ == "__main__":
    main()
