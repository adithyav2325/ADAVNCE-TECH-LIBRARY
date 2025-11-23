import time  

# time is only used to make the visual effect of some delay for showing some realistic

class Books:
    def __init__(self, book_id, titled, author, prices, days_limited):
        self.id = book_id
        self.titled = titled
        self.author = author
        self.prices = prices
        self.days_limited = days_limited
        self.isavailable = True

class LibrarySystem:
    def __init__(self):
        self.wallet = 1000.0  # The amount set as defeault
        self.books = []      # All books as an object us stored here 
        self.my_bag = []     # Bowrroed books are stored here 
        
        self.books.append(Books(101, "Python Essentials", "Vidyarthi Team", 50, 7))
        self.books.append(Books(102, "Data Structures", "Paulo Coe", 30, 14))
        self.books.append(Books(103, "Cyber Security Essentials", "James Charles", 60, 10))
        self.books.append(Books(104, "Java Core", "Robert Kichar", 40, 7))
        self.books.append(Books(105, "Java Advanced", "J.K. Powling", 80, 30))
        self.books.append(Books(106, "C++ Essentials", "Arron Harrdie", 40, 7))
        self.books.append(Books(107, "System Desgining", "Richard Gleese", 100, 14))
        self.books.append(Books(108, "Operating System", "Sukdev Sharma", 90, 7))
        self.books.append(Books(109, "MLops", "Robert Joe", 150, 21))
        self.books.append(Books(110, "AWS Essentials", "Danis Richard", 200, 28))

    
    def add_to_wallet(self):
        try:
            print(f"\nCurrent Wallet: ₹{self.wallet}")
            amounts = float(input("Enter Amount to Add: ₹"))
            if amounts > 0:
                self.wallet += amounts  
                print(f">> Success! New Balance: ₹{self.wallet}")
            else:
                print(">> Amount must be positive.")
        except:
            print(">> Invalid Input.")
        time.sleep(1)

    def browse_library(self):
        print("\n" + "="*60)
        print(f"{'ID':<5} {'TITLE':<25} {'AUTHOR':<20} {'COST':<8} {'DAYS':<5}")
        print("-" * 60)
        
       
        for books in self.books:
            if books.isavailable:
                print(f"{books.id:<5} {books.titled:<25} {books.author:<20} ₹{books.prices:<7} {books.days_limited}")
        print("-" * 60)

        choices = input("\nEnter Book ID to Borrow (0 to Back): ")
        if choices == '0':
            return

        #used to find the book entered
        selected = None
        for book in self.books:
            if str(book.id) == choices:
                selected = book
                break
        
        if selected:
            if self.wallet >= selected.prices:
                #used to update the wallet after book bowrrowing
                self.wallet -= selected.prices
                selected.isavailable = False
                
                transaction = {
                    "book": selected,
                    "due_in": selected.days_limited
                }
                self.my_bag.append(transaction)
                
                print(f"\n>> SUCCESS! You borrowed '{selected.titled}'")
                print(f">> Remaining Wallet: ₹{self.wallet}")
                print(f">> Due in: {selected.days_limited} days")
            else:
                print("\n>> ERROR: Insufficient Funds in Wallet!")
        else:
            print("\n>> ERROR: Invalid Book ID.")
        
        time.sleep(2)

    def my_bag_cart(self):
        print("\n" + "="*60)
        print("MY BORROWED BOOKS")
        print(f"{'ID':<5} {'TITLE':<25} {'DUE IN (DAYS)':<15}")
        print("-" * 60)

        if len(self.my_bag) == 0:
            print("(Your bag is empty)")
        else:
            for items in self.my_bag:
                b = items['book']
                d = items['due_in']
                print(f"{b.id:<5} {b.titled:<25} {d:<15}")

        print("-" * 60)
        print("Options: [R]eturn Book | [E]xtend Time (+5 Days for ₹20) | [B]ack")
        actioned = input("Select Action: ").lower()

        if actioned == 'r':
            self.return_book_back()
        elif actioned == 'e':
            self.extend_book_time()

    def return_book_back(self):
        bids = input("Enter Book ID to Return: ")
        founded = False
        
        for items in self.my_bag:
            if str(items['book'].id) == bids:
                #used to return the book again back to library
                items['book'].isavailable = True  # It makes the book available again for the user
                self.my_bag.remove(items)          # It removes the book from the back
                print(f">> '{items['book'].titled}' Returned Successfully.")
                founded = True
                break
        
        if not founded:
            print(">> ID not found in your bag.")
        time.sleep(1)

    def extend_book_time(self):
        bids = input("Enter Book ID to Extend: ")
        founded = False

        for items in self.my_bag:
            if str(items['book'].id) == bids:
                if self.wallet >= 20.0:
                    self.wallet -= 20.0
                    items['due_in'] += 5  #It adds extra 5 days 
                    print(f">> Extended! New Due In: {items['due_in']} days.")
                    print(f">> Fee Deducted. Wallet: ${self.wallet}")
                else:
                    print(">> Insufficient funds for extension ($2 needed).")
                founded = True
                break
        
        if not founded:
            print(">> ID not found in your bag.")
        time.sleep(1)

def main():
    system = LibrarySystem()
    
    #the loop runs infinte times to always show menu
    while True:
        #used to just make the screen more readable and user firendly 
        print("\n" * 50) 
        #used for design purpose
        print("="*50)
        print(f"ADVANCE TECH LIBRARY")
        print(f"Wallet Balance: ₹{system.wallet}")
        #used for design purpose
        print("="*50)
        print("1.Browse Store")
        print("2.My Bag")
        print("3.Add Funds")
        print("4.Exit")

        choices = input("\nSelect Option: ")

        if choices == '1':
            system.browse_library()
        elif choices == '2':
            system.my_bag_cart()
        elif choices == '3':
            system.add_to_wallet()
        elif choices == '4':
            print("Thank You Tech Buddy")
            break
        else:
            print("Invalid Choice.")
            time.sleep(1)

if __name__ == "__main__":
    main()
