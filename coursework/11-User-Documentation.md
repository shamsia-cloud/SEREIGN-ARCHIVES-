---
title: 11. User Documentation
project: Luminary Archives
---

# 11. User Documentation

**Product:** Luminary Archives  
**Tagline:** A Digital Archive of Books Worth Reading.

This manual is for three readers: whoever is installing the project for marking, the buyer, and the administrator. It is short on purpose.

---

## 11.1 Installation guide

### What you need

- Python 3.10 or newer, if you want to run the algorithm file  
- A current browser, if you want to use the marketplace  
- The GitHub repository (this project)

GitHub will show you the source. GitHub will **not** run Python and will **not** open the shop. That is why a web demonstration is linked from the repository when one has been deployed.

### A. Run the Python algorithms (the assignment’s language)

```bash
python academic/main.py
```

There is nothing to `pip install`. `academic/requirements.txt` is empty on purpose.

You should see registration, a duplicate-email error, login, search for `prince`, a cart that refuses duplicates, checkout to `LA-0001`, and an admin add/edit/delete.

### B. Use the web marketplace

Open the deployed web application from the repository’s demonstration link.

If you are running the interface locally as a developer:

```bash
npm install
npm run dev
```

Then open the address the toolchain prints. Ordinary markers do not need this step if the live link works.

### C. Desktop, web, mobile

There is one web codebase. Open it:

- in a laptop browser (desktop)
- in a phone browser (mobile)
- as an in-browser application (web / PWA-style)

You do not install three products.

---

## 11.2 Buyer manual

### Register

1. Open **Account** or **Register**.  
2. Enter your name, email, and a password.  
3. Submit.  
4. You are signed in and sent into the archive.

If the email already exists, you will be told. Choose another, or log in instead.

### Log in

1. Open **Login**.  
2. Enter the email and password you registered.  
3. A wrong pair produces **Incorrect email or password.** — not a crash.

### Browse and search

- **Home** is the front hall: featured, free, premium.  
- **Browse** is the full shelf.  
- Type a fragment of a title, an author, or a category. Case does not matter. `prince` finds *The Prince*.  
- Filter **All / Free / Premium**. Optionally pick a category.  
- If nothing matches: **No books found.**

### Understand a book

Open a card. You should see the cover, the author, the description, the category, and either **FREE** or a naira price.

### Read a free book

If the details screen says **Read Book**, press it. There is no cart and no payment. If the file is missing, you will get a calm message, not a frozen page.

### Buy a premium book

1. Press **Add to Cart**.  
2. If it is already there, the cart will not clone it.  
3. Open **Cart**. Remove anything you do not want.  
4. Press **Checkout**. You must be signed in.  
5. Check your name, the lines, and the total.  
6. Choose **Card**, **Bank Transfer**, or **Demo Payment**. None of these charges a real account.  
7. Confirm.  
8. Read the confirmation: order ID (`LA-0001` and upward) and total.

### Orders and access

- **Orders** lists every completed purchase: ID, date, items, total, status.  
- **Account** lists books you may read. Premium titles appear here after checkout. Free titles were always yours to open.

### Log out

From **Account**, log out. The next person on the machine should not inherit your cart.

---

## 11.3 Administrator / seller manual

### Log in as administrator

```text
Email:    admin@luminaryarchives.local
Password: admin123
```

These credentials are for the coursework prototype. They are not production credentials. Change them before any real deployment.

After login, an **Admin** link appears in navigation. Buyers never see it.

### Add a book

1. Open **Admin**.  
2. Fill title and author (required).  
3. Description, category, price.  
4. Mark **Free** if the book should skip checkout (price becomes 0).  
5. Cover path and PDF path, if you have files in `assets`.  
6. Save. The catalogue updates at once.

### Edit a book

Select the title, change the fields, save. The details page and the cards show the new values.

### Delete a book

Select the title and delete. It leaves the catalogue. It also leaves anyone’s cart.

### View orders

The admin screen lists orders as they stand. In this prototype they are **Completed** as soon as checkout succeeds. There is no warehouse queue: these are files, not parcels.

### Availability

Uncheck availability if a title must not be sold. Search and cart will treat it as unavailable rather than crashing.

---

## 11.4 FAQ

**Is this a real shop?**  
No. It is an academic marketplace prototype.

**Will my card be charged?**  
No. Payment is simulated.

**Why is there Python *and* a web interface?**  
Python is the language the assignment named for the vital functions (users, catalogue, cart, orders). GitHub does not run that Python for a visitor. The web interface is how the same archive is demonstrated. See [[13-Implementation-Record]].

**Why not Flutter?**  
The brief allowed Python or Flutter. This project took the Python path.

**I searched something and got nothing.**  
That is success, not failure, if the term is not in title, author, or category. You should see **No books found.**

**I added the same book twice.**  
You should see one line and a message. Digital books do not stack.

**The PDF will not open.**  
The file may be missing. The app should tell you. It should not freeze.

**Can a buyer delete a book?**  
No.

**What is SEREIGN?**  
The outer idea: a wider archive. Luminary Archives is the book marketplace inside that idea.

**Is my password hashed?**  
Not in this prototype. Do not reuse a real password.

---

## 11.5 Troubleshooting

| Symptom | What to do |
| --- | --- |
| Cannot check out | Sign in; put at least one premium book in the cart |
| Admin missing | You are not the admin account |
| Cover is blank | Placeholder should appear; the path may be empty |
| Python command fails | Use Python 3; run from the project root: `python academic/main.py` |
| Repository on GitHub looks like “just files” | That is expected. Open the live web link for the shop; open `academic/main.py` for the algorithms |
