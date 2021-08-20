import random
import sys

game = 0
storesecret = None

HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def randomword(wordlist):
    idx = random.randint(0, len(wordlist) - 1)
    print(wordlist[idx])
    global game
    game = 1
    return wordlist[idx]

def getunderlinedword(word):
    secretword = '_'*len(word)
    print("The word is", secretword)
    return secretword

def allinstances(word, uin, secret):
    string = word
    char = uin
    lst = []
    for i in range(len(string)):
        if (string[i] == char):
            lst.append(i)
    print(lst)
    return lst

def getuserinput():
    uin = input("Input the letter a-z to guess")
    return uin


def guesscheck(word, uin, secret):
    x = word.find(uin)
    lst = allinstances(word,uin,secret)
    print(x)
    global storesecret
    if x == -1:
        print("Word not found try again")
    else:
        print(f'{uin} was found in the word')
        temp = list(secret)
        if storesecret != None:
            temp2 = list(storesecret)
            for idx in lst:
                temp2[idx-1] = uin
            storesecret = ''.join(temp2)
        else:
            for idx in lst:
                temp[idx-1] = uin
            storesecret = ''.join(temp)
        print(storesecret)
        return storesecret


def main():
    global game
    if game == 0:
        word2 = randomword(words)
        secret = getunderlinedword(word2)
        global w, s
        w, s = word2, secret
        #hhhhhhit



    uin2 = getuserinput()
    temp = guesscheck(w, uin2, s)
    if temp == w:
        x = input("You won play again y or n?")
        if x == 'y':
            game = 0
            main()
        else:
            sys.exit()



    main()


main()