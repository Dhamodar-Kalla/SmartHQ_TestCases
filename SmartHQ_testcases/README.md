# SmartHQ Test Cases

This repository contains **manual** and **automated (Appium)** test cases for SmartHQ features.

## Features Covered

- **Parts & Accessory Lookup**
- **Contact Us Support Enhancement**

## Flows Under Test

```
Home (Misc Features)
   └── Parts
        ├── Parts Diagram      → opens parts schematic diagrams
        ├── My Distributor     → opens geappliancescustomernet.com/login (GE Appliances Customer Net)
        ├── Customer Net       → "Contact your parts distributor for the code"
        │                        → enter customer code → opens distributor website
        └── Accessories Lookup → enter Model / Product / PIM Product ID → shows product details

Support / Contact Us
   ├── Call Us  → opens phone dialer with 800-792-3395
   ├── Email Us → opens email composer to SmartHQService.Support@geappliances.com
   └── Hours of Operation → Monday - Friday 8:30 AM - 5:00 PM EST
```

## Repository Structure

```
SmartHQ_testcases/
├── Manual_Testcases_Accessory_Lookup.md   # Manual test cases (TC-01 to TC-09)
├── Manual_Testcases_Contact_Us_Support.md # Manual test cases (CU-01 to CU-07)
├── test_accessory_lookup.py               # Appium + pytest automated script
├── requirements.txt                       # Python dependencies
└── README.md                              # This file
```

## Prerequisites

- **Python 3.9+**
- **Node.js** and **Appium Server 2.x** (`npm install -g appium`)
- **UiAutomator2 driver** (`appium driver install uiautomator2`)
- **Android SDK** with a connected device or running emulator
- The **SmartHQ app** installed on the device/emulator

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Dhamodar-Kalla/SmartHQ_TestCases.git
   cd SmartHQ_TestCases/SmartHQ_testcases
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Appium server (in a separate terminal):
   ```bash
   appium
   ```

## Configuration

Before running, update the desired capabilities in `test_accessory_lookup.py`:

```python
CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Android Emulator",
    "appium:appPackage": "com.geappliances.smarthq",              # <-- confirm actual package
    "appium:appActivity": "com.geappliances.smarthq.MainActivity",# <-- confirm actual activity
    "appium:noReset": True,
}
```

> **Note:** The locators and button labels (`"Submit"`, `"Search"`, `"Misc Features"`, etc.)
> are **placeholders**. Align them with the real SmartHQ app's resource IDs / accessibility
> IDs before running the tests.

## Running the Automated Tests

Run all tests:
```bash
pytest test_accessory_lookup.py -v
```

Run a single test:
```bash
pytest test_accessory_lookup.py::TestAccessoryLookupFlow::test_open_my_distributor -v
```

Generate an HTML report (requires `pytest-html`):
```bash
pip install pytest-html
pytest test_accessory_lookup.py --html=report.html --self-contained-html
```

## Manual Test Cases

- [`Manual_Testcases_Accessory_Lookup.md`](./Manual_Testcases_Accessory_Lookup.md) – detailed
  step-by-step manual test cases (TC-01 to TC-09) for Parts & Accessory Lookup, including
  positive and negative scenarios.
- [`Manual_Testcases_Contact_Us_Support.md`](./Manual_Testcases_Contact_Us_Support.md) – manual
  test cases (CU-01 to CU-07) for the Contact Us enhancement covering support phone, email,
  and hours of operation.

## Test Coverage Summary

| Area | Manual | Automated |
|------|--------|-----------|
| Navigate to Parts page | TC-01 | `test_navigate_to_parts_page` |
| Parts Diagram | TC-02 | `test_open_parts_diagram` |
| My Distributor | TC-03 | `test_open_my_distributor` |
| Customer Net prompt | TC-04 | `test_customer_net_prompts_for_code` |
| Customer Net code entry (valid/invalid/empty) | TC-05, TC-06 | `test_customer_net_code_entry` |
| Accessories Lookup prompt | TC-07 | `test_accessories_lookup_prompts_for_identifier` |
| Accessories Lookup details (positive) | TC-08 | `test_accessories_lookup_returns_details` |
| Accessories Lookup invalid input (negative) | TC-09 | `test_accessories_lookup_invalid_input` |
| Contact Us options displayed | CU-01 | — |
| Call Us display and routing | CU-02, CU-03 | — |
| Email Us display and routing | CU-04, CU-05 | — |
| Hours of operation display | CU-06 | — |
| Contact Us channel coexistence | CU-07 | — |
