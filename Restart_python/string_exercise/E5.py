str1 = "P@#yn26at^&i5ve"
# Chars = 0 
# Digits = 0 
# Symbol=0
# for i in str1:
#     if i.isalpha():
#         Chars+=1
#     elif i.isdigit():
#         Digits+=1
#     elif i:
#         Symbol+=1
# print("chars!!",Chars)
# print("Digits!!",Digits)
# print("Symbol!!",Symbol)

chars=0
digit=0
symbol=0
for i in str1:
    if i.isalpha():
        chars+=1
    elif i.isdigit():
        digit+=1
    elif i:
        symbol+=1
print(chars)
print(digit)
print(symbol)
        