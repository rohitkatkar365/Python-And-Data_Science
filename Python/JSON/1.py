import json

books = {
    "Alice": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publication_year": 1960,
        "genre": "Fiction",
        "ISBN": "978-0-06-112008-4",
        "pages": 281,
        "publisher": "J.B. Lippincott & Co.",
        "language": "English",
        "available_formats": ["Hardcover", "Paperback", "eBook", "Audiobook"],
        "price": 18.99  # USD
    },
    "Bob": {
        "title": "1984",
        "author": "George Orwell",
        "publication_year": 1949,
        "genre": "Dystopian, Political Fiction",
        "ISBN": "978-0-452-28423-4",
        "pages": 328,
        "publisher": "Secker & Warburg",
        "language": "English",
        "available_formats": ["Hardcover", "Paperback", "eBook", "Audiobook"],
        "price": 15.99  # USD
    },
    "Charlie": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813,
        "genre": "Romance",
        "ISBN": "978-1-85326-000-1",
        "pages": 279,
        "publisher": "T. Egerton, Whitehall",
        "language": "English",
        "available_formats": ["Hardcover", "Paperback", "eBook", "Audiobook"],
        "price": 12.99  # USD
    },
    "David": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genre": "Tragedy",
        "ISBN": "978-0-7432-7356-5",
        "pages": 180,
        "publisher": "Charles Scribner's Sons",
        "language": "English",
        "available_formats": ["Hardcover", "Paperback", "eBook", "Audiobook"],
        "price": 14.99  # USD
    },
    "Eve": {
        "title": "Moby-Dick",
        "author": "Herman Melville",
        "publication_year": 1851,
        "genre": "Adventure, Epic",
        "ISBN": "978-0-14-243724-7",
        "pages": 585,
        "publisher": "Richard Bentley",
        "language": "English",
        "available_formats": ["Hardcover", "Paperback", "eBook", "Audiobook"],
        "price": 17.99  # USD
    }
}

j = json.dumps(books)
# print(type(j))
s = json.loads(j)
# print(type(s))
# print(j)
# for i in s.items():
#     print(i)

print(s["Alice"]["price"])
# with open("JSON\\data.txt","r+") as f:
    # f.write(j)
    # print(f.read())
