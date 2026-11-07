def not_table():
    print("\nA | NOT")
    print("-------")

    for a in [0, 1]:
        print(f"{a} |  {int(not a)}")


def binary_table(op):
    names = {
        "and": "AND",
        "or": "OR",
        "xor": "XOR",
        "nand": "NAND",
        "nor": "NOR",
        "imp": "IMP",
        "rimp": "RIMP",
        "nimp": "NIMP",
        "nrimp": "NRIMP",
        "eq": "EQ"
    }

    print(f"\nA B | {names[op]}")
    print("-" * (len(names[op]) + 7))

    for a in [0, 1]:
        for b in [0, 1]:

            if op == "and":
                result = a and b

            elif op == "or":
                result = a or b

            elif op == "xor":
                result = a != b

            elif op == "nand":
                result = not (a and b)

            elif op == "nor":
                result = not (a or b)

            elif op == "imp":
                result = (not a) or b
                
            elif op == "rimp":
                result = a or (not b)
                
            elif op == "nimp":
                result = a and (not b)  
                
            elif op == "nrimp":
                result = (not a) and b

            elif op == "eq":
                result = a == b

            print(f"{a} {b} |  {int(result)}")

while True:
    print("\nTruth Table Generator")
    print("---------------------")
    print("1. NOT")
    print("2. AND")
    print("3. OR")
    print("4. XOR")
    print("5. NAND")
    print("6. NOR")
    print("7. IMP")
    print("8. RIMP")
    print("9. NIMP")
    print("10. NRIMP")
    print("11. EQ")
    print("12. Exit")

    choice = input("\nChoice: ")

    operations = {
        "2": "and",
        "3": "or",
        "4": "xor",
        "5": "nand",
        "6": "nor",
        "7": "imp",
        "8": "rimp",
        "9": "nimp",
        "10": "nrimp",
        "11": "eq"
    }

    if choice == "12":
        print("Goodbye!")
        break
    elif choice == "1":
        not_table()
    elif choice in operations:
        binary_table(operations[choice])
    else:
        print("Invalid choice")
