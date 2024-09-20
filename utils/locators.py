class Locators:
    USERNAME_INPUT = "user-name"  # ID for the username input field
    PASSWORD_INPUT = "password"  # ID for the password input field
    LOGIN_BUTTON = "login-button"  # ID for the login button
    ERROR_MESSAGE = "[data-test='error']"  # CSS selector for the h3 element with the error message class
    PRODUCT_TITLE = ".product_label"  # CSS selector for the product title
    INVENTORY_ITEM = "//div[contains(text(), 'T-Shirt')]"  # CLASS for individual inventory items
    TSHIRT_COUNT = "//div[contains(text(), 'T-Shirt')]/../../following-sibling::div/button"
    ADD_TO_CART_BUTTON1 = "(//div[contains(text(), 'T-Shirt')]/../../following-sibling::div/button)[1]"  # CLASS for the add to cart button
    ADD_TO_CART_BUTTON2 = "(//div[contains(text(), 'T-Shirt')]/../../following-sibling::div/button)[2]"
    CART_BADGE = ".fa-layers-counter"  # CLASS for the cart badge
    CART_LINK = ".shopping_cart_link"  # CSS selector for the cart link
    CHECKOUT_BUTTON = ".btn_action.checkout_button"  # CSS selector for the checkout button
    FIRST_NAME_INPUT = "first-name"  # ID for the first name input field
    LAST_NAME_INPUT = "last-name"  # ID for the last name input field
    POSTAL_CODE_INPUT = "postal-code"  # ID for the postal code input field
    CONTINUE_BUTTON = ".btn_primary.cart_button"  # CSS selector for the continue button
    OVERVIEW_TITLE = ".inventory_item_name"  # CSS selector for the overview title
    FINISH_BUTTON = ".btn_action.cart_button"  # CSS selector for the finish button
    COMPLETE_TITLE = ".complete-header"  # CSS selector for the completion title
