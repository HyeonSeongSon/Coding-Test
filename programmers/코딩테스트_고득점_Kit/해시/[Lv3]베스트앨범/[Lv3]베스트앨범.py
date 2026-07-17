from collections import defaultdict

def solution(genres, plays):
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        genre_total[genre] += play
        genre_songs[genre].append((idx, play))

    sorted_genres = sorted(
        genre_total.keys(),
        key=lambda g: genre_total[g],
        reverse=True
    )

    answer = []

    for genre in sorted_genres:
        songs = sorted(
            genre_songs[genre],
            key=lambda x: (-x[1], x[0])
        )

        answer.extend(idx for idx, _ in songs[:2])

    return answer