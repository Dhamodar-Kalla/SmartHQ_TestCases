# Manual Test Cases – Parts & Accessory Lookup

**Feature:** SmartHQ Home → Misc Features → Parts → Parts Diagram / My Distributor / Customer Net / Accessories Lookup
**Module:** Parts & Accessory Lookup
**Prerequisite:** SmartHQ app installed and user is on the Home page with the "Misc Features" section visible.

---

## TC-01 – Navigate to Parts landing page

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-01 |
| **Priority** | High |
| **Preconditions** | User is on the Home page; "Misc Features" section is displayed; "Parts" feature is visible |

**Steps:**
1. On the Home page, locate the "Misc Features" section.
2. Tap the **Parts** feature.

**Expected Result:** The Parts landing page opens and displays the links: **Parts Diagram**, **My Distributor**, **Customer Net**, **Accessories Lookup**.

---

## TC-02 – Open Parts Diagram (schematic diagrams)

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-02 |
| **Priority** | High |
| **Preconditions** | User is on the Parts landing page |

**Steps:**
1. Tap the **Parts Diagram** link.

**Expected Result:** Parts-related schematic diagrams open and are viewable by the user.

---

## TC-03 – Open My Distributor (Customer Net login)

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-03 |
| **Priority** | High |
| **Preconditions** | User is on the Parts landing page |

**Steps:**
1. Tap the **My Distributor** link.

**Expected Result:** The browser/WebView navigates to `geappliancescustomernet.com/login` and displays the **GE Appliances Customer Net** page.

---

## TC-04 – Customer Net prompts for distributor code

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-04 |
| **Priority** | High |
| **Preconditions** | User is on the Parts landing page |

**Steps:**
1. Tap the **Customer Net** link.

**Expected Result:** A message **"Contact your parts distributor for the code"** is displayed, and the user is prompted to enter a customer code.

---

## TC-05 – Enter valid customer code → opens distributor website

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-05 |
| **Priority** | High |
| **Preconditions** | User is on the Customer Net code entry screen |

**Steps:**
1. Enter a **valid** customer code.
2. Submit the code.

**Expected Result:** The appropriate distributor website opens.

---

## TC-06 – Customer Net code validation (negative)

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-06 |
| **Priority** | Medium |
| **Preconditions** | User is on the Customer Net code entry screen |

| Step | Input (Customer Code) | Expected Result |
|------|-----------------------|-----------------|
| 6.1 | Invalid code | Error message is shown |
| 6.2 | Empty field | Validation error is shown |

---

## TC-07 – Open Accessories Lookup and prompt for identifier

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-07 |
| **Priority** | High |
| **Preconditions** | User is on the Parts landing page |

**Steps:**
1. Tap the **Accessories Lookup** link.

**Expected Result:** The Accessories Lookup page opens and prompts the user to enter one of: **Model**, **Product**, or **PIM Product ID**.

---

## TC-08 – Accessories Lookup returns product details (positive)

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-08 |
| **Priority** | High |
| **Preconditions** | User is on the Accessories Lookup page |

| Step | Identifier | Input | Expected Result |
|------|------------|-------|-----------------|
| 8.1 | Model | Valid model | Product details are displayed |
| 8.2 | Product | Valid product | Product details are displayed |
| 8.3 | PIM Product ID | Valid PIM ID | Product details are displayed |

---

## TC-09 – Accessories Lookup with invalid input (negative)

| Field | Detail |
|-------|--------|
| **Test Case ID** | TC-09 |
| **Priority** | Medium |
| **Preconditions** | User is on the Accessories Lookup page |

| Step | Identifier | Input | Expected Result |
|------|------------|-------|-----------------|
| 9.1 | Model | Invalid model | "No results" / error message displayed |
| 9.2 | Product | Invalid product | "No results" / error message displayed |
| 9.3 | PIM Product ID | Invalid PIM ID | "No results" / error message displayed |

---

### Notes
- Confirm the exact button/label texts (e.g., "Submit", "Search") and identifiers with the actual SmartHQ app UI.
- The automated equivalent of these cases is in `test_accessory_lookup.py` (Appium + pytest).
