#Blackjack project

import random
playing = False
chip_pool = 100
bet = 1
restart = "Press 'd' to deal the cards again or 'q' to quit."
suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranking = ('A','2','3','4','5','6','7','8','9','10','Jack','Queen','King')
card_val = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

class Card():

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.suit + self.rank

	def get_suit(self):
		return self.suit

	def get_rank(self):
		return self.rank

	def draw(self):
		print (self.suit +  ' ' + self.rank)

class Hand():

	def __init__(self):
		self.cards = []
		self.value = 0
		# Aces can be either 1 or 11 so made Ace a boolean value to check if ace is in hand
		self.ace = False

	def add_card(self, card):
		self.cards.append(card)
		if card.rank == 'A':
			self.ace = True
		self.value += card_val[card.rank]

	def add_val(self):
		if (self.ace == True and self.value < 12):
			return self.value + 10
		else:
			return self.value

	def __str__(self):
		hand_comp = ""
		for card in self.cards:
			hand_comp += " " + card.__str__()
		return 'The hand has %s' %hand_comp

	def draw(self, hidden):
		if hidden == True and playing == True:
			starting_card = 1
		else:
			starting_card = 0
		for x in range(starting_card, len(self.cards)):
			self.cards[x].draw()

class Deck():

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranking:
				self.deck.append(Card(suit, rank))

	def shuffle(self):
		random.shuffle(self.deck)
	
	def deal(self):
		top_card = self.deck.pop()
		return top_card
	
	def __str__(self):
		deck_comp = ""
		for card in self.cards:
			deck_comp += " " + deck_comp.__str__()
		return "The deck has" + deck_comp


def make_bet():
	global bet
	bet = 0
	print ''
	print 'How much would you like to wager? (enter whole number)'
	while bet == 0:
		bet_comp = int(raw_input())
		if bet_comp >= 1 and bet_comp <= chip_pool:
			bet = bet_comp
		else:
			print "Can't wager what you don't have, and you only have " + str(chip_pool) + " and not a whole lotta time"

def deal():

	global result, playing, deck, player_hand, dealer_hand, chip_pool, bet

	deck = Deck()
	deck.shuffle()
	make_bet()
	player_hand = Hand()
	dealer_hand = Hand()
	#Deal out first card to player and dealer
	player_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())
	#Deal out second card to the player and dealer
	player_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())
	result = "Dare you hit or stay? (Press h or s) "
	if playing == True:
		print 'Fold, sorry '
		chip_pool -= bet
	playing = True
	game_step()

def hit_me():
	global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

	if playing == True:
		if player_hand.add_val() <= 21:
			player_hand.add_card(deck.deal())
		print "Player hand is %s" %player_hand

		if player_hand.add_val() > 21:
			result = "Busted, mate " + restart
			chip_pool -= bet
			playing = False
	else:
		result = "Sorry, can't hit " + restart
	game_step()

def stand():
	global playing, chip_pool, deck, player_hand, dealer_hand, result, bet

	if playing == False:
		if player_hand.add_val() > 0:
			result = "Sorry, you can't stand! "

	else:
		while dealer_hand.add_val < 17:
			dealer_hand.add_card(deck.deal())

		if dealer_hand.add_val > 21:
			result = "Dealer busted, you win... for now. " + restart
			chip_pool += bet
			playing = False

		elif dealer_hand.add_val() > player_hand.add_val():
			result = "House wins, yet again. " + restart
			chip_pool -= bet
			playing = False

		elif dealer_hand.add_val() == player_hand.add_val():
			result = "Tie goes to the house, better luck next time " + restart
			chip_pool -= bet
			playing = False

		else:
			result = "You live to see another day... " + start
			chip_pool += bet
			playing = False
	game_step()

def game_step():
	#Displaying player's hand
	print ''
	print "Player hand is: ", player_hand.draw(hidden = False)
	print "Player total is: ", str(player_hand.add_val())

	#Displaying dealer's hand
	print ''
	print "Dealer's hand is: ", dealer_hand.draw(hidden = True)
	# If game round is over
	if playing == False:
		print  " Dealer's total is: " + str(dealer_hand.add_val() )
		print "Chip Total: " + str(chip_pool)
	# Otherwise, don't know the second card yet
	else:
		print " with another card hidden upside down "
	# Print result of hit or stand.
	print result
	player_input()

def game_exit():
	print 'Thanks for playing! '
	exit()

def player_input():
	''' Read user input, lower case it just to be safe'''
	plin = raw_input().lower()
	
	
	if plin == 'h':
		hit_me()
	elif plin == 's':
		stand()
	elif plin == 'd':
		deal()
	elif plin == 'q':
		game_exit()
	else:
		print "Invalid Input...Enter h, s, d, or q: "
		player_input()

def intro():
	statement = "Welcome to Jaro's BBC (Beta Blackjack Cardgame)! Try to get as close to 21 without busting. Dealer hits till 17 and aces count as 1 or 11. Your starting bankroll is 100."
	print statement

deck = Deck()
deck.shuffle()
player_hand = Hand()
dealer_hand = Hand()
intro()
deal()
