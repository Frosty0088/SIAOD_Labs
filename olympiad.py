
def triangle(sides):
    result = 0
    sides_sorted = sorted(sides, reverse=True)
    for i in range(len(sides_sorted) - 2):
        a = sides_sorted[i]
        b = sides_sorted[i+1]
        c = sides_sorted[i+2]
        if a + b > c and a + c > b and b + c > a:
            return a + b + c
    return result

def maximum(nums):
    nums_str = []
    result = ''
    for num in nums:
        nums_str.append(str(num))
    nums_str_sorting = sorted(nums_str, reverse=True)
    for i in range(len(nums_str_sorting) - 1):
        if nums_str_sorting[i]+nums_str_sorting[i+1] < nums_str_sorting[i+1]+nums_str_sorting[i]:
            nums_str_sorting[i], nums_str_sorting[i+1] = nums_str_sorting[i+1], nums_str_sorting[i]
    for num in nums_str_sorting:
        result += num
    return(result)



def main():
    print("Example 1.1: ",triangle([2, 1, 2]))
    print("Example 1.2: ",triangle([1, 2, 1]))
    print("Example 1.3: ",triangle([3, 2, 3, 4]))
    print("Example 1.4: ",triangle([3,6,2,3]))
    print("Example 2.1: ",maximum([10,2]))
    print("Example 2.2: ",maximum([3, 30, 34, 5, 9]))
    print("Example 2.3: ",maximum([1]))
    print("Example 2.4: ",maximum([10]))

if __name__ == "__main__":
    main()