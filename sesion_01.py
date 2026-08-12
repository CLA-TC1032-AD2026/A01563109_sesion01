import random 

def a_binario(n):
    if n <= 0 : 
        return 0
    binario = []
    while n !=0: 
        bit = n % 2
        binario.insert(0, bit)
        n = n//2
    return binario


def a_hexadecimal(n): 
    if n == 0: 
        return 0
    hexa = []
    while n !=0: 
        bit = n % 16
        if bit == 10:
            bit = "A"
        if bit == 11: 
            bit = "B"
        if bit == 12: 
            bit = "C"
        if bit == 13: 
            bit = "D"
        if bit == 14: 
            bit = "E"  
        if bit == 15: 
            bit = "F"      
        hexa.insert(0, bit)
        n = n//16

    return hexa

def a_decimal (cadena, base):
    inv = reversed (cadena)
    count = 0
    r =0
    for i in inv:
        i = int(i)
        num = (base**(count))*i
        count += 1
        r += num
    return r


    
if __name__ == "__main__":
    n = 156
    print (n, 'En binario es: ', a_binario(n))

    print ('Comprobación de la conversión:: ', bin(n))

    print (n, 'En hexadecimal es: ', a_hexadecimal(n))

    print ('Comprobación de la conversión:: ', hex(n))

    print ('Conversión a decimal de 10011100 con base 2::::  ' , a_decimal("10011100",2))
    print ('Conversión a decimal de 10 con base 8::::  ', a_decimal("10", 8))
    print ('Conversión de 1101 con base 4::::  ', a_decimal("1101", 4))

    print(__name__)
    print(random.__name__)

