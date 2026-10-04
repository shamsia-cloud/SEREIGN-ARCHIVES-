"""
Luminary Archives — academic Python algorithm layer.

This file encodes the coursework marketplace algorithms in Python:

    A  User registration
    B  Login
    C  Search
    D  Add to cart
    E  Checkout
    F  Book management (add / edit / delete)
    G  Order management

It is a standalone, standard-library implementation of the same
in-memory data model used by the live web application. The running
product translates these algorithms into TypeScript
(src/lib/store.ts) and presents them through React.

This is an academic prototype. It does not implement production
authentication, payment security, encryption, DRM, or database
security.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Literal


# ---------------------------------------------------------------------------
# Data model (mirrors the intended relational design)
# ---------------------------------------------------------------------------

Role = Literal["buyer", "admin"]
PriceFilter = Literal["all", "free", "premium"]


@dataclass
class User:
    user_id: int
    name: str
    email: str
    password: str
    role: Role


@dataclass
class Book:
    book_id: int
    title: str
    author: str
    description: str
    category: str
    price: int
    is_free: bool
    cover: str
    pdf: str
    available: bool = True


@dataclass
class CartItem:
    book_id: int


@dataclass
class OrderItem:
    book_id: int
    title: str
    unit_price: int
    quantity: int = 1


@dataclass
class Order:
    order_id: str
    user_id: int
    order_date: str
    items: list[OrderItem]
    total: int
    status: str
    payment_method: str


@dataclass
class Result:
    ok: bool
    message: str
    order_id: str | None = None
    total: int | None = None


def is_valid_email(email: str) -> bool:
    text = email.strip()
    if "@" not in text or text.startswith("@") or text.endswith("@"):
        return False
    local, _, domain = text.partition("@")
    return bool(local) and "." in domain and not domain.startswith(".")


def format_naira(amount: int) -> str:
    return f"₦{amount:,}"


def pad_order(sequence: int) -> str:
    return f"LA-{sequence:04d}"


# ---------------------------------------------------------------------------
# Seed catalogue — the same twelve titles as the live application
# ---------------------------------------------------------------------------

INITIAL_BOOKS: list[Book] = [
    Book(1, "The Prince", "Niccolò Machiavelli",
         "A blunt sixteenth-century handbook on acquiring and keeping political power.",
         "Politics", 0, True, "assets/covers/the_prince.jpg", "assets/pdf/the-prince.pdf"),
    Book(2, "The Art of War", "Sun Tzu",
         "The oldest surviving military treatise, still read far beyond the battlefield.",
         "Strategy", 0, True, "assets/covers/the_art_of_war.jpg", "assets/pdf/the-art-of-war.pdf"),
    Book(3, "Meditations", "Marcus Aurelius",
         "Private notes from a Roman emperor to himself: on duty, mortality, and a steady mind.",
         "Philosophy", 0, True, "assets/covers/meditations.jpg", "assets/pdf/meditations.pdf"),
    Book(4, "White Nights", "Fyodor Dostoevsky",
         "A tender St. Petersburg tale of loneliness, chance meeting, and being seen.",
         "Literature", 0, True, "assets/covers/white_nights.jpg", "assets/pdf/white-nights.pdf"),
    Book(5, "The Psychology of Money", "Morgan Housel",
         "Timeless lessons on wealth, greed, and happiness.",
         "Finance", 4500, False, "assets/covers/psychology_of_money.jpg", "assets/pdf/psychology-of-money.pdf"),
    Book(6, "Mastery", "Robert Greene",
         "A study of how great work is formed: apprenticeship, patience, and craft.",
         "Self-Mastery", 6500, False, "assets/covers/mastery.jpg", "assets/pdf/mastery.pdf"),
    Book(7, "The Laws of Human Nature", "Robert Greene",
         "A field guide to the forces that drive people: envy, narcissism, aggression.",
         "Psychology", 7200, False, "assets/covers/laws_of_human_nature.jpg", "assets/pdf/laws-of-human-nature.pdf"),
    Book(8, "Ego Is the Enemy", "Ryan Holiday",
         "A short argument that ego — not circumstance — is what wrecks promising work.",
         "Philosophy", 4200, False, "assets/covers/ego_is_the_enemy.jpg", "assets/pdf/ego-is-the-enemy.pdf"),
    Book(9, "The Art of Thinking Clearly", "Rolf Dobelli",
         "Ninety-nine cognitive errors, from sunk costs to social proof.",
         "Psychology", 3800, False, "assets/covers/art_of_thinking_clearly.jpg", "assets/pdf/art-of-thinking-clearly.pdf"),
    Book(10, "The Definitive Book of Body Language", "Allan and Barbara Pease",
         "A popular guide to the signals people send without speaking.",
         "Communication", 3500, False, "assets/covers/body_language.jpg", "assets/pdf/body-language.pdf"),
    Book(11, "The Daily Laws", "Robert Greene",
         "366 meditations drawn from Greene's work on power, mastery, and human nature.",
         "Wisdom", 5500, False, "assets/covers/daily_laws.jpg", "assets/pdf/daily-laws.pdf"),
    Book(12, "The 48 Laws of Power", "Robert Greene",
         "Forty-eight laws distilled from courts, palaces, and ruthless operators.",
         "Power", 8000, False, "assets/covers/48_laws_of_power.jpg", "assets/pdf/48-laws-of-power.pdf"),
]

ADMIN = User(1, "Archive Administrator", "admin@luminaryarchives.local", "admin123", "admin")


# ---------------------------------------------------------------------------
# Archive — in-memory prototype store
# ---------------------------------------------------------------------------

@dataclass
class Archive:
    users: list[User] = field(default_factory=lambda: [ADMIN])
    books: list[Book] = field(default_factory=lambda: list(INITIAL_BOOKS))
    cart: list[CartItem] = field(default_factory=list)
    orders: list[Order] = field(default_factory=list)
    current_user_id: int | None = None
    next_book_id: int = 13
    next_user_id: int = 2
    next_order_seq: int = 1

    def current_user(self) -> User | None:
        if self.current_user_id is None:
            return None
        return next((u for u in self.users if u.user_id == self.current_user_id), None)

    def find_book(self, book_id: int) -> Book | None:
        return next((b for b in self.books if b.book_id == book_id), None)

    def cart_books(self) -> list[Book]:
        found: list[Book] = []
        for item in self.cart:
            book = self.find_book(item.book_id)
            if book:
                found.append(book)
        return found

    def cart_total(self) -> int:
        return sum(0 if b.is_free else b.price for b in self.cart_books())

    def owns_book(self, book_id: int) -> bool:
        book = self.find_book(book_id)
        if book and book.is_free:
            return True
        user = self.current_user()
        if not user:
            return False
        return any(
            item.book_id == book_id
            for order in self.orders
            if order.user_id == user.user_id
            for item in order.items
        )

    # ------------------------------------------------------------------
    # Algorithm A — User registration
    # ------------------------------------------------------------------
    def register(self, name: str, email: str, password: str) -> Result:
        name = name.strip()
        email = email.strip().lower()
        if not name or not email or not password:
            return Result(False, "Name, email, and password are required.")
        if not is_valid_email(email):
            return Result(False, "Please enter a valid-looking email address.")
        if any(u.email == email for u in self.users):
            return Result(False, "An account with this email already exists.")
        user = User(self.next_user_id, name, email, password, "buyer")
        self.users.append(user)
        self.current_user_id = user.user_id
        self.next_user_id += 1
        return Result(True, "Welcome to Luminary Archives.")

    # ------------------------------------------------------------------
    # Algorithm B — Login
    # ------------------------------------------------------------------
    def login(self, email: str, password: str) -> Result:
        email = email.strip().lower()
        if not email or not password:
            return Result(False, "Email and password are required.")
        user = next((u for u in self.users if u.email == email and u.password == password), None)
        if user is None:
            return Result(False, "Incorrect email or password.")
        self.current_user_id = user.user_id
        return Result(True, f"Welcome back, {user.name.split()[0]}.")

    def logout(self) -> None:
        self.current_user_id = None
        self.cart = []

    # ------------------------------------------------------------------
    # Algorithm C — Search (title, author, category; case-insensitive)
    # ------------------------------------------------------------------
    def search(self, term: str) -> list[Book]:
        query = term.strip().lower()
        results: list[Book] = []
        for book in self.books:
            haystack = f"{book.title} {book.author} {book.category}".lower()
            if query in haystack:
                results.append(book)
        return results

    def filter_books(
        self,
        term: str = "",
        price: PriceFilter = "all",
        category: str = "all",
    ) -> list[Book]:
        results: list[Book] = []
        query = term.strip().lower()
        for book in self.books:
            if not book.available and price != "all":
                continue
            if query and query not in f"{book.title} {book.author} {book.category}".lower():
                continue
            if price == "free" and not book.is_free:
                continue
            if price == "premium" and book.is_free:
                continue
            if category != "all" and book.category != category:
                continue
            results.append(book)
        return results

    # ------------------------------------------------------------------
    # Algorithm D — Add to cart (one copy per title; no duplicates)
    # ------------------------------------------------------------------
    def add_to_cart(self, book_id: int) -> Result:
        book = self.find_book(book_id)
        if book is None:
            return Result(False, "This book could not be found.")
        if not book.available:
            return Result(False, "This title is currently unavailable.")
        if book.is_free:
            return Result(False, "Free titles can be read without checkout.")
        if self.owns_book(book_id):
            return Result(False, "You already have this book in your archive.")
        if any(item.book_id == book_id for item in self.cart):
            return Result(False, "This book is already in your cart.")
        self.cart.append(CartItem(book_id))
        return Result(True, f'"{book.title}" added to cart.')

    def remove_from_cart(self, book_id: int) -> None:
        self.cart = [item for item in self.cart if item.book_id != book_id]

    # ------------------------------------------------------------------
    # Algorithm E — Checkout (simulated payment)
    # ------------------------------------------------------------------
    def checkout(self, payment_method: str = "Demo Payment") -> Result:
        user = self.current_user()
        if user is None:
            return Result(False, "Please sign in to complete checkout.")
        items = self.cart_books()
        if not items:
            return Result(False, "Your cart is empty.")
        order_items = [
            OrderItem(b.book_id, b.title, 0 if b.is_free else b.price, 1)
            for b in items
        ]
        total = sum(item.unit_price for item in order_items)
        order = Order(
            order_id=pad_order(self.next_order_seq),
            user_id=user.user_id,
            order_date=datetime.now(timezone.utc).isoformat(),
            items=order_items,
            total=total,
            status="Completed",
            payment_method=payment_method,
        )
        self.orders.append(order)
        self.cart = []
        self.next_order_seq += 1
        return Result(
            True,
            "Order placed successfully.",
            order_id=order.order_id,
            total=total,
        )

    # ------------------------------------------------------------------
    # Algorithm F — Book management (administrator only)
    # ------------------------------------------------------------------
    def require_admin(self) -> Result | None:
        user = self.current_user()
        if user is None or user.role != "admin":
            return Result(False, "Administrator access is required.")
        return None

    def add_book(
        self,
        title: str,
        author: str,
        description: str,
        category: str,
        price: int,
        is_free: bool,
        cover: str,
        pdf: str,
    ) -> Result:
        denied = self.require_admin()
        if denied:
            return denied
        title, author = title.strip(), author.strip()
        if not title or not author:
            return Result(False, "Title and author are required.")
        book = Book(
            book_id=self.next_book_id,
            title=title,
            author=author,
            description=description.strip(),
            category=category.strip() or "Uncategorised",
            price=0 if is_free else max(0, int(price)),
            is_free=is_free,
            cover=cover.strip(),
            pdf=pdf.strip(),
        )
        self.books.append(book)
        self.next_book_id += 1
        return Result(True, f'"{book.title}" added to the catalogue.')

    def edit_book(self, book_id: int, **changes: object) -> Result:
        denied = self.require_admin()
        if denied:
            return denied
        book = self.find_book(book_id)
        if book is None:
            return Result(False, "Book not found.")
        for key, value in changes.items():
            if hasattr(book, key):
                setattr(book, key, value)
        book.title = book.title.strip()
        book.author = book.author.strip()
        if not book.title or not book.author:
            return Result(False, "Title and author are required.")
        if book.is_free:
            book.price = 0
        return Result(True, "Book updated.")

    def delete_book(self, book_id: int) -> Result:
        denied = self.require_admin()
        if denied:
            return denied
        book = self.find_book(book_id)
        if book is None:
            return Result(False, "Book not found.")
        self.books = [b for b in self.books if b.book_id != book_id]
        self.cart = [item for item in self.cart if item.book_id != book_id]
        return Result(True, f'"{book.title}" removed from the catalogue.')

    # ------------------------------------------------------------------
    # Algorithm G — Order management
    # ------------------------------------------------------------------
    def user_orders(self) -> list[Order]:
        user = self.current_user()
        if user is None:
            return []
        return [order for order in reversed(self.orders) if order.user_id == user.user_id]

    def all_orders(self) -> list[Order]:
        denied = self.require_admin()
        if denied:
            return []
        return list(reversed(self.orders))


# ---------------------------------------------------------------------------
# Demonstration of the seven algorithms (run: python academic/main.py)
# ---------------------------------------------------------------------------

def demonstrate() -> None:
    archive = Archive()

    print("LUMINARY ARCHIVES — Python algorithm demonstration")
    print("=" * 60)

    print("\nA. Registration")
    r = archive.register("Ada Reader", "ada@example.com", "lantern")
    print("  ", r.message)
    r = archive.register("Ada Reader", "ada@example.com", "lantern")
    print("   duplicate:", r.message)

    print("\nB. Login")
    archive.logout()
    r = archive.login("ada@example.com", "wrong")
    print("   wrong password:", r.message)
    r = archive.login("ada@example.com", "lantern")
    print("  ", r.message)

    print("\nC. Search  (term = 'prince')")
    hits = archive.search("prince")
    if not hits:
        print("   No books found.")
    for book in hits:
        print(f"   {book.title} — {book.author} [{book.category}]")

    print("\n   Filter: free titles")
    for book in archive.filter_books(price="free"):
        print(f"   FREE  {book.title}")

    print("\nD. Add to cart")
    print("  ", archive.add_to_cart(12).message)  # 48 Laws
    print("  ", archive.add_to_cart(12).message)  # duplicate blocked
    print("  ", archive.add_to_cart(1).message)   # free title blocked
    print(f"   cart total: {format_naira(archive.cart_total())}")

    print("\nE. Checkout")
    r = archive.checkout("Demo Payment")
    print("  ", r.message)
    print(f"   Order ID: {r.order_id}")
    print(f"   Total: {format_naira(r.total or 0)}")

    print("\nG. Order management")
    for order in archive.user_orders():
        titles = ", ".join(item.title for item in order.items)
        print(f"   {order.order_id}  {order.status}  {format_naira(order.total)}  {titles}")

    print("\nF. Admin book management")
    archive.logout()
    archive.login("admin@luminaryarchives.local", "admin123")
    print("  ", archive.add_book(
        "Sample Treatise", "Archive Editor",
        "A demonstration title added by the administrator.",
        "Archive", 1000, False, "", "",
    ).message)
    print("  ", archive.edit_book(13, price=1200).message)
    print("  ", archive.delete_book(13).message)

    print("\nDone. Marketplace algorithms A–G executed without error.")


if __name__ == "__main__":
    demonstrate()
