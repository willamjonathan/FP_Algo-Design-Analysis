# FUNCTION TO CHECK WHETHER THE ARRAY IS SORTED OR NOT
def arraySortedOrNot(x):
    # Calculating length
    n = len(x)
 
    # Array has one or no element or the
    # rest are already checked and approved.
    if n == 1 or n == 0:
        return True
 
    # Recursion applied till last element
    return x[0] <= x[1] and arraySortedOrNot(x[1:])
def searchStorage(x):
    if arraySortedOrNot(x):
        items = input("Please enter the item name to search for the storage (String): ")
        for i in range(len(x)):
            if(x[i]==items):
                if(i<=43):
                    A = ('A',[x[i]])
                    print("In Storage A")
                    break
                elif(43<i<=86):
                    B = ('B',[x[i]])
                    print("In Storage B")
                    break
                elif(86<i<=129):
                    C = ('C',[x[i]])
                    print("In Storage C")
                    break
                else:
                    print("The items you are looking for does not exist in our csv file")
                    break
    else:
        print("Sorry, the items are not sorted! Please sort it first!")
        