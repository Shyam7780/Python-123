#check input is Alphabet or not
char = input("Enter a character: ")
if ((char>'a' and char<'z') and (char>'A' and char<'Z')):
    print(char,"is an alphabet.")
else:
    print(char,"is not an alphabet.")