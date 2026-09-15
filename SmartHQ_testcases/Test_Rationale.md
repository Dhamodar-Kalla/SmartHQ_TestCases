# Test Rationale – Parts & Accessory Lookup

## Client Question
> "What is the reason for these test cases?"

## Purpose
The Parts & Accessory Lookup flow is a **customer- and distributor-facing feature**. It lets
users move from the SmartHQ Home page into Parts resources — schematic diagrams, distributor
login, Customer Net, and accessory lookup. Because this flow connects the app to **external
systems** (`geappliancescustomernet.com`, distributor websites, and product data), any breakage
directly impacts the ability to identify, order, and service parts.

## Why We Test This Flow

| # | Reason | Risk if Untested |
|---|--------|------------------|
| 1 | **Navigation integrity** – Parts links must appear and route correctly | Users can't reach parts resources at all |
| 2 | **External redirects** – My Distributor must open the correct Customer Net login URL | Broken/incorrect link erodes trust and blocks distributor access |
| 3 | **Access control** – Customer Net requires a distributor code | Unauthorized access or blocked legitimate users |
| 4 | **Data accuracy** – Accessory Lookup must return correct product details | Wrong part ordered → cost, delays, customer dissatisfaction |
| 5 | **Negative handling** – Invalid codes/IDs must show clear errors | Confusing UX, support tickets, abandoned tasks |

## Reasoning Behind the Test Design
- **End-to-end coverage:** Each user-visible step in the flow has a matching test, so a
  regression anywhere in the chain is caught.
- **Positive + negative cases:** We validate both correct inputs (valid code, valid Model/
  Product/PIM ID) and incorrect ones (invalid, empty) to confirm graceful error handling.
- **Manual + automated parity:** Manual cases (TC-01→TC-09) give traceable, auditable
  documentation for the client; the Appium script provides fast, repeatable regression runs.
- **External-dependency focus:** Special attention is given to redirects and distributor
  code entry, since these are the highest-risk integration points.

## Business Value to the Client
- Confidence that parts/accessory discovery works reliably before each release.
- Reduced support load from broken links or misleading lookups.
- A documented, repeatable QA baseline that scales as the feature evolves.
