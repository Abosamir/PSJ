def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:

    p1 = 0
    p2 = k-1
    summ = sum(arr[p1:k])
    num_of_sublists = 0

    while p2 != len(arr):

        if p1 != 0:
            summ= summ -arr[p1-1] + arr[p2]
            avg = summ/k
        else:
            avg = summ/k
        

        if avg >= threshold:
            num_of_sublists += 1

        p2 += 1
        p1 += 1
        
    return num_of_sublists


print(numOfSubarrays("f",[11,13,17,23,29,31,7,5,2,3], k = 3, threshold= 5))