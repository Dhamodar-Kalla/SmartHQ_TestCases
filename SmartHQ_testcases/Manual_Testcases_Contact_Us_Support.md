# Manual Test Cases – Contact Us Support Enhancement

**Feature:** SmartHQ Service mobile app → Contact Us
**Module:** Contact Us / Support
**Prerequisite:** SmartHQ Service mobile app is installed, the build containing this enhancement is available, and the user can navigate to the **Contact Us** section.

---

## CU-01 – Contact Us section displays updated support options

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-01 |
| **Priority** | High |
| **Preconditions** | User is on the screen from which the **Contact Us** section can be opened |

**Steps:**
1. Navigate to the **Contact Us** section in the SmartHQ Service mobile app.

**Expected Result:** The page loads successfully and displays both support options: **Call Us** and **Email Us**.

---

## CU-02 – Call Us option displays the correct phone number

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-02 |
| **Priority** | High |
| **Preconditions** | User is on the **Contact Us** section |

**Steps:**
1. Locate the **Call Us** support option.
2. Review the phone number shown in that section.

**Expected Result:** The **Call Us** option is visible with a graphic-style representation and the displayed phone number is **800-792-3395**.

---

## CU-03 – Call Us routes to the correct phone number

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-03 |
| **Priority** | High |
| **Preconditions** | User is on the **Contact Us** section; the device supports phone dialing |

**Steps:**
1. Tap the **Call Us** option.

**Expected Result:** The mobile OS dialer opens with **800-792-3395** prefilled as the destination number.

---

## CU-04 – Email Us option displays the correct support email

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-04 |
| **Priority** | High |
| **Preconditions** | User is on the **Contact Us** section |

**Steps:**
1. Locate the **Email Us** support option.
2. Review the email address shown in that section.

**Expected Result:** The **Email Us** option is visible with a graphic-style representation and the displayed email address is **SmartHQService.Support@geappliances.com**.

---

## CU-05 – Email Us routes to the correct support mailbox

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-05 |
| **Priority** | High |
| **Preconditions** | User is on the **Contact Us** section; the device has an email client configured |

**Steps:**
1. Tap the **Email Us** option.

**Expected Result:** The mobile OS email composer opens with the **To** field populated as **SmartHQService.Support@geappliances.com**.

---

## CU-06 – Hours of operation are displayed correctly

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-06 |
| **Priority** | High |
| **Preconditions** | User is on the **Contact Us** section |

**Steps:**
1. Review the support hours displayed on the page.

**Expected Result:** The page displays **Hours of Operation** as **Monday - Friday 8:30 AM - 5:00 PM EST**.

---

## CU-07 – Contact Us page retains both support channels in the same release

| Field | Detail |
|-------|--------|
| **Test Case ID** | CU-07 |
| **Priority** | Medium |
| **Preconditions** | User is on the **Contact Us** section |

**Steps:**
1. Open the **Contact Us** section.
2. Verify the **Call Us** option is present.
3. Verify the **Email Us** option is present.
4. Verify both options are actionable.

**Expected Result:** Both support channels are present on the same page, and the addition of phone support does not remove or break the existing email support path.

---

### Notes
- Confirm the final production copy uses **Call Us** and **Email Us** labels exactly as approved by product/design.
- If the release is gated by a go-live date from the call center, execute these cases only in the build/environment where the feature is intended to be active.
