"""
Description:
In this kata we want to convert a string into an integer. The strings simply
represent the numbers in words.

Examples:

    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
"""
first_ten = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
             'eight', 'nine']
first_ten = dict(zip(first_ten, range(10)))
second_ten = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
second_ten = dict(zip(second_ten, range(10, 20)))
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
        'ninety']
tens = dict(zip(tens, range(20, 100, 10)))
hundreds = 'hundred'
thousands = 'thousand'
million = 'million'


def parse_tens(word):
    words = word.split('-')
    if len(words) == 1:
        if word in first_ten.keys():
            return first_ten[word]
        elif word in second_ten:
            return second_ten[word]
        elif word in tens:
            return tens[word]
        return 0
    else:
        try:
            return tens[words[0]] + first_ten[words[1]]
        except:
            return 0


def parse_hundreds(interval):
    sum = 0
    if hundreds in interval:
        if interval[0] == hundreds:
            sum = 100
        else:
            sum = parse_tens(interval[0]) * 100
        if len(interval) > 2:
            sum += parse_tens(interval[2])
    else:
        sum += parse_tens(interval[0])
    return sum


def parse_int(string):
    if not string:
        return 0
    string = string.replace(" and ", " ")
    word_nums = string.split()
    sum = 0
    intervals = [0] * 3
    # print(string)
    if million in word_nums:
        intervals[0] = word_nums.index(million)
        sum += parse_hundreds(word_nums[:intervals[0]]) * 10 ** 6
        intervals[0] += 1
    if thousands in word_nums[intervals[0]:]:
        intervals[1] = word_nums.index(thousands)
        sum += parse_hundreds(word_nums[intervals[0]:intervals[1]]) * 10 ** 3
        intervals[1] += 1
    if intervals[1] < len(word_nums) and intervals[0] < len(word_nums):
        intervals[2] = len(word_nums)
        sum += parse_hundreds(word_nums[intervals[1]:intervals[2]])
    return sum


if __name__ == "__main__":
    print(parse_int("one million"))
