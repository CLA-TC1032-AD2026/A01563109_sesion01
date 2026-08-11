def a_binario(n: int) -> str:
    """Convierte un entero no negativo a su representación binaria (str), sin usar bin()."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n == 0:
        return "0"

    digitos = []
    while n > 0:
        digitos.append(str(n % 2))
        n //= 2
    return "".join(reversed(digitos))


def a_hexadecimal(n: int) -> str:
    """Convierte un entero no negativo a su representación hexadecimal (str), sin usar hex()."""
    if n < 0:
        raise ValueError("n debe ser un entero no negativo")
    if n == 0:
        return "0"

    simbolos = "0123456789ABCDEF"
    digitos = []
    while n > 0:
        digitos.append(simbolos[n % 16])
        n //= 16
    return "".join(reversed(digitos))


def a_decimal(cadena: str, base: int) -> int:
    """Convierte una cadena en base 2, 8 o 16 a su valor decimal."""
    if base not in (2, 8, 16):
        raise ValueError("base debe ser 2, 8 o 16")

    cadena = cadena.strip().upper()
    if not cadena:
        raise ValueError("cadena no puede estar vacía")

    simbolos = "0123456789ABCDEF"
    valor = 0
    for caracter in cadena:
        digito = simbolos.find(caracter)
        if digito == -1 or digito >= base:
            raise ValueError(f"dígito inválido '{caracter}' para base {base}")
        valor = valor * base + digito
    return valor


if __name__ == "__main__":
    n = 156
    print(f"{n} en binario: {a_binario(n)}  (verificación: {bin(n)})")
    print(f"{n} en hexadecimal: {a_hexadecimal(n)}  (verificación: {hex(n)})")

    casos = [("11010110", 2), ("326", 8), ("2F", 16)]
    for cadena, base in casos:
        print(f"{cadena} (base {base}) -> decimal: {a_decimal(cadena, base)}")
