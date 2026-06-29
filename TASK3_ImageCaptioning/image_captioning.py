captions = {
    "dog": "A happy dog is playing in the park.",
    "cat": "A cute cat is sitting on a sofa.",
    "car": "A red sports car is parked on the road.",
    "tree": "A green tree is standing in a beautiful garden.",
    "beach": "A beautiful beach with golden sand and blue water.",
    "mountain": "Snow-covered mountains under a clear blue sky.",
    "flower": "A colorful flower blooming in the garden.",
    "bird": "A small bird is flying in the sky."
}

print("=" * 50)
print("      IMAGE CAPTIONING SYSTEM")
print("=" * 50)

print("\nAvailable Image Categories:")
for item in captions:
    print("-", item)

image = input("\nEnter image category: ").lower()

if image in captions:
    print("\nGenerated Caption:")
    print(captions[image])
else:
    print("\nSorry! Caption not available for this category.")
