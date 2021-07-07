# Magic the Lambda-ing!

import random

"""
所以才说为什么兴趣牵引是学习最好的导向，这个lab直接实现了一个昆特牌的模式，这太有趣了，从这里面我们应该学到面向对象的一些思路：

1.思考我们首先得先建立卡牌这个类，class Card，用来实例化卡牌，设计卡牌的模式，比如需要有血量和魔法值，那么就需要相应的类中有血量和魔法值的对象属性。

2.其次我们要考虑，有了卡牌这个对象，我们要怎么设计整个游戏，首先是要有卡组，所以要有一个放置卡牌对象的列表，然后要有手牌，所以要有一个放置手牌的列表，如果还有战斗区域，那么战斗区域的卡牌也需要一个列表存放，这样基本上卡组和卡牌的问题就解决了

3.既然是一个游戏，那必然需要玩家，所以玩家应该也是一个类，玩家类当中需要卡组这个对象属性，手牌这个对象属性，以及游戏规则，比如出牌这个方法，抽牌这个方法，以及可能还有弃牌这个方法。

4.游戏可能还有游戏这个主类，所以还得建立Game的主类，Game主类要确定游戏胜利的条件，要确定游戏的流程规范等等

经过这样考虑我们初步有以下框架

class Card():
    def __init__(self,name,attack,defense):
         self.name = name
         self.attack = attack
         self.defense = defensez
    
    def power(self,other):
         return self.attack - other.defense/2


class Player():
    def __init__(self,deck,name):
         self.name = name
         self.deck = deck
         self.hand = 

    def draw():


    def out():


    def drop():
"""


class Card(object):
    cardtype = 'Staff'

    def __init__(self, name, attack, defense):
        """
        Create a Card object with a name, attack,
        and defense.
        >>> staff_member = Card('staff', 400, 300)
        >>> staff_member.name
        'staff'
        >>> staff_member.attack
        400
        >>> staff_member.defense
        300
        >>> other_staff = Card('other', 300, 500)
        >>> other_staff.attack
        300
        >>> other_staff.defense
        500
        """
        self.name = name
        self.attack = attack
        self.defense = defense

    def power(self, other_card):
        """
        Calculate power as:
        (player card's attack) - (opponent card's defense)/2
        where other_card is the opponent's card.
        >>> staff_member = Card('staff', 400, 300)
        >>> other_staff = Card('other', 300, 500)
        >>> staff_member.power(other_staff)
        150.0
        >>> other_staff.power(staff_member)
        150.0
        >>> third_card = Card('third', 200, 400)
        >>> staff_member.power(third_card)
        200.0
        >>> third_card.power(staff_member)
        50.0
        """
        rank = self.attack - other_card.defense/2
        return rank
        


    def effect(self, other_card, player, opponent):
        """
        Cards have no default effect.
        """
        return

    def __repr__(self):
        """
        Returns a string which is a readable version of
        a card, in the form:
        <cardname>: <cardtype>, [<attack>, <defense>]
        """
        return '{}: {}, [{}, {}]'.format(self.name, self.cardtype, self.attack, self.defense)

    def copy(self):
        """
        Returns a copy of this card.
        """
        return Card(self.name, self.attack, self.defense)

class Player(object):
    def __init__(self, deck, name):
        """Initialize a Player object.
        A Player starts the game by drawing 5 cards from their deck. Each turn,
        a Player draws another card from the deck and chooses one to play.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> len(test_deck.cards)
        1
        >>> len(test_player.hand)
        5
        """
        self.deck = deck
        self.name = name
        self.hand = [deck.draw() for _ in range(5)]
        

    def draw(self):
        """Draw a card from the player's deck and add it to their hand.
        >>> test_card = Card('test', 100, 100)
        >>> test_deck = Deck([test_card.copy() for _ in range(6)])
        >>> test_player = Player(test_deck, 'tester')
        >>> test_player.draw()
        >>> len(test_deck.cards)
        0
        >>> len(test_player.hand)
        6
        """
        assert not self.deck.is_empty(), 'Deck is empty!'
        self.hand +=[self.deck.draw()]
        

    def play(self, card_index):
        """Remove and return a card from the player's hand at the given index.
        >>> from cards import *
        >>> test_player = Player(standard_deck, 'tester')
        >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
        >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
        >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
        >>> test_player.play(0) is ta1 
        True
        >>> test_player.play(2) is tutor2 
        True
        >>> len(test_player.hand)
        2
        """
        return self.hand.pop(card_index)


    def display_hand(self):
        """
        Display the player's current hand to the user.
        """
        print('Your hand:')
        for card_index, displayed_card in zip(range(len(self.hand)),[str(card) for card in self.hand]):
            indent = ' '*(5 - len(str(card_index)))
            print(card_index, indent + displayed_card)

    def play_random(self):
        """
        Play a random card from hand.
        """
        return self.play(random.randrange(len(self.hand)))

######################
# Optional Questions #
######################

class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, other_card, player, opponent):
        """
        Discard the first 3 cards in the opponent's hand and have
        them draw the same number of cards from their deck.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 500, 500)
        >>> tutor_test = TutorCard('Tutor', 500, 500)
        >>> initial_deck_length = len(player2.deck.cards)
        >>> tutor_test.effect(other_card, player1, player2)
        p2 discarded and re-drew 3 cards!
        >>> len(player2.hand)
        5
        >>> len(player2.deck.cards) == initial_deck_length - 3
        True
        """
        "*** YOUR CODE HERE ***"
        #Uncomment the line below when you've finished implementing this method!
        print('{} discarded and re-drew 3 cards!'.format(opponent.name))
        for _ in range(3):
            opponent.play(0)
        for _ in range(3):
            opponent.draw()

    def copy(self):
        """
        Create a copy of this card.
        """
        return TutorCard(self.name, self.attack, self.defense)

class TACard(Card):
    cardtype = 'TA'

    def effect(self, other_card, player, opponent):
        """
        Swap the attack and defense of an opponent's card.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> other_card = Card('other', 300, 600)
        >>> ta_test = TACard('TA', 500, 500)
        >>> ta_test.effect(other_card, player1, player2)
        >>> other_card.attack
        600
        >>> other_card.defense
        300
        """
        other_card.attack,other_card.defense = other_card.defense,other_card.attack 

        


    def copy(self):
        """
        Create a copy of this card.
        """
        return TACard(self.name, self.attack, self.defense)

class InstructorCard(Card):
    cardtype = 'Instructor'

    def effect(self, other_card, player, opponent):
        """
        Increase attack/defense of every card in the player's
        deck by 300 each, then adds a copy of the opponent's card
        to both the player's deck and to their hand.
        >>> test_card = Card('card', 300, 300)
        >>> instructor_test = InstructorCard('Instructor', 500, 500)
        >>> opponent_card = test_card.copy()
        >>> test_deck = Deck([test_card.copy() for _ in range(8)])
        >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
        >>> instructor_test.effect(opponent_card, player1, player2)
        p2's card added to p1's hand and deck!
        >>> [(card.attack, card.defense) for card in player1.deck.cards]
        [(600, 600), (600, 600), (600, 600), (300, 300)]
        >>> len(player1.hand)
        6
        >>> opponent_card.attack
        300
        >>> opponent_card.defense
        300
        """
        for card in player.deck.cards:
            card.attack +=300
            card.defense +=300
        opp_cards = other_card.copy()
        player.deck.cards.append(opp_cards)
        player.hand.append(opp_cards)
        #Uncomment the line below when you've finished implementing this method!
        print('{}\'s card added to {}\'s hand and deck!'.format(opponent.name, player.name))

    def copy(self):
        """
        Create a copy of this card.
        """
        return InstructorCard(self.name, self.attack, self.defense)
        
# class ProfessorCard(Card):
#     cardtype = 'Professor'

#     def effect(self, other_card, player, opponent):
#         """
#         Adds the attack and defense of the opponent's card to
#         all cards in the player's deck, then removes all cards
#         in the opponent's deck that share an attack or defense
#         stat with the opponent's card.
#         >>> test_card = Card('card', 300, 300)
#         >>> professor_test = ProfessorCard('Professor', 500, 500)
#         >>> opponent_card = test_card.copy()
#         >>> test_deck = Deck([test_card.copy() for _ in range(8)])
#         >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
#         >>> professor_test.effect(opponent_card, player1, player2)
#         3 cards were discarded from p2's deck!
#         >>> [(card.attack, card.defense) for card in player1.deck.cards]
#         [(600, 600), (600, 600), (600, 600)]
#         >>> len(player2.deck.cards)
#         0
#         """
#         orig_opponent_deck_length = len(opponent.deck.cards)
#         # BEGIN SOLUTION
#         for card in player.deck.cards:
#             card.attack += other_card.attack
#             card.defense += other_card.defense
#         for card in opponent.deck.cards[:]:
#             if card.attack == other_card.attack or card.defense == other_card.defense:
#                 opponent.deck.cards.remove(card)
#         # END SOLUTION
#         discarded = orig_opponent_deck_length - len(opponent.deck.cards)
#         if discarded:
#             #Uncomment the line below when you've finished implementing this method!
#             #print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
#             return

#     def copy(self):
#         return ProfessorCard(self.name, self.attack, self.defense)


########################################
# Do not edit anything below this line #
########################################

class Deck(object):
    def __init__(self, cards):
        """
        With a list of cards as input, create a deck.
        This deck should keep track of the cards it contains, and
        we should be able to draw from the deck, taking a random
        card out of it.
        """
        self.cards = cards

    def draw(self):
        """
        Draw a random card and remove it from the deck.
        """
        assert self.cards, 'The deck is empty!'
        rand_index = random.randrange(len(self.cards))
        return self.cards.pop(rand_index)

    def is_empty(self):
        return len(self.cards) == 0

    def copy(self):
        """
        Create a copy of this deck.
        """
        return Deck([card.copy() for card in self.cards])

class Game(object):

    win_score = 8

    def __init__(self, player1, player2):
        """
        Initialize a game of <REPLACE NAME>.
        """
        self.player1, self.player2 = player1, player2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self, p1_card, p2_card):
        """
        After each player picks a card, play them against
        each other.
        """
        p1_card.effect(p2_card, self.player1, self.player2)
        p2_card.effect(p1_card, self.player2, self.player1)
        p1_power = p1_card.power(p2_card)
        p2_power = p2_card.power(p1_card)
        if p1_power > p2_power:
            # Player 1 wins the round.
            self.p1_score += 1
            result = 'won'
        elif p2_power > p1_power:
            # Player 2 wins the round.
            self.p2_score += 1
            result = 'lost'
        else:
            # This round is a draw.
            result = 'tied'
        # Display results to user.
        print('You {} this round!'.format(result))
        print('{}\'s card: {}; Power: {}'.format(self.player1.name, p1_card, p1_power))
        print('Opponent\'s card: {}; Power: {}'.format(p2_card, p2_power))


    def game_won(self):
        """
        Check if the game is won and, if so,
        which player won.
        """
        if self.p1_score < self.win_score and self.p2_score < self.win_score:
            return 0
        return 1 if self.p1_score > self.p2_score else 2

    def display_scores(self):
        """
        Display players' scores to the user.
        """
        print('{}\'s score: {}'.format(self.player1.name, self.p1_score))
        print('Opponent\'s score: {}'.format(self.p2_score))
