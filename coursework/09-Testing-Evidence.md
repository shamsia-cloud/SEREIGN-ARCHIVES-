---
title: 9. Testing Evidence
project: Luminary Archives
---

# 9. Testing Evidence

Tests were executed against the Python algorithm layer (`python academic/main.py` and the same procedures called directly) and against the live web screens. This table is the assignment’s required form: **input, expected output, pass/fail**.

Legend: **P** = pass.

---

## 9.1 Authentication

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-A1 | Valid registration | name `Ada Reader`, email `ada@example.com`, password `lantern` | Account created; user signed in; welcome message | P |
| T-A2 | Duplicate email | same email as T-A1 | Error: account already exists | P |
| T-A3 | Empty registration | blank name | Validation error: fields required | P |
| T-A4 | Invalid email | `ada-at-archive` | Validation error: valid-looking email | P |
| T-A5 | Valid login | `ada@example.com` / `lantern` | User enters the app | P |
| T-A6 | Wrong password | `ada@example.com` / `wrong` | Error: incorrect email or password | P |
| T-A7 | Unknown email | `nobody@example.com` / `x` | Error: incorrect email or password | P |
| T-A8 | Admin login | `admin@luminaryarchives.local` / `admin123` | Admin session; Admin link visible | P |

---

## 9.2 Catalogue, search, details

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-C1 | Open Browse | — | Books displayed as cards | P |
| T-C2 | Search existing | `prince` | *The Prince* (title match) | P |
| T-C3 | Search by author | `greene` | Greene titles | P |
| T-C4 | Search by category | `philosophy` | Philosophy titles | P |
| T-C5 | Search nonsense | `zzzz-not-a-book` | **No books found.** | P |
| T-C6 | Empty search | blank term | Full catalogue (no crash) | P |
| T-C7 | Free filter | filter = free | Only the four free titles | P |
| T-C8 | Premium filter | filter = premium | Only paid titles | P |
| T-C9 | Open book | click *The Prince* | Details: cover, author, description, FREE, Read Book | P |
| T-C10 | Open premium book | click *The 48 Laws of Power* | Details: price ₦8,000, Add to Cart | P |

---

## 9.3 Cart

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-D1 | Add book | add *48 Laws* | Appears in cart; total ₦8,000 | P |
| T-D2 | Add same book twice | add *48 Laws* again | No duplicate; already-in-cart message | P |
| T-D3 | Add a free book | add *The Prince* | Blocked: read without checkout | P |
| T-D4 | Remove book | remove *48 Laws* | Line gone; total updates | P |
| T-D5 | Empty cart view | cart cleared | **Your cart is empty.** | P |

---

## 9.4 Checkout and orders

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-E1 | Checkout with items | cart has *48 Laws*; method Demo Payment | Order created `LA-0001`; total ₦8,000; status Completed | P |
| T-E2 | Checkout empty cart | empty cart | Blocked: empty-cart message | P |
| T-E3 | Checkout signed out | no session | Blocked: sign in required | P |
| T-E4 | Confirm order | confirm | Cart cleared | P |
| T-E5 | View order | open Orders | Order displayed with ID, date, items, total, status | P |
| T-E6 | Access purchased book | Read on *48 Laws* | Opens (or Open Book to the PDF) | P |
| T-E7 | Access free book | Read on *Meditations* without purchase | Opens | P |

---

## 9.5 Admin

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-F1 | Admin login | admin credentials | Admin screen available | P |
| T-F2 | Add book | *Sample Treatise*, author Archive Editor | Catalogue updates | P |
| T-F3 | Edit book | price 1000 → 1200 | Change appears | P |
| T-F4 | Delete book | delete Sample Treatise | Book removed | P |
| T-F5 | Buyer opens admin | buyer session | Admin hidden / access denied | P |
| T-F6 | Admin views orders | after T-E1 | Order list includes `LA-0001` | P |
| T-F7 | Invalid admin form | blank title | Validation error | P |

---

## 9.6 Resilience

| ID | Test | Input | Expected | Result |
| --- | --- | --- | --- | --- |
| T-R1 | Missing cover | empty / bad path | Placeholder, no crash | P |
| T-R2 | Missing PDF | empty path | Friendly message, no crash | P |
| T-R3 | Unavailable book | `available = false` | Cannot add to cart | P |

---

## 9.7 Python demonstration log (evidence extract)

The following is the output of `python academic/main.py`. It is the algorithm layer signing its own test sheet.

```text
LUMINARY ARCHIVES — Python algorithm demonstration
============================================================

A. Registration
   Welcome to Luminary Archives.
   duplicate: An account with this email already exists.

B. Login
   wrong password: Incorrect email or password.
   Welcome back, Ada.

C. Search  (term = 'prince')
   The Prince — Niccolò Machiavelli [Politics]

   Filter: free titles
   FREE  The Prince
   FREE  The Art of War
   FREE  Meditations
   FREE  White Nights

D. Add to cart
   "The 48 Laws of Power" added to cart.
   This book is already in your cart.
   Free titles can be read without checkout.
   cart total: ₦8,000

E. Checkout
   Order placed successfully.
   Order ID: LA-0001
   Total: ₦8,000

G. Order management
   LA-0001  Completed  ₦8,000  The 48 Laws of Power

F. Admin book management
   "Sample Treatise" added to the catalogue.
   Book updated.
   "Sample Treatise" removed from the catalogue.

Done. Marketplace algorithms A–G executed without error.
```

---

## 9.8 Summary

| Area | Cases | Passed | Failed |
| --- | ---: | ---: | ---: |
| Authentication | 8 | 8 | 0 |
| Catalogue / search | 10 | 10 | 0 |
| Cart | 5 | 5 | 0 |
| Checkout / orders | 7 | 7 | 0 |
| Admin | 7 | 7 | 0 |
| Resilience | 3 | 3 | 0 |
| **Total** | **40** | **40** | **0** |

No case in this sheet produced a traceback to the user.
