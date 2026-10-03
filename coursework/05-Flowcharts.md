---
title: 5. Flowcharts
project: Luminary Archives
---

# 5. Flowcharts

Standard symbols used throughout:

| Symbol | Meaning |
| --- | --- |
| Rounded rectangle | Start / End |
| Parallelogram | Input / Output |
| Rectangle | Process |
| Diamond | Decision |
| Arrow | Flow |

Obsidian and GitHub both render the Mermaid diagrams below. They are the pictures of [[04-Algorithms]].

---

## 5.1 Registration and login

The assignment asks for a combined registration/login chart. Registration is the left decision tree; login is the right. Both end on the home screen when they succeed.

```mermaid
flowchart TD
    Start([Start]) --> Choice{Register or log in?}

    Choice -->|Register| InReg[/Input name, email, password/]
    InReg --> ValReq[Validate required fields]
    ValReq --> Empty{All present?}
    Empty -->|No| Err1[/Display: fields required/]
    Err1 --> End1([End])
    Empty -->|Yes| ValEm{Email looks valid?}
    ValEm -->|No| Err2[/Display: invalid email/]
    Err2 --> End2([End])
    ValEm -->|Yes| Dup{Email already exists?}
    Dup -->|Yes| Err3[/Display: duplicate account/]
    Err3 --> End3([End])
    Dup -->|No| Create[Create buyer and set current user]
    Create --> Home1[/Open home screen/]
    Home1 --> EndOk([End])

    Choice -->|Log in| InLog[/Input email, password/]
    InLog --> Find{Matching credentials?}
    Find -->|No| Err4[/Display: incorrect email or password/]
    Err4 --> End4([End])
    Find -->|Yes| SetUser[Set current user]
    SetUser --> Home2[/Open home screen/]
    Home2 --> EndOk
```

---

## 5.2 Book search and browsing

```mermaid
flowchart TD
    Start([Start]) --> In[/Input search term and filters/]
    In --> Lower[Convert term to lowercase]
    Lower --> Loop[Take next book]
    Loop --> Match{Term in title, author, or category AND filters match?}
    Match -->|Yes| Add[Add book to results]
    Add --> More{More books?}
    Match -->|No| More
    More -->|Yes| Loop
    More -->|No| Empty{Results empty?}
    Empty -->|Yes| None[/Display: No books found./]
    Empty -->|No| Show[/Display result grid/]
    None --> End([End])
    Show --> End
```

---

## 5.3 Add to cart

```mermaid
flowchart TD
    Start([Start]) --> Select[/Select book/]
    Select --> Exists{Book exists?}
    Exists -->|No| E1[/Display: not found/]
    Exists -->|Yes| Avail{Available?}
    Avail -->|No| E2[/Display: unavailable/]
    Avail -->|Yes| Free{Is free?}
    Free -->|Yes| E3[/Display: read without checkout/]
    Free -->|No| Owned{Already owned?}
    Owned -->|Yes| E4[/Display: already in archive/]
    Owned -->|No| InCart{Already in cart?}
    InCart -->|Yes| E5[/Display: already in cart/]
    InCart -->|No| Add[Add one line; update total]
    Add --> Ok[/Display confirmation/]
    E1 --> End([End])
    E2 --> End
    E3 --> End
    E4 --> End
    E5 --> End
    Ok --> End
```

---

## 5.4 Checkout

This is the chart the assignment names explicitly.

```mermaid
flowchart TD
    Start([Start]) --> Open[/Open cart/]
    Open --> Signed{User signed in?}
    Signed -->|No| E1[/Display: please sign in/]
    Signed -->|Yes| Empty{Cart empty?}
    Empty -->|Yes| E2[/Display: Your cart is empty./]
    Empty -->|No| Tot[Calculate total]
    Tot --> Sum[/Display customer, items, total, payment method/]
    Sum --> Pay[/Input payment method and confirmation/]
    Pay --> Go{Confirmed?}
    Go -->|No| EndStop([End])
    Go -->|Yes| Make[Create order LA-000n status Completed]
    Make --> Save[Save order]
    Save --> Clear[Clear cart]
    Clear --> Conf[/Display Order placed successfully/]
    Conf --> EndOk([End])
    E1 --> EndStop
    E2 --> EndStop
```

---

## 5.5 Order fulfilment / order management

Digital books do not travel. Fulfilment is: the order is stored as Completed, the cart is empty, and the buyer may open the file.

```mermaid
flowchart TD
    Start([Start]) --> Who{Who is looking?}
    Who -->|Buyer| Mine[Retrieve orders for current user]
    Who -->|Admin| All[Retrieve all orders]
    Who -->|Nobody| Sign[/Prompt to sign in/]
    Mine --> Each
    All --> Each[For each order]
    Each --> Show[/Display ID, date, items, total, status/]
    Show --> More{More orders?}
    More -->|Yes| Each
    More -->|No| Read{Buyer opens a purchased title?}
    Read -->|Yes| PDF[/Open PDF or show missing-file message/]
    Read -->|No| End([End])
    PDF --> End
    Sign --> End
```

---

## 5.6 Admin book management

```mermaid
flowchart TD
    Start([Start]) --> Gate{Current user is admin?}
    Gate -->|No| Deny[/Display access denied / hide screen/]
    Deny --> End([End])
    Gate -->|Yes| Act{Which action?}
    Act -->|Add| InAdd[/Input book fields/]
    InAdd --> V1{Title and author present?}
    V1 -->|No| Err[/Display validation error/]
    V1 -->|Yes| Add[Append book with new id]
    Act -->|Edit| PickE[/Select book and modified fields/]
    PickE --> Save[Write changes]
    Act -->|Delete| PickD[/Select book/]
    PickD --> Del[Remove from catalogue and cart]
    Add --> Cat[/Display updated catalogue/]
    Save --> Cat
    Del --> Cat
    Err --> End
    Cat --> End
```

---

## 5.7 Whole-marketplace journey (context)

```mermaid
flowchart LR
    D[Discovery] --> U[Understanding]
    U --> A[Acquisition]
    A --> X[Access]
    D -.-> Browse[Browse / Search]
    U -.-> Details[Book details]
    A -.-> Cart[Cart + Checkout]
    X -.-> Read[Reader / Open Book]
```

That last picture is not a control-flow chart. It is the reason the control-flow charts exist.
