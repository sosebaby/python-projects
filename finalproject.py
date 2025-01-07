import csv

# Load dataset from CSV file
def loadBooks(filename):
    books = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numerical values to appropriate types
                row["User Rating"] = float(row["User Rating"])
                row["Reviews"] = int(row["Reviews"])
                row["Price"] = float(row["Price"])
                row["Year"] = int(row["Year"])
                books.append(row)
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
    return books

# 1. Get books by genre
def getBooksByGenre(books, genre):
    return [book["Name"] for book in books if book["Genre"].lower() == genre.lower()]

# 2. Get books by author
def getBooksByAuthor(books, author):
    return [book["Name"] for book in books if book["Author"].lower() == author.lower()]

# 3. Get high-rated books
def getHighRatedBooks(books, minRating):
    return [book["Name"] for book in books if book["User Rating"] >= minRating]

# 4. Get book info
def getBookInfo(books, title):
    for book in books:
        if book["Name"].lower() == title.lower():
            return book
    return None

# 5. Recommend books based on similarity
def recommendBooks(books, favoriteBookTitle):
    favoriteBook = getBookInfo(books, favoriteBookTitle)
    if not favoriteBook:
        print("Favorite book not found in the dataset.")
        return []

    recommendations = []
    for book in books:
        if book["Name"].lower() == favoriteBookTitle.lower():
            continue
        score = 0

        # Similarity scoring
        if book["Genre"] == favoriteBook["Genre"]:
            score += 3
        if book["Author"] == favoriteBook["Author"]:
            score += 2
        if abs(book["User Rating"] - favoriteBook["User Rating"]) <= 0.5:
            score += 1
        if abs(book["Reviews"] - favoriteBook["Reviews"]) <= 1000:
            score += 1
        if abs(book["Price"] - favoriteBook["Price"]) <= 5:
            score += 1
        if abs(book["Year"] - favoriteBook["Year"]) <= 2:
            score += 1

        recommendations.append((book["Name"], score))

    # Sort recommendations by score (descending)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    # Remove duplicates and return top 2 recommendations
    uniqueRecommendations = []
    seenBooks = set()
    for bookName, score in recommendations:
        if bookName not in seenBooks:
            uniqueRecommendations.append((bookName, score))
            seenBooks.add(bookName)
            if len(uniqueRecommendations) == 2:
                break

    return uniqueRecommendations

def main():
    books = loadBooks("books.csv")
    if not books:
        return

    while True:
        print("\nBook Recommendation System")
        print("1. Search by Genre")
        print("2. Search by Author")
        print("3. Search by Rating")
        print("4. Recommend Books")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            genre = input("Enter genre (e.g., Fiction, Non Fiction): ")
            results = getBooksByGenre(books, genre)
            print("Books in genre:", results if results else "No books found.")
        elif choice == "2":
            author = input("Enter author name: ")
            results = getBooksByAuthor(books, author)
            print("Books by author:", results if results else "No books found.")
        elif choice == "3":
            try:
                minRating = float(input("Enter minimum rating (0-5): "))
                results = getHighRatedBooks(books, minRating)
                print("Books with high ratings:", results if results else "No books found.")
            except ValueError:
                print("Invalid rating. Please enter a number.")
        elif choice == "4":
            favoriteBook = input("Enter the title of your favorite book: ")
            recommendations = recommendBooks(books, favoriteBook)
            if recommendations:
                print(f"\nIf you liked '{favoriteBook}', you may also like:")
                for rec in recommendations:
                    print(f"{rec[0]} (Similarity Score: {rec[1]})")
            else:
                print("No recommendations found.")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()

