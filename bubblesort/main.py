from pandas import *
import time

def bubble_sorting(numbers):
    n = len(numbers)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
if __name__ == '__main__':
    start_time = time.time()
    data = read_csv("Vehicles2.csv")

    retail = data['Retail'].tolist()
    dealer_price = data['Dealer'].tolist()
    weight = data['Weight'].tolist()

    bubble_sorting(retail)
    bubble_sorting(dealer_price)
    bubble_sorting(weight)

    print("retail: ")
    for i in retail:
        print(str(i), end=' ')
    print()

    print("weight: ")
    for i in weight:
        print(str(i), end=' ')
    print()

    print("dealer price: ")
    for i in dealer_price:
        print(str(i), end=' ')
    print()

    print("--- %s seconds ---" % (time.time() - start_time))


