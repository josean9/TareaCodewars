def knight_vs_king (knight_position, king_position):
    distX = knight_position[0] - king_position[0]
    distY = ord(knight_position[1]) - ord(king_position[1])
    distancia = distX**2 + distY**2
    if distancia == 5: 
        return 'Knight'
    elif distancia < 3: 
        return 'King'
    else:
        return 'None'