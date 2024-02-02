package main

import "fmt"

type Book struct {
	title  string
	author string
	pages  int
	isRead bool
}

type Shelf []Book

func addBookToShelf(b Book, s *Shelf) {
	*s = append(*s, b)
}

func addBook(t, a string, p int, r bool) Book {
	book := Book{
		title: t, author: a, pages: p, isRead: r,
	}
	return book
}

func readBook(b *Book) {
	b.isRead = true
}

func printBook(b Book) {
	fmt.Printf("Title: %s by %s\nPages: %d\nisRead: %v",
		b.title, b.author, b.pages, b.isRead,
	)
}

func printShelf(s Shelf) {
	for i, book := range s {
		fmt.Printf("Book no: %d\n", i+1)
		printBook(book)
		fmt.Println()
		fmt.Println()
	}
}

func main() {
	fmt.Println("============> Book Shelf <===========")
	var myShelf Shelf

	book1 := addBook("Ramayana", "Valmiki", 200, false)
	addBookToShelf(book1, &myShelf)

	book2 := addBook("Can't Hurt Me", "David Goggins", 100, false)
	addBookToShelf(book2, &myShelf)

	readBook(&myShelf[0])
	fmt.Println()
	printShelf(myShelf)
}
