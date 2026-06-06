# A generator in Python is a special type of iterable
# that allows you to iterate over a sequence of values lazily,
# meaning it generates values one at a time as needed, instead of
# storing them in memory all at once. This makes generators memory efficient
# and suitable for handling large datasets or infinite sequences.

def my_generator():
    for i in range(5):
        yield i
gen=my_generator()
print(next(gen))
print(next(gen))
print(gen)

# def read_large_file(file_path):
#     with open(file_path, "r") as file:
#         for line in file:
#             yield line.strip()
#
# for line in read_large_file("bigdata.txt"):
#     print(line)  # Processes one line at a time
