# https://dmoj.ca/problem/othscc2p1
# Simple implementation, using dictionary

table = {'queen': 9,
         'rook': 5,
         'bishop': 3,
         'knight': 3,
         'pawn': 1,
         'king': 'priceless'
         }

piece = input()
print(table[piece])
