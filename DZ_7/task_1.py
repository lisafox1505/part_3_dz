def int_into_str(nums_list: list[int]) -> list[str]:
    new_list = list(map(str, nums_list))
    return new_list

if __name__ == '__main__':
    print(int_into_str([1, 2, 3]))

