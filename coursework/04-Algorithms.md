---
title: 4. Algorithms
project: Luminary Archives
---

# 4. Algorithms

These algorithms were designed **before** they were typed as Python. Each one states input, processing, decisions, and output. They are the sequence of operations for the core modules named in the assignment: registration, cart, checkout, and order update — plus login, search, and book management, without which a marketplace is not a marketplace.

Python realisation: `academic/main.py` (480 lines).  
Live realisation: `src/lib/store.ts`.

---

## Algorithm A — User registration

**Module:** Authentication  
**Input:** `name`, `email`, `password`  
**Output:** a new buyer session, or an error message

```text
START
INPUT name, email, password
VALIDATE that all three fields are present
IF any field is empty THEN
    DISPLAY "Name, email, and password are required."
    STOP
END IF
VALIDATE that email looks like an email
IF email is not valid THEN
    DISPLAY "Please enter a valid-looking email address."
    STOP
END IF
SEARCH users FOR the same email
IF a user with that email exists THEN
    DISPLAY "An account with this email already exists."
    STOP
END IF
CREATE user with role buyer
STORE user
SET current user to the new user
DISPLAY home / welcome
STOP
```

**Efficiency note:** A linear scan of the in-memory user list is enough for a prototype. A production index on email would replace the scan, not the decisions.

---

## Algorithm B — Login

**Module:** Authentication  
**Input:** `email`, `password`  
**Output:** a session, or an error message

```text
START
INPUT email, password
IF email or password is empty THEN
    DISPLAY "Email and password are required."
    STOP
END IF
SEARCH users FOR matching email AND password
IF no match THEN
    DISPLAY "Incorrect email or password."
    STOP
END IF
SET current user
OPEN home (or the page they were sent from)
STOP
```

---

## Algorithm C — Search and filter

**Module:** Catalogue  
**Input:** search term; optional price filter (`all` / `free` / `premium`); optional category  
**Output:** a list of books, or “No books found.”

```text
START
INPUT search term
CONVERT search term to lowercase
CREATE empty results list
FOR each book in the catalogue
    COMPARE the term with lowercase title, author, and category
    IF the term is found AND the price filter matches AND the category filter matches THEN
        ADD book to results
    END IF
END FOR
IF results is empty THEN
    DISPLAY "No books found."
ELSE
    DISPLAY results
END IF
STOP
```

---

## Algorithm D — Add to cart

**Module:** Cart  
**Input:** selected `book_id`  
**Output:** updated cart, or a reason the book was not added

```text
START
SELECT book
IF book does not exist THEN
    DISPLAY "This book could not be found."
    STOP
END IF
IF book is unavailable THEN
    DISPLAY unavailable message
    STOP
END IF
IF book is free THEN
    DISPLAY "Free titles can be read without checkout."
    STOP
END IF
IF the current user already owns the book THEN
    DISPLAY already-owned message
    STOP
END IF
IF book is already in the cart THEN
    DISPLAY "This book is already in your cart."
    STOP
END IF
ADD book to cart (quantity = 1)
UPDATE cart total
DISPLAY confirmation
STOP
```

Remove is the inverse: drop the matching `book_id` from the cart and refresh the total.

---

## Algorithm E — Checkout

**Module:** Orders  
**Input:** current user, cart, chosen payment method  
**Output:** order confirmation (`LA-00xx`, total, status Completed), or a block message

```text
START
OPEN cart
IF current user is missing THEN
    DISPLAY "Please sign in to complete checkout."
    STOP
END IF
IF cart is empty THEN
    DISPLAY "Your cart is empty."
    STOP
END IF
CALCULATE total from cart lines (free lines contribute 0)
DISPLAY order summary (customer, items, total, payment method)
INPUT confirmation
IF not confirmed THEN
    STOP
END IF
CREATE order
    order_id ← next LA-000n
    user_id  ← current user
    date     ← now
    items    ← cart lines (quantity 1, unit price from the book)
    total    ← calculated total
    status   ← Completed
    payment  ← chosen method
SAVE order
CLEAR cart
DISPLAY "Order placed successfully. Order ID: LA-000n  Total: ₦…"
STOP
```

Payment is simulated. The algorithm records a method; it does not call a bank.

---

## Algorithm F — Book management (administrator)

**Module:** Catalogue administration  
**Input:** admin session; action (add / edit / delete); book fields  
**Output:** updated catalogue, or access denied

```text
START
REQUIRE current user role = admin
IF not admin THEN
    DISPLAY access denied
    STOP
END IF
SELECT action
IF action is ADD THEN
    INPUT title, author, description, category, price, free flag, cover, pdf
    IF title or author is empty THEN
        DISPLAY validation error
    ELSE
        ASSIGN new book_id
        ADD book to catalogue
    END IF
ELSE IF action is EDIT THEN
    SELECT book
    MODIFY fields
    SAVE book
ELSE IF action is DELETE THEN
    SELECT book
    REMOVE book from catalogue
    REMOVE that book from any cart
END IF
DISPLAY updated catalogue
STOP
```

---

## Algorithm G — Order management (order update / history)

**Module:** Orders  
**Input:** current user (buyer or admin)  
**Output:** the orders that person is allowed to see

```text
START
USER OPENS orders
IF no current user THEN
    DISPLAY an empty or sign-in prompt
    STOP
END IF
IF current user is a buyer THEN
    RETRIEVE orders WHERE user_id = current user
ELSE IF current user is admin THEN
    RETRIEVE all orders
END IF
FOR each order
    DISPLAY order ID, date, items, total, status
END FOR
STOP
```

In this prototype an order is born **Completed**. “Order update” is therefore:

- the write that happens inside checkout (status set, cart cleared, ownership granted)
- the read that happens on the Orders screen

There is no separate warehouse step. Digital goods do not ship.

---

## Complexity (honest, for a prototype)

| Algorithm | Dominant work | Why it is acceptable |
| --- | --- | --- |
| A, B | Scan users | Dozens of demo accounts, not millions |
| C | Scan books | Twelve titles in the seed catalogue |
| D, E | Scan cart (tiny) and books | Digital cart is one line per title |
| F | Scan / rewrite the book list | Admin is rare |
| G | Filter orders by user | Linear read of a short list |

If the archive grew, the *decisions* would stay. Only the storage underneath them would change (see the ERD in [[07-System-Design]]).
