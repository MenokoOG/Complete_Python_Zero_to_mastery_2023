""" Modules lesson, L. Jefferson, Menoko OG, 11/2023"""
# import utility #would have to use dot notation for calls to methods.
from utility import *  # this imports all methods for direct call.
# import shopping.more_shopping.shopping_cart #very long way to import
from shopping.more_shopping import shopping_cart  # importing module from the packages.

if __name__ == "__main__":  # this is good for checking this is the file to run and not a file for just importing.
    # print(type(utility))
    # print(utility.multiply(2,3))
    # print(utility.greet())


    # print(utility.add(4,5))
    # print(utility.subtract(100,93))
    print(divide(10, 2))
    print(greet())
    print(multiply(2, 10))
    # print(shopping.more_shopping.shopping_cart.buy("apple")) #very long to call function now
    print(shopping_cart.buy("Orange"))  # now with from import can just call the buy function

    print("Please run this")
