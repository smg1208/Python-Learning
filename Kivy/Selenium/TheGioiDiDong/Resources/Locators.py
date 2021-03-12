from selenium.webdriver.common.by import By


class Locators():
    # --- Home Page Locators ---
    SEARCH_TEXTBOX = (By.ID, "search-keyword")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//button[contains(@class,'btntop')]")
    MOBILEPHONE_BUTTON = (By.XPATH, "//nav/a[contains(@class,'mobile')]")
    TABLET_BUTTON = (By.XPATH, "//nav/a[contains(@class,'tablet')]")
    LAPTOP_BUTTON = (By.XPATH, "//nav/a[contains(@class,'laptop')]")
    ACCESSORIES_BUTTON = (By.XPATH, "//nav/a[contains(@class,'phukien')]")
    SMARTWATCH_BUTTON = (By.XPATH, "//nav/a[contains(@class,'smartwatch')]")
    OLD_DEVICE_BUTTON = (By.XPATH, "//nav/a[contains(@class,'maydoitra')]")
    NEWS_BUTTON = (By.XPATH, "//nav/a[contains(@class,'news')]")
    ASK_BUTTON = (By.XPATH, "//nav/a[contains(@class,'ask')]")
    SIMCARD_BUTTON = (By.XPATH, "//nav/a[contains(@class,'cardsim')]")
    ULTILITIES_BUTTON = (By.XPATH, "//nav/a[contains(@class,'utility')]")

    # --- Search filter
    NEW_PRODUCT_RADIAL_BUTTON = (
        By.XPATH, "//div[contains(@class,'report_text)]/label[@class,'newProduct']")
    OLD_PRODUCT_RADIAL_BUTTON = (
        By.XPATH, "//div[contains(@class,'report_text)]/label[@class,'oldProduct']")
    OLD_PRODUCT_RADIAL_BUTTON = (
        By.XPATH, "//div[contains(@class,'report_text)]/label[@class,'news']")

    # --- Search Results Page Locators ---
    PRODUCTS = (By.XPATH, "//ul[@class,'listsearch']/li[@class,'cat42']")
    PRODUCTS_DISCOUNT = (By.XPATH, "//ul[@class,'listsearch']/li[@class,'cat42']/label")
    SEARCH_RESULT_LINK = (
        By.XPATH, "(//div[@class='sg-col-inner']//img[contains(@data-image-latency,'s-product-image')])[2]")

    # --- Product Details Page Locators ---
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    # --- Sub Cart Page Locators ---
    SUB_CART_DIV = (By.ID, "hlb-subcart")
    PROCEED_TO_BUY_BUTTON = (By.ID, "hlb-ptc-btn-native")
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_LINK = (By.ID, "nav-cart")

    # --- Cart Page Locators ---
    DELETE_ITEM_LINK = (
        By.XPATH, "//div[contains(@class,'a-row sc-action-links')]//span[contains(@class,'sc-action-delete')]")
    CART_COUNT = (By.ID, 'nav-cart-count')
    PROCEED_TO_CHECKOUT_BUTTON = (By.NAME, "proceedToCheckout")
    # --- Signin Page Locators ---
    USER_EMAIL_OR_MOBIL_NO_TEXTBOX = (By.ID, "ap_email")
