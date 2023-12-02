import re


def main():
    with open("input.txt") as file:
        reader = file.read().splitlines()
    print(reader)
    numbers = [find_left_most_and_right_most(number) for number in reader]
    print(numbers)
    print(sum(numbers))


def find_left_most_and_right_most(word):
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    words_pattern = "|".join(["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"])
    numbers_pattern = "|".join(["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    left_most_word = re.search(words_pattern, word)
    left_most_number = re.search(numbers_pattern, word)

    right_most_word = re.search(words_pattern[::-1], word[::-1])
    right_most_number = re.search(numbers_pattern, word[::-1])

    left_word = (left_most_word.group() if left_most_word else "-1")
    left_number = (left_most_number.group() if left_most_number else "-1")
    right_word = (right_most_word.group()[::-1] if right_most_word else "-1")
    right_number = (right_most_number.group() if right_most_number else "-1")

    if left_word == -1 and left_number == -1 and right_word == -1 and right_number == -1:
        return

    if word.find(left_word) < word.find(left_number) and word.find(left_word) != -1:
        left_most_number = numbers[words.index(left_word)]
    else:
        left_most_number = numbers[numbers.index(left_number)]

    if word[::-1].find(right_word[::-1]) < word[::-1].find(right_number) and word.find(left_word) != -1:
        right_most_number = numbers[words.index(right_word)]
    else:
        right_most_number = numbers[numbers.index(right_number)]

    return int(left_most_number + right_most_number)


if __name__ == '__main__':
    main()
