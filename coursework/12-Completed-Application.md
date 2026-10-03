---
title: 12. Completed Application
project: Luminary Archives
---

# 12. Completed Application

This is the last box on the assignment table: a **fully functional Marketplace E-commerce Application**.

Luminary Archives is that application. It is a book marketplace. It is small on purpose. It is finished when the journeys below can be walked without a crash — in Python, and on the web.

---

## 12.1 What was handed in

| Item                      | Where it lives                                             |
| ------------------------- | ---------------------------------------------------------- |
| Working marketplace (web) | The deployed application linked from the GitHub repository |
| Python vital functions    | `academic/main.py` (480 lines)                             |
| Web screens               | `src/routes/*`                                             |
| Catalogue assets          | `public/assets/covers`, `public/assets/pdf`                |
| This report               | `coursework/` (the Obsidian vault)                         |
| Technology justification  | [[13-Implementation-Record]] — **unchanged**               |
| GitHub repository         | Gate way to a live deployment                              |

GitHub is the **gateway** to the work. It is not the engine. A visitor who opens the repository can read every line the marker asked to see. A visitor who opens the live web link can use the shop. That split is the whole deployment story.

---

## 12.2 Definition of done — buyer

```text
Register
   ↓
Login
   ↓
Browse books
   ↓
Search / filter
   ↓
Open book details
   ↓
Read a free book
   OR
Add a premium book to cart
   ↓
Checkout
   ↓
Confirm simulated payment
   ↓
Receive order confirmation
   ↓
View order history
   ↓
Open purchased book
```

All of these steps exist. Tests for them passed. See [[09-Testing-Evidence]].

---

## 12.3 Definition of done — administrator

```text
Login  (admin@luminaryarchives.local / admin123)
   ↓
Open Admin
   ↓
Add / Edit / Delete books
   ↓
View orders
```

Ordinary buyers do not receive this path.

---

## 12.4 Platforms

| Target in the brief | How this project meets it |
| --- | --- |
| Desktop | Laptop browser; full grid, generous spacing |
| Web (SPA / PWA-style) | Single web application, dark theme, installable where the host allows |
| Mobile | Responsive layout, phone-first demonstration |

Flutter was an allowed alternative. It was not used. Python was.

---

## 12.5 Demo accounts

| Role | Email | Password |
| --- | --- | --- |
| Administrator | `admin@luminaryarchives.local` | `admin123` |
| Buyer | Create one with **Register** | Your choice |

Do not use a password you use anywhere else.

---

## 12.6 Catalogue in the completed build

Twelve titles. Four free (Machiavelli, Sun Tzu, Marcus Aurelius, Dostoevsky). Eight premium. Covers and PDFs as supplied. Details in [[07-System-Design]].

---

## 12.7 What the completed application is not

- Not a real payment processor  
- Not a multi-seller Amazon  
- Not a Flutter rewrite  
- Not a Python file pretending to be a website on GitHub  
- Not unfinished on the journeys the brief named

---

## 12.8 Closing

Knowledge should have a place to live.

Traditional shops stop at the receipt. Luminary Archives was built so that discovery, understanding, acquisition, and access are one motion. SEREIGN names the larger house. This application is the room with the lights on: a dark archive, a gold rule, a cart that does not lie, an order number you can read back, and a Python file that can still explain itself when the browser is closed.

That is the completed marketplace.
