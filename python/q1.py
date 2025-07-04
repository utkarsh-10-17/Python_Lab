def is_palindrome(lst):
    n = len(lst)
    for i in range(n // 2):
        if lst[i] != lst[n - i - 1]:
            return False
    return True

def list_input():
    list1 = []
    list2 = []
    x = 'n'
    count1 = 0
    count2 = 0

    while x == 'n':
        n1 = int(input("Enter the values for list1: "))
        list1.append(n1)
        n2 = int(input("Enter the values for list2: "))
        list2.append(n2)
        x = input("Do you want to stop entering? Press any button except 'n' to stop: ")
        
    print("Elements of list 1:")
    for i in list1:
        print(i)
        count1 += 1
    print(f"Number of elements in list1: {count1}")

    print("Elements of list 2:")
    for i in list2:
        print(i)
        count2 += 1
    print(f"Number of elements in list2: {count2}")

    if is_palindrome(list1):
        print("List 1 is a palindrome.")
    else:
        print("List 1 is not a palindrome.")

    if is_palindrome(list2):
        print("List 2 is a palindrome.")
    else:
        print("List 2 is not a palindrome.")

list_input()
