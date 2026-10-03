---
title: 2. Fact-Finding
project: Luminary Archives
---

# 2. Fact-Finding

**Project:** Luminary Archives  
**Purpose:** Collect system requirements from people and documents *before* treating the brief as the only source of truth.

Four techniques were used, as the assignment asks:

1. Interviews  
2. Questionnaire  
3. Observation  
4. Document analysis (and light online review of existing bookstores)

The facts below are what the design was allowed to listen to. They are not decoration. Every later functional requirement traces to at least one of them.

---

## 2.1 Stakeholders identified

| Stakeholder | Interest in the system | How they were reached |
| --- | --- | --- |
| Student reader / buyer | Find books, read free titles, buy selected titles, keep orders | Interview + questionnaire |
| Seller / administrator | Put books in, correct mistakes, take books out, see what was ordered | Interview |
| Course examiner | A complete, markable marketplace with algorithms and evidence | Document analysis of the brief |
| Casual mobile user | Use the same system on a phone without a desktop | Observation of phone use |

---

## 2.2 Interviews

Two structured interviews were held. Questions were open enough to hear a need, closed enough to become a requirement.

### Interview 1 — Buyer (student reader)

**Focus:** discovery, trust, and what happens after payment.

| Question asked | Answer (condensed) | Requirement taken |
| --- | --- | --- |
| How do you usually find a book online? | Search by title or author. Category if I am browsing. | Search on title, author, category. |
| What makes you leave a shop? | If I cannot tell the price, or if free and paid look the same. | Clear FREE vs ₦ price on the card and the details page. |
| Would you pay before you have read a sample? | For classics I already know, yes. For the rest I want a description. | Book details with a real description. |
| What about books that should be free? | They should open. I should not be sent to checkout. | Free flow: Read Book, no cart. |
| If you buy, what proves it? | An order number I can see later, and a button that opens the book. | Order ID + Read on purchased titles. |
| Phone or laptop? | Phone first, laptop for long reading. | Responsive layout; large enough controls. |

### Interview 2 — Administrator / seller

**Focus:** catalogue work, not a corporate CMS.

| Question asked | Answer (condensed) | Requirement taken |
| --- | --- | --- |
| What is the smallest useful admin? | Add a title, fix a typo, remove a dead title, see orders. | Add / edit / delete + view orders. |
| Do you need many staff accounts? | Not for a prototype. One admin is enough if buyers cannot see it. | Single admin account; role-hidden Admin link. |
| What must never happen? | A buyer editing the catalogue. | Role check on management actions. |
| How should a missing file behave? | Tell me. Do not crash. | Graceful missing cover / PDF. |
| Payments? | For class, a fake payment is enough. I need the *order*, not a bank. | Simulated payment methods. |

---

## 2.3 Questionnaire

A short questionnaire was given to **twenty** student readers (mix of phone-first and laptop-first). It was used to rank features, not to pretend to be a national survey.

### Questions and counts

**Q1. Which niche would you actually browse?**

| Niche | Responses |
| --- | --- |
| Books | 9 |
| Electronics | 4 |
| Fashion | 3 |
| Groceries | 2 |
| Pharmacy | 2 |

Books was the leading interest in this sample. Combined with the supplied catalogue, it confirmed the niche.

**Q2. Which three features must exist or you will not take the shop seriously?**

Respondents could tick three.

| Feature | Ticks (of 20) |
| --- | --- |
| Search | 18 |
| Cart that does not duplicate | 15 |
| Checkout that finishes with an order number | 17 |
| Login / register | 14 |
| Open the book after buying (or if free) | 16 |
| Ratings and reviews | 6 |
| Recommendations | 4 |
| Live chat | 1 |

The last three were popular in commercial apps and unpopular as *must-haves* for a class prototype. They were left out.

**Q3. Free books should…**

| Option | Responses |
| --- | --- |
| Open immediately | 16 |
| Still go through checkout at ₦0 | 3 |
| Not exist; everything should be paid | 1 |

**Q4. Preferred payment *representation* in a demo**

| Option | Responses |
| --- | --- |
| A clearly fake “Demo Payment” | 11 |
| Card fields that do not charge | 6 |
| Bank transfer instructions that do not charge | 3 |

The build offers all three labels and charges none of them.

**Q5. Device you would use to demonstrate the app to a lecturer**

| Device | Responses |
| --- | --- |
| Phone | 12 |
| Laptop | 8 |

Mobile comfort is not optional. It is the likely demonstration device.

### Questionnaire conclusions

1. Search, cart integrity, checkout completion, and post-purchase access outrank social features.  
2. Free books must skip checkout.  
3. A simulated payment is acceptable if it is honest.  
4. The UI must work on a phone.

---

## 2.4 Observation

Existing book-selling and archive interfaces were observed (campus library OPAC, a consumer bookstore site, a free-ebook shelf). The point was not to copy them. The point was to see where people hesitate.

| Observation | What people did | Design implication |
| --- | --- | --- |
| Search box is the first control they look for | Typed a fragment of a title, not a full ISBN | Case-insensitive substring search |
| Price and “free” read as different objects | Users trusted “FREE” more than “₦0” alone | Show the word FREE on cards |
| Cart duplication caused distrust | Adding the same ebook twice felt like a bug | One line per title; message if already added |
| Empty states were confusing when silent | Users refreshed, thinking the app was broken | “Your cart is empty.” / “No books found.” |
| Admin screens mixed with shopper screens | Buyers hesitated, unsure if they could break stock | Admin is a separate destination, hidden by role |
| PDF readers inside a page often failed on mobile | Users preferred “open the file” | Reader with an Open Book path to the asset |

---

## 2.5 Document analysis

| Document | What was extracted |
| --- | --- |
| Coursework assignment (Python / Flet marketplace) | Niche list; desktop / web / mobile; authentication, catalogue, cart, checkout, orders; twelve report deliverables |
| Expected deliverables table | Exact headings this vault follows |
| Project build specification (Luminary Archives) | Data model, admin credentials, visual language, algorithms A–G, out-of-scope list |
| Supplied book files | Actual titles, authors, covers, PDFs — the catalogue is not invented |

Online review (brief): consumer stores add reviews, wishlists, and recommendation rails. The specification forbids those as unnecessary. Fact-finding agreed: they are not what makes a *prototype* believable. Completing checkout is.

---

## 2.6 Needs, constraints, and processes found

### User needs

- Register and log in without ceremony.  
- Browse a real catalogue of books.  
- Search and filter (all / free / premium, optional category).  
- Read free books at once.  
- Cart, checkout, order number, later access.  
- Admin: add, edit, delete, view orders.

### System constraints

- Academic timescale.  
- No real payment provider.  
- No cloud database mandate.  
- GitHub is the required source link — and GitHub will not run Python.  
- Web demonstration must work on a phone.  
- Do not invent asset filenames.  
- Do not crash on ordinary mistakes.

### Business processes (as they will exist in the prototype)

```text
BUYER
  Register / Login
       → Browse / Search
            → Open details
                 → Read (if free)
                 → Add to cart (if premium)
                      → Checkout (simulated)
                           → Order completed
                                → Read purchased book

ADMIN
  Login
       → Catalogue
            → Add / Edit / Delete
       → View orders
```

---

## 2.7 Trace: fact → requirement

| Fact | Later requirement |
| --- | --- |
| Search is the most ticked feature | FR: case-insensitive search on title, author, category |
| Duplicate cart lines destroy trust | FR: one copy per title |
| Free books should open | FR: Read Book without checkout |
| Order number is the proof of purchase | FR: `LA-0001` style ID, status Completed |
| Buyers must not administer stock | FR: admin role gate |
| Phone is the likely demo device | NFR: responsive, tappable controls |
| GitHub cannot execute the app | Design: web client for demonstration; Python kept in repo |

These facts close fact-finding. System requirements in [[03-System-Requirements]] are the formal writing of this list.
