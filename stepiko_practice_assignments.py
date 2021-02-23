# n = int(input())

def two_two_seven(inp_number):
    n = inp_number
    a = 0
    b = 1
    i = 0

    while True:
        if n == a:
            print(i)
            return False
        elif n < a:
            print('no')
            return False
        a, b = b, a + b
        i += 1


def two_two_fifteen():
    flist = []

    while True:
        n = input()
        if n == '.':
            break
        flist.append(float(n))

    flist.pop(flist.index(max(flist)))
    print(max(flist))

def three_one_five():

    kek = 'qweqwre-qwrqtq'
    print(kek[1::2])


if __name__ == '__main__':
    three_one_five()