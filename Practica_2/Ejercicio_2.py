
playlist = [
{"title": "Bohemian Rhapsody", "duration": "5:55"},
{"title": "Hotel California", "duration": "6:30"},
{"title": "Stairway to Heaven", "duration": "0:00"},
{"title": "Imagine", "duration": "3:07"},
{"title": "Smells Like Teen Spirit", "duration": "5:01"},
{"title": "Billie Jean", "duration": "4:54"},
{"title": "Hey Jude", "duration": "7:11"},
{"title": "Like a Rolling Stone", "duration": "6:13"},
]
minutos =0
segundos = 0
for x in playlist:
    y = x["duration"].split(':')
    segundos += int(y[1])
    if segundos >=60:
        minutos += 1
        segundos -= 60
    minutos += int(y[0])

print(f'{minutos}:{segundos}')

cancion_max = max(playlist, key=lambda x: int(x["duration"].split(':')[0]*60) + int(x["duration"].split(':')[1]))

print(cancion_max)