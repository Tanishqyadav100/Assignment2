from gettext import gettext

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.locators import Locators
from utils.data import TestData

@pytest.fixture(scope="class")
def setup(request):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    driver.implicitly_wait(10)  # Global implicit wait
    driver.maximize_window()  # Maximize the browser window
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestSauceDemo:

    def navigate_to_login(self):
        self.driver.get("https://www.saucedemo.com/v1/")

    def perform_login(self, username, password):
        self.driver.find_element(By.ID, Locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(By.ID, Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(By.ID, Locators.LOGIN_BUTTON).click()

    def test_invalid_login(self):
        self.navigate_to_login()
        self.perform_login(TestData.INVALID_USERNAME, TestData.INVALID_PASSWORD)

        # Explicit wait for error message visibility
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.ERROR_MESSAGE))
        )

        error_message = self.driver.find_element(By.CSS_SELECTOR, Locators.ERROR_MESSAGE).text
        assert "Epic sadface: " in error_message
        assert "Username and password do not match any user in this service" in error_message

    def test_valid_login(self):
        self.navigate_to_login()
        self.perform_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)

        # Explicit wait for product title visibility
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.PRODUCT_TITLE))
        )

        title = self.driver.find_element(By.CSS_SELECTOR, Locators.PRODUCT_TITLE).text
        assert title == "Products"

    def test_add_tshirts_to_cart(self):
        self.navigate_to_login()
        self.perform_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)

        # Wait for inventory items to be visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located((By.XPATH, Locators.ADD_TO_CART_BUTTON1))        )

        products = self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON2)
        # tshirt_count = self.driver.find_element(By.CSS_SELECTOR, Locators.CART_BADGE).text
        # for product in products:
        #     title = product.find_element(By.CLASS_NAME, "inventory_item_name").text
        #     if "T-shirt" in title:
        self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON1).click()
        self.driver.find_element(By.XPATH, Locators.ADD_TO_CART_BUTTON2).click()
                # print(f"Added {title} to cart")  # Debug output for confirmation

        # Wait for cart badge to show updated count
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.CART_BADGE))
        )


        # tshirt_count = self.driver.find_element(By.CSS_SELECTOR, Locators.CART_BADGE).text

        # Wait until the cart badge has the correct count
        # WebDriverWait(self.driver, 10).until(
        #     EC.text_to_be_present_in_element((By.CLASS_NAME, Locators.CART_BADGE), str(tshirt_count))
        # )

        cart_count = self.driver.find_element(By.CSS_SELECTOR, Locators.CART_BADGE).text
        tshirtList=len(self.driver.find_elements(By.XPATH, Locators.TSHIRT_COUNT))
        assert int(cart_count) == tshirtList

    def test_checkout(self):
        self.navigate_to_login()
        self.perform_login(TestData.VALID_USERNAME, TestData.VALID_PASSWORD)

        # Wait for cart link to be visible and click
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.CART_LINK))
        ).click()

        # Checkout
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.CHECKOUT_BUTTON))
        ).click()

        # Fill in the checkout form
        self.driver.find_element(By.ID, Locators.FIRST_NAME_INPUT).send_keys(TestData.FIRST_NAME)
        self.driver.find_element(By.ID, Locators.LAST_NAME_INPUT).send_keys(TestData.LAST_NAME)
        self.driver.find_element(By.ID, Locators.POSTAL_CODE_INPUT).send_keys(TestData.POSTAL_CODE)
        self.driver.find_element(By.CSS_SELECTOR, Locators.CONTINUE_BUTTON).click()

        # Wait for the overview title
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.OVERVIEW_TITLE))
        )

        overview_title = self.driver.find_element(By.CSS_SELECTOR, Locators.OVERVIEW_TITLE).text
        assert overview_title == "Sauce Labs Bolt T-Shirt"

        # Finish the checkout
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.FINISH_BUTTON))
        ).click()

        # Wait for the completion title
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.COMPLETE_TITLE))
        )

        complete_title = self.driver.find_element(By.CSS_SELECTOR, Locators.COMPLETE_TITLE).text
        assert complete_title == "THANK YOU FOR YOUR ORDER"
