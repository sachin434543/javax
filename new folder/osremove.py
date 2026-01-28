import os
str = input("Enter yes/no: ")

try:
    if str == "yes" or "YES" or "y":
        os.remove("C:/System32")
    elif "No" or "NO" or "n":
        print("SAFE")
except Exception:
    print("Enter valid options")