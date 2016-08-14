from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def isInHand(word, hand):
    """
    Assumes that the word is in the wordList;
    Returns True if word is is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    """
    alpha = VOWELS+CONSONANTS
    handcopy = hand.copy()
    if len(word) < 1:
        return False
    for letter in word:
        if letter not in alpha:
            return False
        elif letter not in hand:
            return False
        else:
            handcopy[letter] -= 1
    for letter in handcopy:
        if handcopy[letter] < 0:
            return False
    return True


def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    maxWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isInHand(word,hand):
            # Find out how much making that word is worth
            thisScore = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if thisScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = thisScore
                maxWord = word
    # return the best word you found.
    return maxWord

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    handscore = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print "Current hand:",
        displayHand(hand)
        chosenWord = compChooseWord(hand, wordList, n)
        if chosenWord == None:
            break
        else:
            wordscore = getWordScore(chosenWord,n)
            handscore += wordscore
            print '"'+chosenWord+'" earned '+str(wordscore)+' points. Total: '+str(handscore)+' points'
            print
            # Update the hand 
            hand = updateHand(hand, chosenWord)
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if calculateHandlen(hand) > 0:
        print 'Goodbye! Total score: '+str(handscore)+' points'
    elif calculateHandlen(hand) == 0:
        print 'Ran out of letters. Total score: '+str(handscore)+' points'
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    uberHand = 0
    while True:
        msg = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
        if msg == 'n':
            uberHand = dealHand(HAND_SIZE)
            player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
            if player == 'u':
                playHand(uberHand, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(uberHand, wordList, HAND_SIZE)
            else:
                print "Invalid choice. (I don't understand %r!)" % msg
        elif msg == 'r' and uberHand == 0:
            print 'You have not played a hand yet. Please play a new hand first!'
        elif msg == 'r' and uberHand != 0:
            player = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
            if player == 'u':
                playHand(uberHand, wordList, HAND_SIZE)
            elif player == 'c':
                compPlayHand(uberHand, wordList, HAND_SIZE)
            else:
                print "Invalid choice. (I don't understand %r!)" % msg
        elif msg == 'e':
            break
        else:
            print "Invalid command. (I don't understand %r!)" % msg
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


