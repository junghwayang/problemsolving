def bonAppetit(bill, k, b):
    anna = (sum(bill) - bill[k]) // 2 
    print("Bon Appetit" if anna == b else b - anna)