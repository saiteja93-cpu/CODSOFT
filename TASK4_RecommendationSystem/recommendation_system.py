movies = {
    "action": [
        "Avengers",
        "John Wick",
        "Mad Max"
    ],
    "comedy": [
        "The Mask",
        "Mr. Bean",
        "Home Alone"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix"
    ],
    "drama": [
        "Forrest Gump",
        "The Pursuit of Happyness",
        "The Shawshank Redemption"
    ]
}

print("=" * 50)
print("MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Genres:")
for genre in movies:
    print("-", genre)

choice = input("\nEnter your favorite genre: ").lower()

if choice in movies:
    print("\nRecommended Movies:")
    for movie in movies[choice]:
        print("-", movie)
else:
    print("Sorry! Genre not found.")
