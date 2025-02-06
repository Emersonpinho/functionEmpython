def somar(a, b):
    """retorna a soma de dois numeros"""
    return a + b

'''print(somar(10, 10))'''

# se você não quiser parametros, basta deixar os parenteses vazios

def multiplicar():
    return 20 * 2

print(multiplicar()) # erro, pois a função não tem parametros. você não pode inserir dados no print se não tiver parametros

# você pode definir valores padrões para os parametros
def dividir(a=2, b=2):
    return a / b

print(dividir())
print(dividir(10, 2)) 