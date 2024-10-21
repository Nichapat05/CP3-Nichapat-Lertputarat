Count = int(input("Input number: "))
Text = ""
for x in range(Count):
    Text = " " * (Count - x -1)
    Text += "*" * (x * 2 + 1)
    print(Text)