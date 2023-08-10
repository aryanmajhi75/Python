import time

def makeCodewords():
    print("------------------------------------------")
    print("| *Input word should be within 5 letters |")
    print("------------------------------------------")
    code=input("\nENter YoUr CODE WorD :")
    if(len(code)>5):
        print("------------------------------------------")
        print("| *Input word SHOULD BE within 5 letters |")
        print("------------------------------------------")
        menu()
    else:
        convertedCode=""
        Padding=["0","0","0","0","0","0","0","0"]
        # print(Padding)
        for i in range(len(code)):
            # print("i : ",i)
            OrdValue=ord(code[i])
            Binary=bin(OrdValue)
            Binary=str(Binary[2:])
            Padding[i]="1"
            Padding="".join(Padding)
            # print(Padding)
            convertedCode=convertedCode+Padding
            convertedCode=convertedCode+Binary
            # print(convertedCode)
            Padding=["0","0","0","0","0","0","0","0"]
    print(f"\nConverted Code Word for {code} : {convertedCode}\n")
    print("------------------------------------")
    print("| Ask Your Friends to Try it Now ! |")
    print("------------------------------------")

def menu():
    while True:
        print("\nMenu:")
        print("1. Make Codewords")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == "1":
            makeCodewords()
        elif choice == "2":
            time.sleep(1)
            print("Thank You..")
            for i in range(0,2):
              time.sleep(1)
              print("Bye")
            break
        else:
            print("Invalid choice! Please select a valid option i.e. -> (1/2).")



if __name__ == '__main__':
    menu()