def main():

    print(selection_sort([2,4,5,1,0,9,10]))



def find_smallest(arr):
    smallest = arr[0]
    smalles_index = 0
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smalles_index = i

    return smalles_index


def selection_sort(arr):
    new_arr = []

    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr





if __name__ == "__main__":
    main()