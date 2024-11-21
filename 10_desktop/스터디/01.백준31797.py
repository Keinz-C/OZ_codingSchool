def find_drinker(N, M, hands):
    hand_positions = []
    for i in range(M):
        H1, H2 = hands[i]
        hand_positions.append((H1, i + 1))
        hand_positions.append((H2, i + 1))
        
    hand_positions.sort()
    
    drinker = hand_positions[N-1][1]
    return drinker

N, M = map(int, input().split())
hands = [tuple(map(int, input().split())) for _ in range(M)]

print(find_drinker(N, M, hands))