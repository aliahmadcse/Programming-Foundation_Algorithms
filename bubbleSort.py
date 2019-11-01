
# bubble sort implementation

def bubble_sort(dataset):
    for i in range(len(dataset)-1,0,-1):
        for j in range(i):
            if dataset[j] > dataset[j+1]:
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp


def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    bubble_sort(list1)
    print(list1)


if __name__ == "__main__":
    main()
