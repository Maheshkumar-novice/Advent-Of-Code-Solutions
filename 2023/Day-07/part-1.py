from collections import Counter
from functools import cmp_to_key

value_weights = {
	'A': 15,
	'K': 14,
	'Q': 13,
	'J': 12,
	'T': 11
}

def compare_hand_values(v1, v2):
	v1 = value_weights.get(v1) or int(v1)
	v2 = value_weights.get(v2) or int(v2)

	if v1 < v2:
		return -1
	elif v1 > v2:
		return 1
	else:
		return 0
	

def compare_hands(hand1, hand2):
	for i, j in (zip(iter(hand1), iter(hand2))):
		comparison = compare_hand_values(i, j)
		if comparison != 0:
			return comparison
	return 0


def sort_hands(hand_cards):
	if len(hand_cards) == 1:
		return hand_cards
	else:
		return sorted(hand_cards, key=cmp_to_key(compare_hands))


with open('input.txt', 'r') as f:
	hands_weights = {}
	five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []

	for line in f:
		hand, weight = line.split()
		hands_weights[hand] = int(weight)
		count = Counter(hand)

		if len(count.values()) == 1:
			five_of_a_kind.append(hand)
		elif len(count.values()) == 2:
			if 4 in count.values():
				four_of_a_kind.append(hand)
			else:
				full_house.append(hand)
		elif len(count.values()) == 3:
			if 3 in count.values():
				three_of_a_kind.append(hand)
			else:
				two_pair.append(hand)
		elif len(count.values()) == 4:
			one_pair.append(hand)
		elif len(count.values()) == 5:
			high_card.append(hand)

	total = 0
	rank = 1
	for hands in [high_card, one_pair, two_pair, three_of_a_kind, full_house, four_of_a_kind, five_of_a_kind]:
		hands = sort_hands(hands)

		for hand in hands:
			total += (rank * hands_weights[hand])
			rank += 1

	print(total)
