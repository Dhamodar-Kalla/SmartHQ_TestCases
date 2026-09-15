"""
Appium automated test script for the SmartHQ Parts & Accessory Lookup flow.

Flow covered:
  Home (Misc Features) -> Parts -> Parts landing page
    -> Parts Diagram      : opens schematic diagrams
    -> My Distributor      : opens geappliancescustomernet.com/login (GE Appliances Customer Net)
    -> Customer Net        : prompts "Contact your parts distributor for the code",
                             then asks for customer code, then opens distributor website
    -> Accessories Lookup  : asks for Model / Product / PIM Product ID, returns product details

Requirements:
  pip install Appium-Python-Client pytest selenium
  A running Appium server (default http://127.0.0.1:4723)
  A connected Android device / emulator with the SmartHQ app installed
"""

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

APPIUM_SERVER = "http://127.0.0.1:4723"

# ---- Update these to match your app / environment ----
CAPS = {
    "platformName": "Android",
    "appium:automationName": "UiAutomator2",
    "appium:deviceName": "Android Emulator",
    "appium:appPackage": "com.geappliances.smarthq",       # TODO: confirm actual package
    "appium:appActivity": "com.geappliances.smarthq.MainActivity",  # TODO: confirm actual activity
    "appium:noReset": True,
    "appium:newCommandTimeout": 300,
}


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options().load_capabilities(CAPS)
    drv = webdriver.Remote(APPIUM_SERVER, options=options)
    drv.implicitly_wait(10)
    yield drv
    drv.quit()


def wait(driver, timeout=15):
    return WebDriverWait(driver, timeout)


def tap_text(driver, text):
    """Tap an element by its visible text (Android UiSelector)."""
    el = wait(driver).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}")')
        )
    )
    el.click()
    return el


def is_text_visible(driver, text, timeout=15):
    try:
        wait(driver, timeout).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 f'new UiSelector().textContains("{text}")')
            )
        )
        return True
    except Exception:
        return False


# ------------------------------------------------------------------
# Navigation
# ------------------------------------------------------------------
def open_parts_landing(driver):
    """From home page, open Misc Features -> Parts landing page."""
    tap_text(driver, "Misc Features")
    tap_text(driver, "Parts")
    assert is_text_visible(driver, "Parts Diagram"), "Parts landing page did not open"


class TestAccessoryLookupFlow:

    def test_navigate_to_parts_page(self, driver):
        open_parts_landing(driver)
        for link in ["Parts Diagram", "My Distributor", "Customer Net", "Accessories Lookup"]:
            assert is_text_visible(driver, link), f"'{link}' link not visible on Parts page"

    # ---- Parts Diagram ----
    def test_open_parts_diagram(self, driver):
        open_parts_landing(driver)
        tap_text(driver, "Parts Diagram")
        assert is_text_visible(driver, "Diagram") or is_text_visible(driver, "Schematic"), \
            "Parts schematic diagrams did not open"

    # ---- My Distributor ----
    def test_open_my_distributor(self, driver):
        open_parts_landing(driver)
        tap_text(driver, "My Distributor")
        # WebView / browser opens the customer net login page
        assert is_text_visible(driver, "Customer Net") or \
               is_text_visible(driver, "geappliancescustomernet.com/login"), \
            "My Distributor did not open GE Appliances Customer Net login"

    # ---- Customer Net ----
    def test_customer_net_prompts_for_code(self, driver):
        open_parts_landing(driver)
        tap_text(driver, "Customer Net")
        assert is_text_visible(driver, "Contact your parts distributor for the code"), \
            "Customer Net distributor-code message not shown"

    @pytest.mark.parametrize("code,expected", [
        ("VALID_CODE", "distributor"),   # valid -> distributor website opens
        ("INVALID_CODE", "error"),       # invalid -> error message
        ("", "required"),                # empty -> validation error
    ])
    def test_customer_net_code_entry(self, driver, code, expected):
        open_parts_landing(driver)
        tap_text(driver, "Customer Net")
        field = wait(driver).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.widget.EditText")')
            )
        )
        field.clear()
        if code:
            field.send_keys(code)
        tap_text(driver, "Submit")
        assert is_text_visible(driver, expected, timeout=10), \
            f"Expected '{expected}' outcome for code '{code}'"

    # ---- Accessories Lookup ----
    def test_accessories_lookup_prompts_for_identifier(self, driver):
        open_parts_landing(driver)
        tap_text(driver, "Accessories Lookup")
        assert (is_text_visible(driver, "Model")
                or is_text_visible(driver, "Product")
                or is_text_visible(driver, "PIM Product ID")), \
            "Accessories Lookup did not prompt for Model/Product/PIM Product ID"

    @pytest.mark.parametrize("identifier,value", [
        ("Model", "VALID_MODEL"),
        ("Product", "VALID_PRODUCT"),
        ("PIM Product ID", "VALID_PIM_ID"),
    ])
    def test_accessories_lookup_returns_details(self, driver, identifier, value):
        open_parts_landing(driver)
        tap_text(driver, "Accessories Lookup")
        tap_text(driver, identifier)
        field = wait(driver).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.widget.EditText")')
            )
        )
        field.clear()
        field.send_keys(value)
        tap_text(driver, "Search")
        assert is_text_visible(driver, "Product Details") or is_text_visible(driver, "Details"), \
            f"Product details not shown for {identifier}={value}"

    @pytest.mark.parametrize("identifier,value", [
        ("Model", "INVALID_MODEL"),
        ("Product", "INVALID_PRODUCT"),
        ("PIM Product ID", "INVALID_PIM_ID"),
    ])
    def test_accessories_lookup_invalid_input(self, driver, identifier, value):
        open_parts_landing(driver)
        tap_text(driver, "Accessories Lookup")
        tap_text(driver, identifier)
        field = wait(driver).until(
            EC.presence_of_element_located(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.widget.EditText")')
            )
        )
        field.clear()
        field.send_keys(value)
        tap_text(driver, "Search")
        assert is_text_visible(driver, "No results") or is_text_visible(driver, "not found"), \
            f"Expected no-results/error for {identifier}={value}"
