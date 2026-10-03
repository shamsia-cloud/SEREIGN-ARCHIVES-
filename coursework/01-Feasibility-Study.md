---
title: 1. Feasibility Study
project: Luminary Archives
---

# 1. Feasibility Study

**Project:** Luminary Archives  
**Type:** Digital book marketplace / e-commerce prototype  
**Niche:** Books  
**Question asked:** Is this project practical to attempt, to finish, and to demonstrate within the coursework window?

A feasibility study is not a hope. It is a decision. The decision here is: **yes, with a deliberately small design.**

The assignment asks for a marketplace that buyers and sellers can share: list, search, purchase, and manage. It names Python (or Flutter) as the development path, and it asks that one codebase be capable of desktop, web, and mobile demonstration. It also asks for a full report — feasibility, facts, requirements, algorithms, flowcharts, pseudocode, design, code, tests, screenshots, and a user manual.

That is a large envelope. The only way it is practical is if the *product* stays small while the *documentation* stays complete.

---

## 1.1 Technical feasibility

### Available technology

| Layer | Choice | Why it is feasible |
| --- | --- | --- |
| Marketplace algorithms | Python 3, standard library, one file (`academic/main.py`) | Matches the Python requirement. No packages to install. An examiner can read and run Algorithms A–G directly. |
| Live interface | React screens, TypeScript store, Vite bundler | Satisfies the **web** demonstration, SPA/PWA-style delivery, and responsive mobile layout from a single codebase. |
| Data | In-memory lists (users, books, cart, orders), optional browser persistence | No database server is required for the prototype. The relational model is designed on paper for the report. |
| Assets | Local covers and PDFs | Reading can be demonstrated without a CDN or DRM system. |
| Admin | A single predefined administrator account | Product management is demonstrable without a multi-tenant seller platform. |

### Skills required versus skills used

| Skill | Required by the brief | Used in this project | Feasible? |
| --- | --- | --- | --- |
| Python procedural logic | Yes | Yes — registration, login, search, cart, checkout, catalogue, orders | Yes |
| Structured documentation | Yes | Yes — this vault | Yes |
| Web user interface | Yes (web target) | Yes — React / Vite | Yes |
| Flutter | Optional alternative | Not used (Python path was chosen) | Not needed |
| Flet desktop window | Named in the brief | Not the live demonstration host | Accepted trade-off (see below) |
| Real payment APIs | Not required for a prototype | Simulated checkout only | Yes |
| Cloud database | Not required | Not used | Yes |

### The Flet / GitHub problem (stated plainly)

The brief is titled *Python / Flet app*. Flet can draw a UI from Python. That is technically valid.

Two demonstration constraints made a pure Flet window the wrong *delivery* choice:

1. **GitHub does not run Python.** A repository link shows source. It does not open a Flet application. The lecturer asked for a GitHub link. A link that cannot be clicked into a working marketplace would fail the “completed application” demonstration.
2. **The brief also requires Web, and a responsive mobile layout.** A static web client, with the same algorithms translated into the running store, can be opened on desktop and on a phone without installing Python.

So the feasible design is a **split that still honours Python**:

- Python holds the algorithms (the vital functions: users, catalogue, cart, orders).
- The web client presents those same functions so the project can actually be marked as a working marketplace.

This is technically feasible because the two layers implement the same steps, the same validations, and the same order-ID format. They are one marketplace, two readings of it.

### Technical risks and treatments

| Risk | Treatment |
| --- | --- |
| Missing PDF or cover crashes the app | Fail gracefully; placeholder cover; disable or message the reader |
| Browser cannot embed a PDF | Provide an Open Book action to the asset |
| Duplicate cart lines | One copy per title |
| Empty checkout | Blocked with a readable message |
| Ordinary user reaches admin | Admin navigation is hidden unless role is administrator |
| Scope explosion (reviews, AI, wallets) | Explicitly out of scope |

**Verdict — technical:** Feasible.

---

## 1.2 Economic feasibility

This is a student prototype, not a shop that must break even.

| Item | Cost to the project | Note |
| --- | --- | --- |
| Python | None | Standard library |
| React / Vite toolchain | None at student scale | Development tooling, not a licence fee |
| Hosting the repository | None | GitHub academic use |
| Hosting the live demo | None at student scale | Web static/app hosting for demonstration |
| Real payment gateway | Avoided | Simulated Card / Bank Transfer / Demo Payment |
| Book stock | Already supplied | Covers and PDFs were provided with the project |
| Database hosting | Avoided | In-memory prototype |
| Designer / extra developers | None | Single student project |

**Benefits (academic, not commercial)**

- A complete coursework trail: facts → requirements → algorithms → code → tests.
- A demonstrable buyer journey and a demonstrable admin journey.
- A portfolio artefact: a dark literary marketplace rather than a generic product grid.

**Cost–benefit:** The cost is time and attention. The benefit is a markable system. No cash outlay is required to make the prototype work. A production shop would later pay for real payments, hashing, and a database — that is *future* cost, not this semester’s cost.

**Verdict — economic:** Feasible.

---

## 1.3 Operational feasibility

Will people actually use a system this small?

| Stakeholder | What they need | What the prototype gives | Accepted? |
| --- | --- | --- | --- |
| Student buyer | Find a book, read a free one, buy a premium one, see the order | Home, Browse, Details, Reader, Cart, Checkout, Orders | Yes, for a demo |
| Administrator / seller | Add, edit, delete titles; see orders | Admin catalogue + order list | Yes, kept intentionally simple |
| Examiner | Trace algorithms to code to screens | Python file + web screens + this report | Yes |
| General public | A real bookstore | Not this project | Out of scope |

Operationally the system is a **two-role archive**. That is enough. A multi-seller dashboard, reviews, and recommendations would make the operation heavier than the assignment.

User acceptance in the fact-finding sample favoured:

- a catalogue that can be searched
- a clear free / premium split
- a cart that does not duplicate
- a checkout that finishes
- a way to open the book afterwards

All of those are in the build. The prototype does **not** claim production login security. That honesty is itself an operational requirement: users of a coursework demo should not be told their passwords are fortress-grade.

**Verdict — operational:** Feasible.

---

## 1.4 Legal feasibility

| Question | Position taken |
| --- | --- |
| Are we a real shop taking real money? | No. Payment is simulated. |
| Are user passwords production-safe? | No. Prototype storage. Documented as such. |
| Can we ship the supplied PDFs in a student demo? | They were provided as project assets for the coursework build. The report does not claim commercial republication rights. |
| Data protection | No cloud database of strangers. Demo accounts live in prototype storage. |
| Accessibility of claims | The app does not claim to be a bank, a publisher, or a licensed library. |
| Compliance with the brief | Python algorithms, marketplace features, documentation pack — present. |

Legal feasibility for a **coursework prototype** is a matter of not over-claiming. The required sentence is therefore part of the product, not a footnote:

> The application is an academic prototype and does not implement production-grade authentication, payment security, encryption, DRM, or database security.

**Verdict — legal:** Feasible, as a prototype.

---

## 1.5 Schedule feasibility

The brief is a semester artefact, not a startup roadmap. The implementation order was fixed so that polish could not eat the marketplace:

1. Application shell  
2. Book data  
3. Catalogue  
4. Login / registration  
5. Book details  
6. Search / filter  
7. Cart  
8. Checkout  
9. Orders  
10. Admin  
11. PDF access  
12. Visual polish  
13. Testing and report  

That order is feasible because each step is a closed function. Search does not wait for a recommendation engine. Checkout does not wait for Paystack.

Documentation (this vault) is scheduled as a pack that maps one-to-one onto the twelve expected deliverables, so the report cannot “forget” a heading the marking scheme contains.

**Verdict — schedule:** Feasible if scope stays small. Scope stayed small.

---

## 1.6 Feasibility summary

| Dimension | Result | One-sentence finding |
| --- | --- | --- |
| Technical | **Go** | Python can express the marketplace; the web client can demonstrate it. |
| Economic | **Go** | No paid gateways, no paid database, supplied assets. |
| Operational | **Go** | Two roles, one catalogue, one cart, one checkout. |
| Legal | **Go (prototype)** | Simulated payment; documented security limits. |
| Schedule | **Go** | Priority list respected; no extra architecture. |

**Overall decision:** Proceed with Luminary Archives as a **small, complete, documented book marketplace** — Python for the vital functions, a web client for the living archive, GitHub for the source the lecturer asked to see.
