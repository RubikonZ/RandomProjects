def main():
    noun = input('Input noun: ')
    adj = input('Input adjective: ')
    verb = input('Input verb: ')
    noun2 = input('Input second noun: ')
    word_list = []
    word_list.append(input('Dobavit slovo v spisok: '))

    print(f'Vsem privet ya {noun.lower().strip()},\nya ochen {adj.lower()},\nmne tak hotelos bi {verb.lower()},\nno ya skoree poluchu {noun2.lower()}. :(')
    print(word_list)

if __name__=='__main__':
    main()