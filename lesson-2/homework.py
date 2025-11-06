#     НОМЕРА С 1 ПО 3
a = "The quick brown fox jumps over the lazy dog"
for word in a.split(" "):
    print(word)

    # НОМЕРА С 4 ПО 8
# list = [i for i in range(3,43)]
# print(list)
# list_squares = [i ** 2 for i in list]
# print(list_squares)
# dict = {
#     i: str(i)*3
#     for i in list_squares
# }
# print(dict)

#     НОМЕР 9
# def spisok(*num):
#     chisla = []
#     def prostie(n):
#         if n <= 1:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     for i in range(len(num)):
#         if prostie(num[i]) == True:
#             chisla.append(num[i])   
#     return chisla

#     НОМЕР 10
# def simvoli(str):
#     bukvi = []
#     for char in str:
#         if char not in bukvi:
#             bukvi.append(char)
#     return bukvi



    