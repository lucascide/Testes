# Docs: https://docs.python.org/3/library/exceptions.html

a = 1

# b = int(input("Insira um numero que dividirá a: "))
# a = a / b

# Except genérico

# try:
#     b = int(input("Insira um numero que dividirá a: "))
#     a = a / b
# except:
#     print("Houve algum erro")

# Except específico

# try:
#     b = int(input("Insira um numero que dividirá a: "))
#     a = a / b
# except ValueError:
#     print("O que foi inserido não é um numero")
# except ZeroDivisionError:
#     print("Não é possível dividir por zero")
# except:
#     print("Ocorreu outro erro")

# print("O valor de a ficou igual a = " + str(a))


# Try except else  (Else é executado caso não haja exceção)

try:
    b = int(input("Insira um numero que dividirá a: "))
    a = a / b
except ValueError:
    print("O que foi inserido não é um numero")
except ZeroDivisionError:
    print("Não é possível dividir por zero")
except:
    print("Ocorreu outro erro")
else:
    print("O valor de a ficou igual a = " + str(a))
finally:
    print("Processamento completo")
