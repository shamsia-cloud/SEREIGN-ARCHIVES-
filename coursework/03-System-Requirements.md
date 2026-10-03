---
title: 3. System Requirements
project: Luminary Archives
---

# 3. System Requirements Specification (SRS)

**System:** Luminary Archives  
**Niche:** Books  
**Roles:** Buyer, Administrator  
**Prototype status:** Academic. Not a production shop.

This SRS states what the system **must do** (functional) and how well it **must behave** (non-functional), plus the hardware and software it assumes. It is the formal writing of [[02-Fact-Finding]] and the assignment brief.

---

## 3.1 Purpose

To provide a single digital marketplace where:

- a **buyer** can register, log in, browse and search books, read free titles, cart and purchase premium titles (simulated payment), view orders, and open owned books
- an **administrator** can log in, manage the catalogue (add, edit, delete), and view orders

The philosophical frame is unchanged: the book is a container of ideas, not only a SKU. The process the software must make continuous is:

> Discovery → Understanding → Acquisition → Access

---

## 3.2 Scope

**In scope**

Authentication, catalogue, search, filters, book details, free reading, cart, checkout, simulated payment, order history, purchased access, simple admin, responsive web UI, Python algorithm layer.

**Out of scope**

Real payment gateways, password hashing infrastructure, cloud databases, reviews, ratings, recommendations, AI, chat, blockchain, multi-seller CMS, DRM, Flutter as a second codebase.

---

## 3.3 Users

| Actor | Description |
| --- | --- |
| Guest | May browse. Must register or log in to check out. |
| Buyer | Registered user with role `buyer`. |
| Administrator | Predefined account with role `admin`. May also use buyer features. |

Prototype administrator:

```text
Email:    admin@luminaryarchives.local
Password: admin123
```

Coursework credentials only.

---

## 3.4 Functional requirements

Each requirement is numbered so tests in [[09-Testing-Evidence]] can point at it.

### Authentication

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-01 | The system shall allow a guest to register with name, email, and password. | Must |
| FR-02 | Registration shall reject empty fields, a non-email string, and an email that already exists. | Must |
| FR-03 | Successful registration shall create a buyer and sign that buyer in. | Must |
| FR-04 | The system shall log a user in when email and password match a stored account. | Must |
| FR-05 | Failed login shall show a clear error and shall not reveal a stack trace. | Must |
| FR-06 | A signed-in user shall be able to log out from the account area. | Must |

### Catalogue, search, details

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-07 | The system shall display a catalogue of books (cover, title, author, price or FREE). | Must |
| FR-08 | Search shall match title, author, or category, case-insensitive. | Must |
| FR-09 | If search returns nothing, the system shall display **No books found.** | Must |
| FR-10 | The system shall filter by All, Free (`is_free == true`), and Premium (`is_free == false`). | Must |
| FR-11 | Optional category filter shall narrow the catalogue. | Should |
| FR-12 | Opening a book shall show cover, title, author, description, category, price, and free/premium status. | Must |

### Free reading and premium purchase

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-13 | A free book shall offer **Read Book** and shall not require checkout. | Must |
| FR-14 | A premium book shall offer **Add to Cart**. | Must |
| FR-15 | If a PDF is missing, the reader shall show a friendly message rather than crash. | Must |
| FR-16 | If a cover is missing, a placeholder shall be used. | Must |

### Cart

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-17 | Adding a premium available book shall place it in the cart. | Must |
| FR-18 | Adding a title already in the cart shall not duplicate it; a message shall be shown. | Must |
| FR-19 | A cart line shall be removable. | Must |
| FR-20 | The cart shall show each title, its price, and a total. | Must |
| FR-21 | An empty cart shall display **Your cart is empty.** | Must |
| FR-22 | Quantity is one per title (digital goods). | Must |

### Checkout and orders

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-23 | Checkout shall be blocked when the cart is empty or the user is not signed in. | Must |
| FR-24 | Checkout shall show customer information, items, total, and a payment method. | Must |
| FR-25 | Payment method shall be simulated: Card, Bank Transfer, or Demo Payment. | Must |
| FR-26 | Confirming an order shall create an order, assign an ID of the form `LA-0001`, store it, clear the cart, and show confirmation. | Must |
| FR-27 | A new order shall have status **Completed**. | Must |
| FR-28 | A buyer shall view their own orders: ID, date, items, total, status. | Must |
| FR-29 | After purchase, the buyer shall be able to **Read** / open the book. | Must |

### Administration

| ID | Requirement | Priority |
| --- | --- | --- |
| FR-30 | Admin navigation shall appear only for an administrator. | Must |
| FR-31 | An administrator shall add a book (title, author, description, category, price, free/premium, cover path, PDF path). | Must |
| FR-32 | An administrator shall edit an existing book. | Must |
| FR-33 | An administrator shall delete a book from the catalogue. | Must |
| FR-34 | An administrator shall view existing orders. | Must |
| FR-35 | A buyer shall not perform catalogue mutations. | Must |

---

## 3.5 Non-functional requirements

| ID | Quality | Requirement |
| --- | --- | --- |
| NFR-01 | Usability | Buttons labelled; errors in ordinary language; consistent navigation (Home, Browse, Cart, Orders, Account, Admin). |
| NFR-02 | Usability | Sufficient contrast on a dark (obsidian) ground with ivory text and muted gold accent. |
| NFR-03 | Responsiveness | Usable at mobile, tablet, and desktop widths. No horizontal overflow on a phone. Controls large enough to tap. |
| NFR-04 | Reliability | Ordinary mistakes (empty search, bad login, empty cart, missing file) shall not crash the application. |
| NFR-05 | Performance | No continuous animation, no unnecessary libraries, no background polling. |
| NFR-06 | Security (prototype) | Validate registration and login; hide admin from buyers; do not claim production security. |
| NFR-07 | Maintainability | Marketplace logic lives in a small Python file and a small TypeScript store, not in a forest of services. |
| NFR-08 | Availability (demo) | The web demonstration can be opened from a repository-linked deployment without installing Python on the examiner’s machine. |
| NFR-09 | Portability | Demonstration targets Web; the same responsive UI covers desktop and mobile browsers. |
| NFR-10 | Accessibility | Text is readable; interactive elements are obvious; labels exist on form controls. |

---

## 3.6 Hardware requirements (prototype)

| Item | Minimum for demonstration |
| --- | --- |
| Device | A laptop or a smartphone with a modern browser |
| Display | From ~390px wide (phone) upward |
| Input | Keyboard and mouse, or touch |
| Network | Needed only to load the web demonstration and its assets |
| Server hardware | None for the in-memory prototype. No dedicated database machine. |

The assignment’s “desktop / web / mobile” target is met by **one web codebase** that runs in those browsers, not by three native binaries.

---

## 3.7 Software requirements

| Item | Requirement |
| --- | --- |
| Python (algorithm layer) | Python 3.10+ — standard library only. File: `academic/main.py`. |
| Browser (live app) | Current Chrome, Firefox, Safari, or Edge. |
| Node / Vite (to build the web client) | Used to compile and serve the React interface. |
| Git | To hold the GitHub repository the brief/lecturer requires. |
| Operating system | Windows, Linux, or macOS — the app does not depend on one. |

Not required: PostgreSQL, Firebase, Supabase, Paystack, Flutterwave, Stripe, Docker, a Flet runtime on the examiner’s PC.

---

## 3.8 Interface requirements (summary)

A full layout discussion is in [[07-System-Design]]. The destinations the software must provide:

| Screen | Actor | Purpose |
| --- | --- | --- |
| Home | All | Brand, search, featured / free / premium |
| Browse | All | Search, filters, grid |
| Book details | All | Understanding before acquisition |
| Reader | Buyer (free or owned) | Access |
| Cart | Buyer | Review and remove |
| Checkout | Buyer | Simulated payment |
| Orders | Buyer | History |
| Account | Buyer / Admin | Identity, logout, owned books |
| Login / Register | Guest | Authentication |
| Admin | Admin only | Catalogue and all orders |

---

## 3.9 Assumptions and dependencies

1. The supplied covers and PDFs remain in `assets/` (academic Python) and `public/assets/` (web client).  
2. Currency display is Nigerian Naira (₦), as in the specification’s confirmation example.  
3. Digital books have quantity 1.  
4. SEREIGN names the outer archive concept; Luminary Archives is the implemented marketplace.

---

## 3.10 Requirement trace to algorithms

| Functions in the brief | Algorithm note | Code |
| --- | --- | --- |
| Registration, login | [[04-Algorithms]] A, B | `academic/main.py` → `register`, `login` |
| Cart | Algorithm D | `add_to_cart` |
| Checkout | Algorithm E | `checkout` |
| Order update / history | Algorithm G | `user_orders` |
| Product management | Algorithm F | `add_book`, `edit_book`, `delete_book` |
| Search (needed by FR-08) | Algorithm C | `search` |
