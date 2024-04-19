def squares_generator(n):
    for i in range(n):
        yield i ** 2


squares_gen = squares_generator(5)


print("Using a for loop:")
for square in squares_gen:
    print(square)


print("\nManually using next():")
squares_gen = squares_generator(5)
print(next(squares_gen))  
print(next(squares_gen))  
print(next(squares_gen))  
print(next(squares_gen))