---
title: Luminary Archives Coursework Report Index
project: Luminary Archives
niche: Books
---

# Luminary Archives

## Coursework Report

**A Digital Archive of Books Worth Reading.**

This vault is the complete project report for the Marketplace E-commerce Application assignment (Python / Flet brief; Books niche). It is written so it can be opened in Obsidian, read as GitHub Markdown, or exported to PDF without losing tables or diagrams.

Luminary Archives is the marketplace. SEREIGN is the outer idea: a wider archive of collections, of which this book room is the one that was actually built.

---

## Expected deliverables

| # | Component | This note | What it contains |
| ---: | --- | --- | --- |
| 1 | Feasibility Study | [[01-Feasibility-Study]] | Technical, economic, operational, legal, schedule |
| 2 | Fact-Finding | [[02-Fact-Finding]] | Interviews, questionnaire, observation, document review |
| 3 | System Requirements | [[03-System-Requirements]] | Functional, non-functional, hardware, software |
| 4 | Algorithms | [[04-Algorithms]] | Registration, login, search, cart, checkout, orders, admin |
| 5 | Flowcharts | [[05-Flowcharts]] | Registration/login, search, cart, checkout, order fulfilment, admin |
| 6 | Pseudocode | [[06-Pseudocode]] | Structured English, language-independent |
| 7 | System Design | [[07-System-Design]] | Architecture, ERD, tables, interface design |
| 8 | Source Code | [[08-Source-Code]] | Module map, Python location, React/Vite location |
| 9 | Testing Evidence | [[09-Testing-Evidence]] | Test cases, inputs, expected results, pass/fail |
| 10 | Screenshots | [[10-Screenshots]] | Working screens of the application |
| 11 | User Documentation | [[11-User-Documentation]] | Install, buyer manual, admin manual, FAQ |
| 12 | Completed Application | [[12-Completed-Application]] | What was delivered, demo accounts, platforms |
| — | Implementation Record | [[13-Implementation-Record]] | Why Python, why React, why Vite — left unchanged |

---

## One-line architecture

```text

Python (academic/main.py)     →  the algorithms the assignment asked for

TypeScript store              →  the same algorithms, running in the browser

React screens + Vite          →  the living web archive

GitHub                        →  the repository the lecturer can mark

Web deployment                →  the demonstration GitHub itself cannot render

```

GitHub stores source. It does not execute Python, and it does not present a Flet window. That is why the live marketplace is a web application, and why the Python remains in the repository as the examinable algorithm layer, not as a decoration, as the logic.

---

## Prototype credentials

These are coursework credentials only. They are not production secrets.

| Role | Email | Password |
| --- | --- | --- |
| Administrator | `admin@luminaryarchives.local` | `admin123` |
| Buyer | Register a new account in the app | Chosen at registration |

---

## Statement on scope

The application is an academic prototype and does not implement production-grade authentication, payment security, encryption, DRM, or database security.

Payment is simulated. The catalogue uses the supplied book files. Free titles open without checkout. Premium titles open after a completed order.
