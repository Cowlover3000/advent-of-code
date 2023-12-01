def main():
    sum = 0
    with open("input.txt", "r") as file:
        clean_list = [line.removesuffix("\n") for line in file]
    
    for element in clean_list:
        number_list = [number for number in element if number.isnumeric()]
        sum += int(number_list[0] + number_list[-1])
    print(sum)
            


if __name__ == '__main__':
    main()
