#(1) object:- The value to be printed. You can pass multiple objects separated by commas.

x = "Kashif Alam"
print(x)
print(x, x)
print(x, 4)
print(x, "Khan")
print("Md", x)



#(2) sep:- The string inserted between the values, defaulting to a spance (' ').

print("Hello", "World")
print("Hello", "World", sep=" ")
print("Hello", "World", sep="")
print("Hello", "World", sep="-")



#(3) end:- The string appended after the last value, defaulting to newline ('\n')

print("Hello", "World", end="!")
print() # to create a new line or you can use \n in above end parameter
print("Hello", "World", sep="", end="!")



#(4) file:- An object with a write(string) method; the default is sys.stdout (standard output). Type: File-like object.

with open("output.txt", "w") as f:
    print("hello kashif how are you", file=f)


#(5) flush:- A boolean that controls whether the output is flushed (i.e., forcibly written) after printing. The default is False. Type: Boolean.

print("Hello", "World", sep=", ", end="!\n", flush=True)


import time

print("Starting...", flush=True)
time.sleep(2)  # Simulate a long process
print("Finished!", flush=True)
