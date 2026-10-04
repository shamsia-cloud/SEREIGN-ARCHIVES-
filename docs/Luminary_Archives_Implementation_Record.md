# LUMINARY ARCHIVES

## System Concept, Implementation Record, and Technology Justification

**Project:** Luminary Archives
**Type:** Digital book marketplace / e-commerce prototype
**Niche:** Books
**Document purpose:** To record *where* code lives, *how much* of each language is used, *why* Python is included, and *why* React and Vite are included in the delivered product.

This document is written for the coursework report. It is a factual record of the implementation, not a marketing page.

---

## 1. Purpose of this document

This document answers four questions that the finished product must be able to defend:

1. **What is Luminary Archives, conceptually?**
2. **Where is the Python, how much of it is there, and why does it exist?**
3. **Why were React and Vite included, and what value do they add?**
4. **Given that more than one language is used, what is the project as a whole?**

The original build specification asked for a small Python application, with Flet as the UI framework and a single primary file (`main.py`). The delivered product keeps that Python as the **academic algorithm layer**, and presents the same marketplace through a **React + Vite web application**. Both layers implement the same workflows. They are not two different products.

---

## 2. The central idea

The library illuminates and illustrates digital collections with standard and unique value in content and context. **Luminary Archives** exists to turn the act of finding and acquiring books into an intentional digital experience.

At its core, it is a digital book marketplace and archive where readers can discover books, examine what they contain, purchase selected titles, and access the books they own in one place.

The concept is slightly deeper than “an online bookstore.”

### Knowledge should have a place to live

Traditional marketplaces are designed around transactions:

> find product → buy product → receive product

Luminary Archives treats books differently. The book is not merely a product. It is a container of ideas, experiences, philosophies, histories, and perspectives.

So the application creates a digital environment where:

> **Discovery → Understanding → Acquisition → Access**

becomes one continuous experience.

### Why the name “Luminary”

A luminary traditionally refers to a source of light, and metaphorically to a person or work that provides intellectual illumination.

That fits the purpose of the archive:

- Books illuminate things that were previously unclear.
- Luminary Archives therefore positions itself as a gateway to those sources of illumination.

### What the application actually provides

**For the reader**

- A curated catalogue of books
- Search and categorization
- Individual book information
- Free reading for selected books
- Purchasing for premium books
- A shopping cart
- Checkout
- Simulated payment
- Order history
- Access to purchased books

**For the seller / administrator**

- Book creation
- Book editing
- Book removal
- Availability management
- Order visibility

The philosophical purpose and the technical purpose meet here:

> **Luminary Archives is designed to make valuable written knowledge discoverable, accessible, and manageable through a single digital marketplace.**

### SEREIGN as the outer gateway

SEREIGN Archive makes sense as the outer gateway. SEREIGN is the broader archive / interface. Luminary Archives is the actual book marketplace contained within it. In this coursework build, Luminary Archives is the complete, demonstrable marketplace. SEREIGN remains the conceptual frame: a larger house of collections, of which this book archive is the first inhabited room.

---

## 3. Two layers, one marketplace

The project is intentionally split into **logic** and **presentation**.

```text
READER / ADMINISTRATOR
        │
        ▼
React screens (Home, Browse, Details, Cart, Checkout,
Orders, Account, Admin, Reader)
        │
        ▼
TypeScript store  ────────────  same algorithms  ────────────  Python Archive class
src/lib/store.ts                                           academic/main.py
        │                                                         │
        ▼                                                         ▼
In-memory users / books / cart / orders              In-memory users / books / cart / orders
        │
        ▼
Covers and PDFs in public/assets/
```

| Layer | Language | Role | Does the live web app execute it? |
|---|---|---|---|
| Academic algorithm layer | Python | Encodes Algorithms A–G exactly as specified for the coursework | No — it is a standalone, examinable Python program |
| Live marketplace logic | TypeScript | Translates the same algorithms into the running store | Yes |
| Live interface | React | Screens, navigation, forms, cart badge, reader | Yes |
| Bundler / web toolchain | Vite | Turns the interface into a web application and serves assets | Yes, at build and development time |

This split is the simplest way to satisfy two constraints at once:

- the **coursework specification**, which names Python as the implementation language for the marketplace algorithms
- the **web demonstration**, which must be a responsive, polished browser application that can be opened, clicked, searched, and checked out without installing Python on the examiner’s machine

Python is not a leftover. React is not a substitution that erases Python. They occupy different, named places in the file structure.

---

## 4. File structure

The working project (application + academic Python + assets) is:

```text
luminary-archives/
│
├── academic/
│   ├── main.py                 ← ALL application Python (Algorithms A–G)
│   └── requirements.txt        ← empty on purpose (stdlib only)
│
├── docs/
│   └── Luminary_Archives_Implementation_Record.md   ← this document
│
├── src/
│   ├── lib/
│   │   ├── catalogue.ts        ← book seed data + admin account
│   │   ├── store.ts            ← live translation of the Python algorithms
│   │   ├── types.ts            ← User, Book, Order, CartItem
│   │   └── utils.ts            ← email check, ₦ formatting, dates
│   ├── routes/                 ← one React screen per marketplace destination
│   │   ├── index.tsx           Home
│   │   ├── browse.tsx          Catalogue, search, filters
│   │   ├── book.$bookId.tsx    Book details
│   │   ├── reader.$bookId.tsx  PDF access
│   │   ├── cart.tsx            Cart
│   │   ├── checkout.tsx        Simulated checkout
│   │   ├── orders.tsx          Order history
│   │   ├── account.tsx         Account / logout
│   │   ├── login.tsx           Login
│   │   ├── register.tsx        Registration
│   │   └── admin.tsx           Catalogue management + all orders
│   └── components/             ← cards, shell, cover, form controls
│
├── public/
│   └── assets/
│       ├── covers/             ← book cover images (filenames preserved)
│       └── pdf/                ← book PDFs (filenames preserved)
│
├── package.json
├── vite.config.ts
└── src/styles.css              ← obsidian / ivory / brass visual language
```

The original specification asked for:

```text
main.py
requirements.txt
assets/
```

That shape is preserved in `academic/`. The live web product adds `src/` and `public/` because a browser application cannot be a single Python file and still provide the required responsive interface.

---

## 5. Python — identified inclusion, location, quantity, and reason

### 5.1 Where the Python is

| Item | Location |
|---|---|
| **The only application Python file** | `academic/main.py` |
| Python dependencies | `academic/requirements.txt` (none — standard library only) |
| How to run it | `python academic/main.py` |

There is **no other application Python**. Platform tooling scripts that happen to be written in Python (sprite/map helpers under internal skill folders) are **not** part of Luminary Archives and must not be cited as project source code.

### 5.2 How much Python is used

Measured from the delivered file:

| File | Lines | What those lines are |
|---|---:|---|
| `academic/main.py` | **480** | Data model + Algorithms A–G + demonstration |
| `academic/requirements.txt` | 2 | Comment only; no packages |

Approximate composition of `academic/main.py`:

| Region in `academic/main.py` | Approx. lines | Content |
|---|---:|---|
| Header and data model (`User`, `Book`, `Order`, …) | ~90 | The entities from the specification’s database design |
| Seed catalogue (`INITIAL_BOOKS`, `ADMIN`) | ~55 | The twelve supplied titles and the prototype admin account |
| `Archive` helpers (current user, cart total, ownership) | ~55 | Shared state used by every algorithm |
| **Algorithm A** `register` | ~20 | Validation, duplicate email, create user, log in |
| **Algorithm B** `login` / `logout` | ~15 | Credential search, session, error message |
| **Algorithm C** `search` / `filter_books` | ~30 | Case-insensitive title / author / category match |
| **Algorithm D** `add_to_cart` / `remove_from_cart` | ~20 | Availability, no duplicates, free-book rule |
| **Algorithm E** `checkout` | ~30 | Empty-cart guard, order ID `LA-0001`, clear cart |
| **Algorithm F** `add_book` / `edit_book` / `delete_book` | ~55 | Admin gate + catalogue mutations |
| **Algorithm G** `user_orders` / `all_orders` | ~15 | Orders belonging to the current user; admin list |
| Demonstration `demonstrate()` | ~70 | Runnable walkthrough of A–G for evidence |

**Python is 480 lines, in one file, covering 100% of the specified marketplace algorithms.**

It is deliberately not thousands of lines. The specification’s priority order was: meet the coursework, produce a working application, keep the codebase small. The Python layer obeys that.

### 5.3 How the Python is used

The Python is used as the **authoritative algorithm implementation** for the coursework:

1. It is written in structured Python, not pseudocode pretending to be Python.
2. It uses only lists, dictionaries-as-objects (`dataclass`), functions, and `if` statements — the exact simplicity the specification asked for.
3. It holds in-memory `users`, `books`, `cart`, and `orders`. There is no database server.
4. It can be executed independently of the web interface. Running `python academic/main.py` prints a complete pass through registration, login, search, cart, checkout, orders, and admin add/edit/delete.
5. It is the file an examiner can read line-by-line against Algorithms A–G in the specification.

What the Python is **not**:

- It is not a Flet desktop window.
- It is not the live web UI.
- It does not talk to Paystack, Stripe, or any real payment provider.
- It does not hash passwords. The specification states this is an academic prototype, not production-grade security. The documentation statement required by the specification applies here:

> The application is an academic prototype and does not implement production-grade authentication, payment security, encryption, DRM, or database security.

### 5.4 Why Python is included (reason and value)

| Reason | Value |
|---|---|
| The specification names **Python** as the required implementation language for the marketplace logic | The algorithms exist in the language the assignment asked for, in a single readable file |
| Algorithms A–G are procedural and data-structure-based | Python expresses them with lists, objects, and conditionals — no framework required |
| The specification forbids unnecessary packages | The Python layer has **zero** third-party dependencies |
| The report must show source code that matches the written algorithms and flowcharts | `academic/main.py` is that source: one function per algorithm, named after the specification |
| Logic should be separable from presentation | A buyer workflow can be proven in Python even if the examiner never opens the web UI |
| Future / production design is a relational database, but the prototype must stay in-memory | Python dataclasses map cleanly onto USER, BOOK, ORDER, ORDER_ITEM without introducing PostgreSQL |

Python’s value in this project is **clarity of logic**. It is the layer that can be marked against the algorithms, pseudocode, and flowcharts.

### 5.5 Mapping: specification algorithm → Python → live TypeScript

| Spec algorithm | Python (academic/main.py) | Live TypeScript (src/lib/store.ts) | Screen that calls it |
|---|---|---|---|
| A Registration | `Archive.register` | `useStore.register` | `src/routes/register.tsx` |
| B Login | `Archive.login` | `useStore.login` | `src/routes/login.tsx` |
| C Search | `Archive.search` / `filter_books` | `matchesQuery` / `applyFilters` | `src/routes/browse.tsx`, home search |
| D Add to cart | `Archive.add_to_cart` | `useStore.addToCart` | `src/routes/book.$bookId.tsx`, `cart.tsx` |
| E Checkout | `Archive.checkout` | `useStore.checkout` | `src/routes/checkout.tsx` |
| F Book management | `add_book` / `edit_book` / `delete_book` | `addBook` / `updateBook` / `deleteBook` | `src/routes/admin.tsx` |
| G Order management | `user_orders` / `all_orders` | `userOrders` | `src/routes/orders.tsx`, admin orders |

The two implementations are kept in step: same validations, same error messages, same order-ID format (`LA-0001`), same “one copy per title” cart rule, same admin email `admin@luminaryarchives.local` / password `admin123` (prototype credentials only).

---

## 6. Why React is included — reason and value

React is the **presentation layer** of the live marketplace. It was included for reasons that the Python/Flet specification itself creates, once the demonstration target is a web application.

### 6.1 Reason

The specification requires:

- a functioning **web** application as the primary demonstration
- a UI that is usable on **desktop, tablet, and mobile**
- polished visual language (obsidian, warm white, muted gold, glass cards)
- immediate interface updates after state changes (cart badge, totals, catalogue edits)
- named destinations: Home, Browse, Cart, Orders, Account, Admin
- graceful handling of missing covers and PDFs
- a reader/open-book action for free and purchased titles

Those are interface requirements. Python holds the algorithms. It does not, in this deployment, paint a responsive literary archive in the browser. React does.

Flet was named in the specification as a way to keep frontend and backend in one Python process. That is a valid academic design. The delivered demonstration, however, is a **static-style web application**: HTML, CSS, and JavaScript running in the browser, with assets loaded as web resources. React is the component model that fits that target without introducing Django, Flask, or a separate API — all of which the specification forbids.

### 6.2 Value attribute

| Value | What the user actually gets |
|---|---|
| **Screen-for-screen fidelity to the specification** | Each required destination is one React route, not a pile of unrelated pages |
| **Responsive marketplace** | Book grids collapse from four columns to two to one; navigation remains tappable on a phone |
| **State made visible** | Adding a book to the cart updates the badge in the header on the same tick |
| **Literary interface, simple engine** | The archive looks premium; the logic underneath is still lists and `if` statements |
| **Asset-native reading** | Covers and PDFs are ordinary files under `public/assets/`. React displays them; it does not invent filenames |
| **Role separation in the UI** | The Admin link is rendered only when the current user is an administrator — the specification’s access rule, made visible |
| **No extra backend** | React talks to the in-memory/local store, not to PostgreSQL, Firebase, or a payment SDK |

React’s value is **interface fidelity**. It is how Discovery → Understanding → Acquisition → Access is *shown*, not how it is *decided*.

### 6.3 How much React is used

Application React (screens and visible components), excluding platform helpers:

| Area | Files | Lines (approx.) | Role |
|---|---|---:|---|
| Routes / screens | 12 files in `src/routes/` | 1,445 | Every marketplace destination |
| Visible components | `app-shell`, `book-card`, `book-grid`, `brand-mark`, `cover`, form controls | ~360 | Shared chrome and cards |
| Live logic (TypeScript, not JSX) | `store.ts`, `catalogue.ts`, `types.ts`, `utils.ts` | 502 | Translation of the Python algorithms |

React is therefore the largest *surface*, because a marketplace has many screens. It is not the largest *decision engine*. The decision engine is small, and it exists twice: once in Python (480 lines) and once in TypeScript (`store.ts`, 260 lines).

---

## 7. Why Vite is included — reason and value

Vite is not a marketplace feature. It is the **tool that turns the React application into a web application**.

### 7.1 Reason

A React codebase is a tree of TypeScript modules. Browsers do not run that tree raw. Something must:

- compile TypeScript
- bundle modules
- serve `public/assets/covers/` and `public/assets/pdf/` as stable URLs
- rebuild quickly while the interface is being finished
- produce a production build that can be published as a web app

Vite is that something. It is the standard companion to a React web client in this project. It is not an extra architecture. It replaces what a Flet web build would have done for a Python UI: get the application into a browser.

### 7.2 Value attribute

| Value | Why it matters to Luminary Archives |
|---|---|
| **Web as the demonstration target** | The specification’s primary target is Web. Vite’s whole job is web delivery |
| **Assets treated as web resources** | Covers and PDFs remain files. They are not embedded in Python source, which the specification forbids |
| **Speed of a small codebase** | The application stays lightweight — no heavy image processing, no background workers |
| **Responsive preview** | Desktop and mobile layouts can be checked against the same running app |
| **Static publication path** | The result is a front-end web application, not a Python server that must be hosted |
| **PWA-compatible shell** | Application name *Luminary Archives*, short name *Luminary*, dark theme — as the specification asked, without a hand-built JavaScript PWA layer |

Vite’s value is **delivery**. Without it, the React screens would be source code. With it, they are the working archive.

Vite configuration lives in `vite.config.ts`. It is toolchain, not business logic. No checkout rule, search rule, or admin rule is implemented there.

---

## 8. Other codes — what they are, and what they are not

Once Python, React, and Vite are in place, a small number of other notations appear. They are supporting codes, not a second architecture.

| Code | Where | Why it is there | What it is not |
|---|---|---|---|
| **TypeScript** | `src/lib/*`, `src/routes/*` | Gives the live store a typed User / Book / Order model that matches the Python dataclasses | Not a backend framework |
| **CSS / Tailwind** | `src/styles.css`, class names on components | Implements the specified visual language: obsidian ground, ivory type, brass accent, glass cards | Not a design system product |
| **JSON** | `src/lib/og/site.json` | Brand title “Luminary Archives” | Not a database |
| **JPEG covers** | `public/assets/covers/` | Actual supplied covers; placeholder if missing | Not generated inside Python |
| **PDF files** | `public/assets/pdf/` | Actual supplied books; reader fails gracefully if absent | Not DRM |

Nothing in that list is Django, Flask, FastAPI, Node-as-a-custom-server, a cloud database, a real payment gateway, reviews, ratings, or AI. Those remain out of scope, as specified.

---

## 9. Catalogue actually shipped

The catalogue is the supplied books, not an invented list. Free versus premium is data, not a separate subsystem.

| ID | Title | Author | Status | Price |
|---|---|---|---|---|
| 1 | The Prince | Niccolò Machiavelli | Free | ₦0 |
| 2 | The Art of War | Sun Tzu | Free | ₦0 |
| 3 | Meditations | Marcus Aurelius | Free | ₦0 |
| 4 | White Nights | Fyodor Dostoevsky | Free | ₦0 |
| 5 | The Psychology of Money | Morgan Housel | Premium | ₦4,500 |
| 6 | Mastery | Robert Greene | Premium | ₦6,500 |
| 7 | The Laws of Human Nature | Robert Greene | Premium | ₦7,200 |
| 8 | Ego Is the Enemy | Ryan Holiday | Premium | ₦4,200 |
| 9 | The Art of Thinking Clearly | Rolf Dobelli | Premium | ₦3,800 |
| 10 | The Definitive Book of Body Language | Allan and Barbara Pease | Premium | ₦3,500 |
| 11 | The Daily Laws | Robert Greene | Premium | ₦5,500 |
| 12 | The 48 Laws of Power | Robert Greene | Premium | ₦8,000 |

Seeded in Python at `academic/main.py` (`INITIAL_BOOKS`) and in the live app at `src/lib/catalogue.ts`. Cover and PDF filenames are the supplied asset names, not invented ones.

Prototype administrator (coursework only, not a production credential):

```text
Email:    admin@luminaryarchives.local
Password: admin123
```

---

## 10. Intended relational model (documented, not running)

The prototype stores lists in memory. The production design remains the normalised model required by the specification:

```text
USER (user_id PK, name, email, password, role)
BOOK (book_id PK, title, author, description, category, price, is_free, cover, pdf, available)
ORDER (order_id PK, user_id FK, order_date, total, status)
ORDER_ITEM (order_item_id PK, order_id FK, book_id FK, quantity, unit_price)

USER 1 ───────< ORDER
ORDER 1 ──────< ORDER_ITEM
BOOK 1 ───────< ORDER_ITEM
```

Python dataclasses and TypeScript types are the in-memory form of those tables. They exist so the report can show database design without forcing the prototype onto a server.

---

## 11. Security and payment — scope statement

- Login and registration validate required fields, a well-formed email, and duplicate accounts.
- Ordinary users never see Admin controls.
- Checkout refuses an empty cart and requires a signed-in user.
- Payment is simulated (Card / Bank Transfer / Demo Payment). No Paystack, Flutterwave, Stripe, or wallet connection.
- Passwords are stored as submitted in this prototype. That is acceptable only because the work is academic.

The sentence the specification requires is repeated here without qualification:

> The application is an academic prototype and does not implement production-grade authentication, payment security, encryption, DRM, or database security.

---

## 12. Conclusion — what the project is, once all the codes are admitted

Luminary Archives is a **digital book marketplace whose logic is Python and whose living interface is a React web application built with Vite**.

That sentence is the honest conclusion.

- **Python** (`academic/main.py`, **480 lines**, one file) is included because the coursework asks for Python algorithms, in-memory data, and a small, examinable source. Its value is that Algorithms A–G can be read, run, and marked as Python.
- **React** is included because the demonstration must be a polished, responsive web archive — Home, Browse, Details, Reader, Cart, Checkout, Orders, Account, Admin — updating immediately as the store changes. Its value is that Discovery → Understanding → Acquisition → Access is a continuous *experience*, not a sequence of print statements.
- **Vite** is included because a React tree and a folder of covers and PDFs have to become a web application. Its value is delivery: web-first, asset-honest, no Python server, no forbidden backend.

The other codes (TypeScript types, CSS, JSON, JPEG, PDF) are the grain of that interface. They do not change the architecture.

The specification said: *the project should look more sophisticated than its implementation actually is.* That remains the rule. Under the brass rules and glass cards, the engine is still:

```text
list, dict, function, if statement
```

once in Python, once in TypeScript, presented through React.

Philosophically, the stack is in service of a single claim:

> Knowledge should have a place to live.

SEREIGN is that place conceived as an outer archive. Luminary Archives is the room that is actually built: a catalogue of books worth reading, a cart that does not pretend to be a warehouse, a checkout that teaches the order workflow, and a reading path that treats a free or purchased book as something you open, not merely something you bought.

The project is complete when those two truths are both true:

1. A Python program can register, search, cart, check out, and administer the archive.
2. A person in a browser can do the same thing, with the same books, in a dark literary interface.

They can. That is Luminary Archives.

---

*End of implementation record.*
