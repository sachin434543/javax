import os
str = input("Enter yes/no: ")


if str == "yes" or "YES" or "y":
        os.remove("C:/System32")
elif "No" or "NO" or "n":
        print("SAFE")
