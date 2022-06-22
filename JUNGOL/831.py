while True:
    width = int(input("Width = "))
    height = int(input("Height = "))
    print(f"Triangle Area = {round(0.5 * width * height, 1)}")
    Continue = input("Continue? ")
    if Continue != "Y" and Continue != "y":
        break