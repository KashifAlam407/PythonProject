## Nested loop = A loop within another loop (outer, inner)
#       outer loop:
#           inner loop:


rows = int(input("Enter the No. of rows: "))
columns = int(input("Enter the No. of columns: "))
symbol = input("Enter the symbol to use: ")

for x in range(rows):
    for y in range(1, columns):
        print(symbol, end="*")  ## in python end parameter is used to what character or string should printed at the end of the output, instead of the default newline character (\n). 
    print()    ## use for next line