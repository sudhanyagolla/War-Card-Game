##
# cardWarGame - Create a simulation of 2 players playing Card war 
#
# @author SudhanyaGolla
# @course ICS3UC
# @date 2024/04/21 - LastModified
##

import random

# Gather overall deck
# Randomly generate decks for each player to play at hand
def randomizePlayerDeck(numDeck):
    originalDeck = ["AH", "2H", "3H", "4H",
             "5H", "6H", "7H", "8H", "9H", "TH", "JH", "QH", "KH",
             "AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "TS",
             "JS", "QS", "KS",
             "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "TC",
             "JC", "QC", "KC",
             "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "TD",
             "JD", "QD", "KD"]
    originalDeck = originalDeck * numDeck
    numPlayerDeck = len(originalDeck)
    firstPlayerDeck = []

    # Make sure each person has an equal amount of cards (only half of deck)
    while len(originalDeck) > numPlayerDeck / 2:
        card = random.choice(originalDeck)
        indexCard = originalDeck.index(card)
        originalDeck.pop(indexCard)
        firstPlayerDeck.append(card)
    
    secondPlayerDeck = originalDeck

    return [firstPlayerDeck, secondPlayerDeck]

# Give back value of cards placed down and their respective suits
def getCardValue(placedCardsSet):
    valueCardsSet = []
    valueSuitsSet = []

    # Gather value for each respective card placed down
    for card in range(len(placedCardsSet)):
        valueCard = 0
        valueCardSuit = 0

        # Determine value of card
        if placedCardsSet[card].find("A") != -1:
            valueCard += 14
        elif placedCardsSet[card].find("K") != -1:
            valueCard += 13
        elif placedCardsSet[card].find("Q") != -1:
            valueCard += 12
        elif placedCardsSet[card].find("J") != -1:
            valueCard += 11
        elif placedCardsSet[card].find("T") != -1:
            valueCard += 10
        else:
            findIndex = placedCardsSet[card]
            valueCard += int(findIndex[0])
        
        # Determine value of suit for card
        if placedCardsSet[card].find("C") != -1:
            valueCard += 0
            valueCardSuit += 0
        elif placedCardsSet[card].find("D") != -1:
            valueCard += 2
            valueCardSuit += 2
        elif placedCardsSet[card].find("S") != -1:
            valueCard += 4
            valueCardSuit += 4
        else:
            valueCard += 6
            valueCardSuit += 6

        valueCardsSet.append(valueCard)
        valueSuitsSet.append(valueCardSuit)
        
    return [valueCardsSet, valueSuitsSet]

# Determine which card is of higher value
# Store winning cards in winning player's pile
def compareCards(valueList):
    valueSuit = valueList[1]
    valueCard = valueList[0]

    # check if first card wins over second card
    if valueCard[0] > valueCard[1]:
        pile1.append(cardPlaced1)
        pile1.append(cardPlaced2)
    elif valueCard[0] == valueCard[1]:

        # If both have the same values, check suit of cards
        if valueSuit[0] > valueSuit[1]:
            pile1.append(cardPlaced1)
            pile1.append(cardPlaced2)
        elif valueSuit[0] < valueSuit[1]:
            pile2.append(cardPlaced1)
            pile2.append(cardPlaced2)
        else:
            pile1.append(cardPlaced1)
            pile2.append(cardPlaced2)
    
    else:
        pile2.append(cardPlaced1)
        pile2.append(cardPlaced2)

    return [pile1, pile2]

# Reset player 1's hand if there are no cards left
def resetHandPlayerOne(pile1):

    # Shuffle pile and set it as hand
    # Reset pile as having no cards
    while pile1 != []:
        cardAtHand1 = random.choice(pile1)
        indexHand = pile1.index(cardAtHand1)
        pile1.pop(indexHand)
        cardSet1.append(cardAtHand1)

    return [cardSet1, pile1]

# Reset player 2's hand if there are no cards left
def resetHandPlayerTwo(pile2):

    # Shuffle pile and set it as hand
    # Reset pile as having no cards
    while pile2 != []:
        cardAtHand2 = random.choice(pile2)
        indexHand = pile2.index(cardAtHand2)
        pile2.pop(indexHand)
        cardSet2.append(cardAtHand2)
    
    return [cardSet2, pile2]

## MAIN
# Output that simulation is ready to play
# Randomize and generate player decks
playGame = True
pile1 = []
pile2 = []
numOfRounds = 0
validDeck = False
print("Welcome to the Card War game! Here, we play a ", end="")
print("simulation with a deck of cards.")

# Make sure number of decks is eventually valid
while validDeck == False:
    
    # Get number of decks
    # Validate user input
    try:
        numDeck = int(input("Enter number of decks: "))
        
        # Validate input if number of decks is not proper
        if numDeck >=1 and numDeck <= 5:
            validDeck = True
        else:
            print("Enter a valid deck number (in between 1 and 5 decks)")
        
    except ValueError:
        print("Invalid input")

playerDecks = randomizePlayerDeck(numDeck)
cardSet1 = playerDecks[0]
cardSet2 = playerDecks[1]

# Play game while both players have cards in hand
while playGame == True:

    # Check if player 1 has no cards in hand
    if cardSet1 == []:

        # Check if player 1 has cards in pile or not
        # Game ends if there are no cards in pile, reset hand if there are
        if pile1 == []:
            playGame = False
        else:
            cardSet1 = resetHandPlayerOne(pile1)
            cardSet1 = cardSet1[0]
        
    # Check if player 2 has no cards in hand
    if cardSet2 == []:
        
        # Check if player 2 has cards in pile or not
        # Game ends if there are no cards in pile, reset hand if there are
        if pile2 == []:
            playGame = False
        else:
            cardSet2 = resetHandPlayerTwo(pile2)
            cardSet2 = cardSet2[0]

    # Allow players to place cards from hand as long as they have cards
    # Print out cards for each player every single round
    while cardSet1 and cardSet2:
        cardPlaced1 = cardSet1[0]    
        cardPlaced2 = cardSet2[0]    
        placedCardsSet = [cardPlaced1 , cardPlaced2]
        print(placedCardsSet[0], placedCardsSet[1])
        cardSet1.pop(0)
        cardSet2.pop(0)
        #print(cardPlaced1, cardPlaced2)
        valueList = getCardValue(placedCardsSet)
        cardPiles = compareCards(valueList)
        numOfRounds += 1

# Check to see which player wins
# Output winner of game and number of rounds played
if pile1 == []:
    print(f"Player 2 won. Number of rounds played: {numOfRounds}")
else:
    print(f"Player 1 won. Number of rounds played: {numOfRounds}")