---
title: 8. Source Code
project: Luminary Archives
---

# 8. Source Code

The assignment asks for a complete, working codebase organised by module. This note is the **map**. The files themselves live in the GitHub repository. Python is not a comment in a README. It is a runnable module.

The technology *why* is in [[13-Implementation-Record]] and is not repeated here as an argument. This page only says **what sits where**.

---

## 8.1 Tree

```text
luminary-archives/
│
├── academic/
│   ├── main.py                 Python algorithms A–G  (480 lines)
│   └── requirements.txt        empty — standard library only
│
├── src/
│   ├── lib/
│   │   ├── catalogue.ts        seed books + admin account
│   │   ├── store.ts            live translation of the Python
│   │   ├── types.ts            User, Book, CartItem, Order
│   │   └── utils.ts            email check, ₦, dates
│   ├── routes/                 one module per screen
│   └── components/             shell, cards, cover, fields
│
├── public/assets/
│   ├── covers/                 book covers
│   └── pdf/                    book files
│
├── coursework/                 this report (Obsidian vault)
├── docs/Luminary_Archives_Implementation_Record.md
├── package.json
└── vite.config.ts              web bundler — not business logic
```

---

## 8.2 Modules and responsibilities

### Python — the vital functions

| Module | File | Lines | Responsibility |
| --- | --- | ---: | --- |
| Data model | `academic/main.py` | ~90 | `User`, `Book`, `Order`, `OrderItem`, `CartItem` |
| Catalogue seed | same file | ~55 | Twelve titles, admin account |
| Archive helpers | same file | ~55 | Current user, totals, ownership |
| Algorithm A | `Archive.register` | ~20 | Registration |
| Algorithm B | `Archive.login` | ~15 | Login |
| Algorithm C | `Archive.search` / `filter_books` | ~30 | Search and filters |
| Algorithm D | `Archive.add_to_cart` | ~20 | Cart integrity |
| Algorithm E | `Archive.checkout` | ~30 | Order creation |
| Algorithm F | `add_book` / `edit_book` / `delete_book` | ~55 | Admin catalogue |
| Algorithm G | `user_orders` / `all_orders` | ~15 | Order lists |
| Demonstration | `demonstrate()` | ~70 | Runnable evidence of A–G |

**Total application Python: 480 lines, one file.**  
Run:

```bash
python academic/main.py
```

That command walks registration (including the duplicate-email failure), login (including a wrong password), search for `prince`, free filter, cart duplicate block, checkout to `LA-0001`, order listing, and admin add/edit/delete.

Python is the examinable heart. Users, books, cart lines, and orders are decided here in the language the assignment named.

### TypeScript store — the same heart, beating in the browser

| File | Lines | Responsibility |
| --- | ---: | --- |
| `src/lib/store.ts` | 260 | register, login, search helpers, cart, checkout, admin |
| `src/lib/catalogue.ts` | 170 | `INITIAL_BOOKS`, `ADMIN_ACCOUNT` |
| `src/lib/types.ts` | 45 | typed records |
| `src/lib/utils.ts` | 27 | `isValidEmail`, `formatNaira` |

The web application **does not import** `academic/main.py`. GitHub Pages and a static web host cannot execute that file. The store is a line-by-line cousin: same messages, same `LA-0001` padding, same “one title, one line” cart, same admin email.

### React screens — the rooms of the archive

| File | Lines | Screen |
| --- | ---: | --- |
| `src/routes/index.tsx` | 120 | Home |
| `src/routes/browse.tsx` | 104 | Catalogue / search / filter |
| `src/routes/book.$bookId.tsx` | 115 | Details |
| `src/routes/reader.$bookId.tsx` | 88 | Read / Open Book |
| `src/routes/cart.tsx` | 98 | Cart |
| `src/routes/checkout.tsx` | 162 | Checkout + confirmation |
| `src/routes/orders.tsx` | 83 | Order history |
| `src/routes/account.tsx` | 114 | Account / logout / owned books |
| `src/routes/login.tsx` | 108 | Login |
| `src/routes/register.tsx` | 97 | Registration |
| `src/routes/admin.tsx` | 304 | Catalogue management + all orders |
| `src/routes/__root.tsx` | 52 | Document shell |
| **Routes total** | **1,445** | |
| Components (shell, card, cover, fields) | ~360 | Shared chrome |

Vite (`vite.config.ts`) compiles this tree and serves `public/assets`. It does not decide prices.

---

## 8.3 Why the code is organised this way

The brief asked, where possible, for **one codebase** that can be shown on desktop, web, and mobile. The web client is that codebase: one set of screens, three classes of browser.

The brief also asked for **Python**. A web host will not run a Flet window from a GitHub link. So Python is organised as its own module — complete, standard-library, examinable — instead of being stretched into a server the assignment told us not to build.

That is organisation, not apology.

---

## 8.4 How to read the source in an oral defence

1. Open `academic/main.py`. Point at `register`, `login`, `search`, `add_to_cart`, `checkout`, `add_book`, `user_orders`.  
2. Open `src/lib/store.ts`. Show the same names in TypeScript.  
3. Open the matching route (for example `checkout.tsx`) and show the screen that calls it.  
4. Run `python academic/main.py` for a text proof.  
5. Open the web application for a visual proof.

Two proofs, one marketplace.
