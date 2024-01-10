print("Welcome to Hindu library".center(100, "-"))

class Library:
    books = ["ramayan", "mahabharat", "vishnupuran", "shivpuran", "gita"]

    def start(self):
        while True:
            print("Enter 1 for book list\nEnter 2 for request book\nEnter 3 for submission of book\nEnter 4 for donate a book\nEnter 5 for exit")
            x = int(input("\nYour input: "))
            
            if x == 1:
                self.showbooklist()
            elif x == 2:
                self.requestbook()
            elif x == 3:
                self.submitbook()
            elif x == 4:
                self.donatebook()
            elif x == 5:
                print("\nThanks for coming please visit again. Jai shree ram\n")
                break
            else:
                print("\nInvalid input. Retry!\n")

    def showbooklist(self):
        for book in self.books:
            print(book)
        print("\n")

    def requestbook(self):
        z = input("\nEnter the book name: ").lower()
        if z in self.books:
            print(f'\nYour book {z} has been granted. Please return it within 15 days.')
            self.books.remove(z)
        else:
            print(f'\nBook {z} is not available in the library.')

    def submitbook(self):
        z = input("\nEnter the book name you want to submit: ").lower()
        if z in self.books:
            print(f"\nThe book {z} is already in the library!")
            return

        y = int(input(f"\nFor how many days have you had {z}: "))
        if y <= 15:
            print("\nNo fine will be taken.")
        else:
            fine = (y - 15) * 2
            print(f"\nThere is a 2rs/day fine, so your fine will be: {fine} rs.")
        self.books.append(z)
        print("\nThanks for submission.")

    def donatebook(self):
        z = input("\nEnter the book name you want to donate: ").lower()
        if z in self.books:
            print(f"\nThe book {z} is already in the library!")
        else:
            self.books.append(z)
            print("\nThanks for the donation.")

l1 = Library()
l1.start()
