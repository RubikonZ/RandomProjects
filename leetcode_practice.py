# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
def remove_duplicates_from_array(num_array):
    # nums = list(set(num_array))
    # print(num_array)
    i = 0
    while i < len(num_array) - 1:
        n = num_array[i]
        if n == num_array[i+1]:
            num_array.remove(num_array[i+1])
        else:
            i += 1
    print(num_array)

# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/564/
def best_time_to_buy_and_sell_stock(prices):
    # Checking with previous item instead of next one is MUCH better
    ans = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            ans += prices[i] - prices[i - 1]
        print(ans)
    print(ans)


# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/578/
def contains_duplicate(lst):
    lst.sort()
    for i in range(0, len(lst) - 1):
        if lst[i] == lst[i+1]:
            return True
    return False

# https://youtu.be/GWIqs8LNLZY?t=876
def find_number_wo_pair(arr):
    a = {}
    bSet = set()

    for nmbr in arr:
        if nmbr not in bSet:
            bSet.add(nmbr)
        else:
            bSet.remove(nmbr)

    for nmbr in arr:
        a[nmbr] = a.get(nmbr, 0) + 1

    return a, bSet.pop()
    # print(list(bSet)[0]) # How to show result of set


# https://twitter.com/Al_Grigor/status/1357028887209902088
def input_to_output(strng):
    a = list()
    counter = 0
    last_n = strng[:1]
    for n in strng:
        if n == last_n:
            counter += 1
        else:
            a.append((last_n, counter))
            counter = 1
            last_n = n
    if counter > 0:
        a.append((last_n, counter))
    print(a)


def skobki_generator(both, opn, clsed, n):
    if len(both) == 2*n:
        # print(both)
        return
    if opn < n:
        skobki_generator(both+'(', opn+1, clsed, n)
    if clsed < opn:
        skobki_generator(both+')', opn, clsed+1, n)
    print(both)

def coursera_twitter_assignment():
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

    # lists of words to use

    def strip_punctuation(wrd):
        for char in punctuation_chars:
            wrd = wrd.replace(char, '')
        return wrd

    def get_neg_pos(st_sentence):
        count_negative = 0
        positive_count = 0
        for word in st_sentence.split():
            word.lower()
            if strip_punctuation(word) in negative_words:
                count_negative += 1
            elif strip_punctuation(word) in positive_words:
                positive_count += 1
        return count_negative, positive_count

    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())

    negative_words = []
    with open("negative_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())

    with open('project_twitter_data.csv', 'r') as f:
        post_ls = []
        for line in f.readlines()[1:]:
            tweet, retweets, replies = line.strip().split(',')
            negative_score, positive_score = get_neg_pos(tweet)
            post_ls.append(
                (int(retweets), int(replies), positive_score, negative_score, positive_score - negative_score))

    print(post_ls)
    with open('resulting_data.csv', 'w') as f:
        f.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
        for tweet in post_ls:
            f.write('{},{},{},{},{}'.format(*tweet))
            f.write('\n')


# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/559/
def plus_one(digits: list[int]):
    # digits[-1] += 1
    # if digits[-1] % 10 == 0:
    #     digits[-1] = 0
    #     if len(digits[:-1]) > 0:
    #         # recursive function if we need to change next decimal
    #         digits[:-1] = plus_one(digits[:-1])
    #     else:
    #         # If we need to add new decimal
    #         digits.insert(0, 1)
    # return digits

    if digits[-1] == 9 and len(digits) == 1:
        return [1, 0]

    if digits[-1] != 9:
        digits[-1] += 1
        return digits
    else:
        digits[-1] = 0
        digits[:-1] = plus_one(digits[:-1])
        return digits
if __name__ == '__main__':



    # print(plus_one([0]))
    # print(plus_one([9]))
    # print(plus_one([9, 9]))
    # print(plus_one([4, 3, 2, 1]))
    # print(plus_one([4, 3, 2, 9]))
    # print(plus_one([4, 3, 9, 9]))

    # print(sorted_id)

    # input_to_output("aaaabbbcca")
    # input_to_output("a")

    # print(find_number_wo_pair((5, 4, 5, 3, 1, 4, 1, 8, 6, 8, 6)))
    # skobki_generator('', 0, 0, 1)
    # skobki_generator('', 0, 0, 2)
    # skobki_generator('', 0, 0, 3)

    # print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
    # print(contains_duplicate([1, 2, 3, 1]))
    # print(contains_duplicate([1, 2, 3, 4]))
    # remove_duplicates_from_array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    # remove_duplicates_from_array([1, 1, 2])

    # best_time_to_buy_and_sell_stock([7, 1, 5, 3, 6, 4])
    # best_time_to_buy_and_sell_stock([1, 2, 3, 4, 5])
    # best_time_to_buy_and_sell_stock([7, 6, 4, 3, 1])
    # best_time_to_buy_and_sell_stock([2, 1, 2, 0, 1])
    # best_time_to_buy_and_sell_stock([2,1,2,1,0,1,2])
    # best_time_to_buy_and_sell_stock([3,3,5,0,0,3,1,4])

    # lst.insert()
