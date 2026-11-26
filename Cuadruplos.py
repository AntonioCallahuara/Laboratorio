def infijo_a_postfijo(expresion):
    # Definición de precedencias (a mayor valor, mayor prioridad)
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    asociatividad_derecha = {'^'} # Se usa un set para búsquedas rápidas

    pila = []      # Almacena operadores y paréntesis
    salida = []    # Resultado en notación postfija

    # Remover espacios en blanco para procesar caracteres limpios
    tokens = expresion.replace(" ", "")

    for token in tokens:
        # Caso 1: El token es un operando (Letra o Número)
        if token.isalnum():
            salida.append(token)

        # Caso 2: Paréntesis de apertura
        elif token == '(':
            pila.append(token)

        # Caso 3: Paréntesis de cierre
        elif token == ')':
            while pila and pila[-1] != '(':
                salida.append(pila.pop())
            if pila and pila[-1] == '(':
                pila.pop() # Eliminar el '(' residual

        # Caso 4: El token es un operador
        elif token in precedencia:
            # CORRECCIÓN AQUÍ: Condición completa del while
            while (pila and pila[-1] != '(' and 
                  (precedencia[pila[-1]] > precedencia[token] or 
                   (precedencia[pila[-1]] == precedencia[token] and token not in asociatividad_derecha))):
                salida.append(pila.pop())
            pila.append(token)

    # Vaciar los elementos restantes de la pila
    while pila:
        salida.append(pila.pop())

    return " ".join(salida)

# Pruebas de ejecución
if __name__ == "__main__":
    ejemplo = "A + B * C ^ D - E"
    resultado = infijo_a_postfijo(ejemplo)
    print(f"Infijo: {ejemplo} -> Postfijo: {resultado}")
