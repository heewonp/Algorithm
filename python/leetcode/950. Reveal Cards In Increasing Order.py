from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        d = deque()
        while sorted_deck:
            if d :
                d.appendleft(d.pop())
            d.appendleft(sorted_deck.pop())

        return list(d)