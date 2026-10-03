---
title: 6. Pseudocode
project: Luminary Archives
---

# 6. Pseudocode

The assignment asks for **structured English**, independent of a programming language. This is not Python with the punctuation filed off. It describes *what* each process does so that either Python or the TypeScript store can implement it.

---

## 6.1 Registration

```text
PROCEDURE Register (name, email, password)
    TRIM name and email
    IF name is blank OR email is blank OR password is blank THEN
        RETURN failure "Name, email, and password are required."
    END IF
    IF email does not contain a local part, an @, and a domain with a dot THEN
        RETURN failure "Please enter a valid-looking email address."
    END IF
    IF any existing user has this email THEN
        RETURN failure "An account with this email already exists."
    END IF
    CREATE buyer with the next user number
    APPEND buyer to the user list
    SET the current user to this buyer
    RETURN success "Welcome to Luminary Archives."
END PROCEDURE
```

---

## 6.2 Login

```text
PROCEDURE Login (email, password)
    TRIM and lowercase email
    IF email is blank OR password is blank THEN
        RETURN failure "Email and password are required."
    END IF
    FIND a user whose email and password both match
    IF none found THEN
        RETURN failure "Incorrect email or password."
    END IF
    SET the current user to the one found
    RETURN success greeting
END PROCEDURE
```

---

## 6.3 Search

```text
PROCEDURE Search (term)
    SET needle TO lowercase trimmed term
    SET results TO empty list
    FOR EACH book IN catalogue
        SET haystack TO lowercase (title + author + category)
        IF needle is contained in haystack THEN
            APPEND book TO results
        END IF
    END FOR
    IF results is empty THEN
        DISPLAY "No books found."
    ELSE
        DISPLAY results
    END IF
    RETURN results
END PROCEDURE
```

---

## 6.4 Filter (All / Free / Premium)

```text
PROCEDURE FilterBooks (term, priceFilter, category)
    SET results TO empty list
    FOR EACH book IN catalogue
        IF book fails Search rule for term THEN SKIP
        IF priceFilter is Free AND book is not free THEN SKIP
        IF priceFilter is Premium AND book is free THEN SKIP
        IF category is not All AND book.category differs THEN SKIP
        APPEND book TO results
    END FOR
    RETURN results
END PROCEDURE
```

---

## 6.5 Add to cart

```text
PROCEDURE AddToCart (bookId)
    SET book TO the catalogue entry with this id
    IF book is missing THEN RETURN failure "This book could not be found."
    IF book is not available THEN RETURN failure "This title is currently unavailable."
    IF book is free THEN RETURN failure "Free titles can be read without checkout."
    IF current user already owns book THEN RETURN failure "You already have this book in your archive."
    IF cart already contains bookId THEN RETURN failure "This book is already in your cart."
    APPEND one cart line for bookId
    RETURN success with the book title
END PROCEDURE
```

```text
PROCEDURE RemoveFromCart (bookId)
    DROP every cart line whose book id is bookId
END PROCEDURE
```

---

## 6.6 Checkout

```text
PROCEDURE Checkout (paymentMethod)
    IF there is no current user THEN
        RETURN failure "Please sign in to complete checkout."
    END IF
    SET items TO the books currently in the cart
    IF items is empty THEN
        RETURN failure "Your cart is empty."
    END IF
    SET lines TO empty list
    SET total TO 0
    FOR EACH book IN items
        SET price TO 0 if book is free ELSE book.price
        APPEND a line (book id, title, price, quantity 1)
        ADD price TO total
    END FOR
    CREATE order
        id      ← "LA-" followed by a four-digit sequence
        user    ← current user
        date    ← today
        items   ← lines
        total   ← total
        status  ← "Completed"
        payment ← paymentMethod
    APPEND order to the order list
    EMPTY the cart
    INCREMENT the order sequence
    RETURN success with the order id and total
END PROCEDURE
```

---

## 6.7 Order history

```text
PROCEDURE ListOrdersForCurrentUser
    IF there is no current user THEN RETURN empty list
    RETURN every stored order whose user matches the current user,
           newest first
END PROCEDURE
```

```text
PROCEDURE ListAllOrders
    IF current user is not admin THEN RETURN empty list
    RETURN every stored order, newest first
END PROCEDURE
```

---

## 6.8 Book management

```text
PROCEDURE RequireAdmin
    IF current user is missing OR role is not admin THEN
        RETURN failure "Administrator access is required."
    END IF
    RETURN ok
END PROCEDURE

PROCEDURE AddBook (title, author, description, category, price, isFree, cover, pdf)
    IF RequireAdmin failed THEN RETURN that failure
    IF title or author is blank THEN RETURN failure "Title and author are required."
    CREATE book with the next book number
    IF isFree THEN SET price TO 0
    APPEND book to the catalogue
    RETURN success
END PROCEDURE

PROCEDURE EditBook (bookId, changes)
    IF RequireAdmin failed THEN RETURN that failure
    FIND the book
    IF missing THEN RETURN failure "Book not found."
    APPLY changes
    IF title or author became blank THEN RETURN failure
    IF book is free THEN SET price TO 0
    RETURN success "Book updated."
END PROCEDURE

PROCEDURE DeleteBook (bookId)
    IF RequireAdmin failed THEN RETURN that failure
    FIND the book
    IF missing THEN RETURN failure "Book not found."
    DROP it from the catalogue
    DROP it from the cart
    RETURN success
END PROCEDURE
```

---

## 6.9 Ownership (access after acquisition)

```text
PROCEDURE OwnsBook (bookId)
    SET book TO catalogue entry
    IF book is free THEN RETURN true
    IF there is no current user THEN RETURN false
    IF any of the user's completed orders contains bookId THEN RETURN true
    RETURN false
END PROCEDURE
```

That last procedure is the quiet hinge of the whole archive: a free book is already a light you may sit down with; a premium book becomes one only after Algorithm E has run.
