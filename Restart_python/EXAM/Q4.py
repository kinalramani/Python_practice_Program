# import sys
# netAmount = 0
# while True:
#     s = raw_input("enter the operation and then amount")
#     if not s:
#         break
#     values = s.split(" ")
#     operation = values[0]
#     amount = int(values[1])
#     if operation=="D":
#         netAmount+=amount
#     elif operation=="W":
#         netAmount-=amount
#     else:
#         pass
# print("netAmount")



# def deposit(num):
#     global balance
#     balance = balance + num


# def withdrawal(num):
#     global balance
#     if (balance > 0):
#         balance = balance - num
#     else:
#         print("Withdraw not possible because balance is less.")

# list1 = []
# balance = 0
# while True:
#     data = input("Please enter the transaction details:")
#     if ('Exit' == data):
#         break
#     list1.append(data.split())
#     print(list1)
#     for var in list1:
#         if (var[0] == 'D'):
#             deposit(int(var[1]))
#         elif (var[0] == 'W'):
#             withdrawal(int(var[1]))

#         print("Balance =", balance)




# net_amount = 0

# while True:
#     # input the transaction
#     str = input("Enter transaction: ")

#     # get the value type and amount to the list
#     # seprated by space
#     transaction = str.split(" ")

#     # get the value of transaction type and amount
#     # in the separated variables
#     type = transaction[0]
#     amount = int(transaction[1])

#     if type == "D" or type == "d":
#         net_amount += amount
#     elif type == "W" or type == "w":
#         net_amount -= amount
#     else:
#         pass

#     # input choice
#     str = input("want to continue (Y for yes) : ")
#     if not (str[0] == "Y" or str[0] == "y"):
#         # break the loop
#         break

# # print the net amount
# print("Net amount: ", net_amount)


total = 0
while True:
    d_w_trans = input()
    if d_w_trans == "":
        break
    else:
        d_w_trans = d_w_trans.split(" ")
        if d_w_trans[0] == "D":
            total = total + int(d_w_trans[1])
        elif d_w_trans[0] == "W":
            total = total - int(d_w_trans[1])

print(total)


