def alphabet_war(fight):
    equipo1 = {'w':4,'p':3,'b':2,'s':1}
    equipo2 = {'m':4,'q':3,'d':2,'z':1}
    puntaje1 = 0
    puntaje2 = 0
    for letra in fight:
        if letra in equipo1:
            puntaje1 += equipo1[letra]
        elif letra in equipo2:
            puntaje2 += equipo2[letra]
    if puntaje1 > puntaje2:
        return 'Left side wins!'
    elif puntaje2 > puntaje1:
        return 'Right side wins!'
    else:
        return "Let's fight again!"
