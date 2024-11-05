from calculadora import soma

# print(soma(2, 3))
# print(soma(4.3, 3.1))
# print(soma(1, 3))

try:
    print(soma(1, "10"))
except AssertionError as e:
    print(f'conta inválida: {e}')
