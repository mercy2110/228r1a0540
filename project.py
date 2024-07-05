from tkinter import *
import pymysql as p
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
y = list(range(2020, 2040))
d = list(range(1, 32))


class Book:
    def __init__(self, title, author, rating, summary, reviews, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.summary = summary
        self.reviews = reviews
        self.price = price


class BookVerseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Verse")

        # Dummy book data
        self.books = [
            Book(
                title="Book 1: Python Programming",
                author="Williams",
                rating=4.3,
                summary="Python Programming book provides a comprehensive introduction to the Python language and its applications in real-world scenarios. It covers basic to advanced topics including data structures, algorithms, and web development.",
                reviews=["Great book!", "Highly recommended for beginners.", "Easy to follow examples."],
                price="$35.50"
            ),
            Book(
                title="Book 2: Java Programming",
                author="Rutherford",
                rating=4.5,
                summary="Java Programming book offers a detailed exploration of Java programming concepts, from basic syntax to advanced features such as multithreading and GUI development. Suitable for both beginners and experienced programmers.",
                reviews=["Excellent read!", "Comprehensive and well-structured content."],
                price="$40.00"
            ),
            Book(
                title="Book 3: Machine Learning with Python",
                author="Shake appe",
                rating=4.0,
                summary="Machine Learning with Python introduces readers to the fundamental concepts of machine learning and its practical applications using Python libraries like scikit-learn and TensorFlow. Includes hands-on exercises and real-world case studies.",
                reviews=["Good book!", "Clear explanations and practical examples."],
                price="$45.99"
            ),
            Book(
                title="Book 4: Data Science Handbook",
                author="Mahdendr",
                rating=4.2,
                summary="Data Science Handbook covers essential topics in data science, including statistical analysis, data visualization, and machine learning algorithms. It provides insights into best practices and tools used by data scientists in industry.",
                reviews=["Informative and well-written.", "Useful for beginners and professionals alike."],
                price="$38.75"
            ),
            Book(
                title="Book 5: Web Development with Django",
                author="Shake williams",
                rating=4.8,
                summary="Web Development with Django is a comprehensive guide to building web applications using the Django framework. It covers Django's MVC architecture, ORM, security features, and deployment strategies.",
                reviews=["Great book for Django enthusiasts!", "Practical examples and clear explanations."],
                price="$42.50"
            ),
            Book(
                title="Book 6: Cybersecurity Fundamentals",
                author="cyber-star",
                rating=4.1,
                summary="Cybersecurity Fundamentals provides an overview of cybersecurity principles, threats, and defense strategies. It covers topics such as network security, cryptography, and ethical hacking techniques.",
                reviews=["Essential reading for cybersecurity professionals.", "Well-structured and informative content."],
                price="$37.25"
            ),
        ]

        self.create_widgets()

    def create_widgets(self):
        # Title
        lbl_title = Label(self.master, text="Book Verse", font=("Helvetica", 24, "bold"), fg="blue")
        lbl_title.grid(row=0, column=0, columnspan=3, pady=10)

        # Book Grid
        row_num = 1
        col_num = 0
        for book in self.books:
            frame = Frame(self.master, bd=2, relief=RIDGE)
            frame.grid(row=row_num, column=col_num, padx=10, pady=10)

            lbl_book_title = Label(frame, text=f"{book.title}", font=("Helvetica", 12, "bold"), fg="green")
            lbl_book_title.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

            lbl_author = Label(frame, text=f"Author: {book.author}")
            lbl_author.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

            lbl_rating = Label(frame, text=f"Rating: {book.rating}")
            lbl_rating.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

            lbl_price = Label(frame, text=f"Price: {book.price}")
            lbl_price.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

            btn_buy = Button(frame, text="Buy", command=lambda b=book: self.buy_ebook(b))
            btn_buy.grid(row=4, column=0, pady=5, padx=5, sticky="ew")

            btn_summary = Button(frame, text="Summary", command=lambda b=book: self.get_summary(b))
            btn_summary.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

            btn_reviews = Button(frame, text="Reviews", command=lambda b=book: self.view_reviews(b))
            btn_reviews.grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            btn_rating = Button(frame, text="Rating", command=lambda b=book: self.view_rating(b))
            btn_rating.grid(row=6, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1

    def buy_ebook(self, book):
        messagebox.showinfo("Buy eBook", f"You have bought '{book.title}' by {book.author} for {book.price}.")

    def get_summary(self, book):
        messagebox.showinfo("Book Summary", f"Summary of '{book.title}':\n\n{book.summary}")

    def view_reviews(self, book):
        reviews = "\n".join(book.reviews)
        messagebox.showinfo("Customer Reviews", f"Customer Reviews for '{book.title}':\n\n{reviews}")

    def view_rating(self, book):
        messagebox.showinfo("Book Rating", f"The rating for '{book.title}' is {book.rating}.")


def connectdb():
    global con, cur
    con = p.connect(host='localhost', user='root', password='', database='LibraryDB')
    cur = con.cursor()


def closedb():
    cur.close()
    con.close()


def loginlibr():
    global window
    connectdb()
    cur.execute("SELECT * FROM Login WHERE userid=%s AND branch=%s", (e1.get().strip(), e2.get().strip()))
    data = cur.fetchone()
    if data:
        closedb()
        libr()
    else:
        messagebox.showerror("Login Error", "Invalid Credentials")
        window.withdraw()
        closedb()
        home()


def libr():
    global window
    window.withdraw()
    global win
    win = Tk()
    win.title('Library')
    win.geometry("500x500+480+180")
    win.resizable(False, False)
    bo = Button(win, height=2, width=25, text=' View All Books ', command=viewallbooks)
    b1 = Button(win, height=2, width=25, text=' Add Book ', command=addbook)
    b2 = Button(win, height=2, width=25, text=' Issue Book ', command=issuebook)
    b3 = Button(win, height=2, width=25, text=' Return Book ', command=returnbook)
    b4 = Button(win, height=2, width=25, text=' View Book ', command=viewbook)
    b5 = Button(win, height=2, width=25, text=' Issued Book ', command=issuedbook)
    b6 = Button(win, height=2, width=25, text=' Delete Book ', command=deletebook)
    b7 = Button(win, height=2, width=25, text=' LogOut ', command=logout)
    bo.place(x=110, y=30)
    b1.place(x=110, y=80)
    b2.place(x=110, y=130)
    b3.place(x=110, y=180)
    b4.place(x=110, y=230)
    b5.place(x=110, y=280)
    b6.place(x=110, y=330)
    b7.place(x=110, y=380)
    win.mainloop()


def viewallbooks():
    global win
    win.destroy()
    win = Tk()
    win.title('View All Book')
    win.resizable(False, False)
    app = BookVerseApp(win)
    win.mainloop()


def addbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Add Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="Fill Book Details", font=("Arial", 20, "bold")).place(x=100, y=10)
    l1 = Label(win, text="Book Title:").place(x=50, y=60)
    l2 = Label(win, text="Book Author:").place(x=50, y=100)
    l3 = Label(win, text="Book ID:").place(x=50, y=140)
    l4 = Label(win, text="Price:").place(x=50, y=180)
    e1 = Entry(win)
    e1.place(x=160, y=60)
    e2 = Entry(win)
    e2.place(x=160, y=100)
    e3 = Entry(win)
    e3.place(x=160, y=140)
    e4 = Entry(win)
    e4.place(x=160, y=180)

    def adbook():
        connectdb()
        cur.execute("INSERT INTO books(bookname, authorname, bookid, price) VALUES (%s, %s, %s, %s)",
                    (e1.get(), e2.get(), e3.get(), e4.get()))
        con.commit()
        closedb()
        messagebox.showinfo("Added", "Book added successfully")

    b = Button(win, text="Add Book", command=adbook).place(x=150, y=220)
    win.mainloop()


def issuebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Issue Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="Fill Details", font=("Arial", 20, "bold")).place(x=100, y=10)
    l1 = Label(win, text="Member ID:").place(x=50, y=60)
    l2 = Label(win, text="Book ID:").place(x=50, y=100)
    l3 = Label(win, text="Date:").place(x=50, y=140)
    e1 = Entry(win)
    e1.place(x=160, y=60)
    e2 = Entry(win)
    e2.place(x=160, y=100)
    c1 = Combobox(win, values=d, width=5)
    c1.set(datetime.datetime.now().day)
    c1.place(x=160, y=140)
    c2 = Combobox(win, values=month, width=10)
    c2.set(month[datetime.datetime.now().month - 1])
    c2.place(x=220, y=140)
    c3 = Combobox(win, values=y, width=5)
    c3.set(datetime.datetime.now().year)
    c3.place(x=310, y=140)

    def isbook():
        connectdb()
        cur.execute("INSERT INTO issuebook(memberid, bookid, date) VALUES (%s, %s, %s)",
                    (e1.get(), e2.get(), str(c1.get()) + " " + c2.get() + " " + c3.get()))
        con.commit()
        closedb()
        messagebox.showinfo("Issued", "Book issued successfully")

    b = Button(win, text="Issue Book", command=isbook).place(x=150, y=220)
    win.mainloop()


def returnbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Return Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="Fill Details", font=("Arial", 20, "bold")).place(x=100, y=10)
    l1 = Label(win, text="Member ID:").place(x=50, y=60)
    l2 = Label(win, text="Book ID:").place(x=50, y=100)
    l3 = Label(win, text="Date:").place(x=50, y=140)
    e1 = Entry(win)
    e1.place(x=160, y=60)
    e2 = Entry(win)
    e2.place(x=160, y=100)
    c1 = Combobox(win, values=d, width=5)
    c1.set(datetime.datetime.now().day)
    c1.place(x=160, y=140)
    c2 = Combobox(win, values=month, width=10)
    c2.set(month[datetime.datetime.now().month - 1])
    c2.place(x=220, y=140)
    c3 = Combobox(win, values=y, width=5)
    c3.set(datetime.datetime.now().year)
    c3.place(x=310, y=140)

    def rebook():
        connectdb()
        cur.execute("DELETE FROM issuebook WHERE memberid=%s AND bookid=%s", (e1.get(), e2.get()))
        con.commit()
        closedb()
        messagebox.showinfo("Returned", "Book returned successfully")

    b = Button(win, text="Return Book", command=rebook).place(x=150, y=220)
    win.mainloop()


def viewbook():
    global win
    win.destroy()
    win = Tk()
    win.title('View Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="View Book", font=("Arial", 20, "bold")).place(x=100, y=10)
    l1 = Label(win, text="Enter Book ID:").place(x=50, y=60)
    e1 = Entry(win)
    e1.place(x=160, y=60)

    def viwbook():
        connectdb()
        cur.execute("SELECT * FROM books WHERE bookid=%s", (e1.get(),))
        data = cur.fetchone()
        if data:
            l2 = Label(win, text="Book Details", font=("Arial", 15, "bold")).place(x=100, y=100)
            l3 = Label(win, text="Title: " + data[0]).place(x=50, y=140)
            l4 = Label(win, text="Author: " + data[1]).place(x=50, y=180)
            l5 = Label(win, text="Price: " + data[3]).place(x=50, y=220)
        else:
            messagebox.showerror("Error", "Book not found")
        closedb()

    b = Button(win, text="View Book", command=viwbook).place(x=150, y=300)
    win.mainloop()


def issuedbook():
    global win
    win.destroy()
    win = Tk()
    win.title('Issued Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="Issued Book", font=("Arial", 20, "bold")).place(x=100, y=10)

    def isuedbook():
        connectdb()
        cur.execute("SELECT * FROM issuebook")
        data = cur.fetchall()
        if data:
            l2 = Label(win, text="Issued Book Details", font=("Arial", 15, "bold")).place(x=100, y=60)
            y = 100
            for row in data:
                l3 = Label(win, text="Member ID: " + row[0] + " Book ID: " + row[1] + " Date: " + row[2]).place(x=50, y=y)
                y += 40
        else:
            messagebox.showerror("Error", "No issued book found")
        closedb()

    b = Button(win, text="View Issued Book", command=isuedbook).place(x=150, y=300)
    win.mainloop()


def deletebook():
    global win
    win.destroy()
    win = Tk()
    win.title('Delete Book')
    win.geometry("400x400+480+180")
    win.resizable(False, False)
    l = Label(win, text="Delete Book", font=("Arial", 20, "bold")).place(x=100, y=10)
    l1 = Label(win, text="Enter Book ID:").place(x=50, y=60)
    e1 = Entry(win)
    e1.place(x=160, y=60)

    def delbook():
        connectdb()
        cur.execute("DELETE FROM books WHERE bookid=%s", (e1.get(),))
        con.commit()
        closedb()
        messagebox.showinfo("Deleted", "Book deleted successfully")

    b = Button(win, text="Delete Book", command=delbook).place(x=150, y=100)
    win.mainloop()


def logout():
    global win
    win.destroy()
    home()


def home(loginlibrarian=None):
    global window
    window = Tk()
    window.title('Library Management')
    window.geometry("400x400+480+180")
    window.resizable(False, False)
    lbl = Label(window, text="Librarian Login", font=("Arial", 25, "bold")).place(x=80, y=30)
    l1 = Label(window, text="User ID").place(x=80, y=100)
    l2 = Label(window, text="Branch").place(x=80, y=140)
    global e1, e2
    e1 = Entry(window)
    e1.place(x=150, y=100)
    e2 = Entry(window)
    e2.place(x=150, y=140)
    b = Button(window, text="Login", command=loginlibrarian).place(x=180, y=180)
    window.mainloop()


home()
