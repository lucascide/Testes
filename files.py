# File1 = open("./.txt", "r")

# print(File1.read())
# print(File1.name)

# File1.close()

# # Uma forma alternativa de abrir e fechar é usando with

# with open("./.txt", "r") as File2:
#     file_content = File2.read()
#     print(file_content)

# print(File2.closed)


# with open("./.txt", "r") as File3:
#     file_content3 = File3.readlines()
#     print(file_content3)

# with open("./.txt", "r") as File4:
#     file_content4 = File4.readline()
#     print(file_content4)

# with open("./.txt", "r") as File5:
#     for line in File5:
#         print(line)


### Para escrever em arquivos

# with open(".txt", "w") as f:
#     f.write("Escrevido")


# Para copiar de um arquivo para outro:

# with open("./reafile.txt", "r") as readfile:
#     with open("./writefile.txt", "w") as writefile:
#         for line in readfile:
#             writefile.write(line)


# Para ambos

# with open("./writefile.txt", "a+") as writefile:
#     writefile.write("oi familll")
#     writefile.seek(
#         0, 0
#     )  # Qtd de bytes pulado a partir do inicio 0, posicao atual 1, ou fim 2
#     print(writefile.read())
