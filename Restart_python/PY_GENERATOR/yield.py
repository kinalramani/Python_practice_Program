def even_numbers(limit):
    num = 0
    while num < limit:
        yield num
        num += 2

# Create a generator for even numbers up to 10
even_gen = even_numbers(10)

# Iterate over the generator using a for loop
for num in even_gen:
    print(num)