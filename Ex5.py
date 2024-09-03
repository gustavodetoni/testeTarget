def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

input_usuario = input("Informe a string a ser invertida: ")

string_invertida = inverter_string(input_usuario)

print(f"String invertida: {string_invertida}")

