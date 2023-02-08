def descending_order(num):
    highest = []

    num = str(num)
    reversed = num[::-1]

    for number in reversed:
        highest.append(number)    
    highest.sort(reverse=True)

    return int(''.join(highest))