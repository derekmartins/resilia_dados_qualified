def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):

    if (tempo_chegada1 < tempo_chegada2) and (tempo_chegada1 < tempo_chegada3):
        if tempo_chegada2 < tempo_chegada3:
            ordem = (tempo_chegada1, tempo_chegada2, tempo_chegada3)

        else:
            ordem = (tempo_chegada1, tempo_chegada3, tempo_chegada2)

    elif(tempo_chegada2 < tempo_chegada1) and (tempo_chegada2 < tempo_chegada3):
        if tempo_chegada1 < tempo_chegada3:
            ordem = (tempo_chegada2, tempo_chegada1, tempo_chegada3)

        else:
            ordem = (tempo_chegada2, tempo_chegada3, tempo_chegada1)

    else:
        if tempo_chegada1 < tempo_chegada2:
            ordem = (tempo_chegada3, tempo_chegada1, tempo_chegada2)

        else:
            ordem = (tempo_chegada3, tempo_chegada2, tempo_chegada1)

    result = ''

    for i, x in enumerate(ordem):
        result += f'{i+1} - {x} minutos\n'
    return result