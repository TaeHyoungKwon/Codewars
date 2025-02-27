max_viewing_time = list(map(int, input().split()))
mel_time = list(map(int, input().split()))

def calculate_viewing_time(viewing_time):
    trailer_time, series_time, film_time = viewing_time[0], viewing_time[1], viewing_time[2]
    return trailer_time * 3 + series_time * 20 + film_time * 120


if calculate_viewing_time(max_viewing_time) == calculate_viewing_time(mel_time):
    print("Draw")
    exit()

if calculate_viewing_time(max_viewing_time) > calculate_viewing_time(mel_time):
    print("Max")
else:
    print("Mel")