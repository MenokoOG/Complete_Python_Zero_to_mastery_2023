"""I/O lesson, Menoko OG, 11-2023,"""
# this file is put on desktop, otherwise would have to put full path to file if not in same area , folder, etc...
my_file = open("test.txt")

# print(my_file.read())
# my_file.seek(0) # this is so can display the under print commands in terminal, otherwise would only print once, this is due to cursor detection
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
print(my_file.readlines()) # returns a list of file content

my_file.close() # always good practice to close file after you are done wiht it so it can be used somewhere else and it is not locked.