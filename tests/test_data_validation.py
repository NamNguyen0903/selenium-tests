import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get('http://localhost/opencart/upload/index.php?route=product/product&product_id=43')
    yield driver
    driver.quit()
def test_data_validation(driver):
    # Verify the product name
    product_name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
    )
    assert product_name.text == 'MacBook', "Product name did not match expected value"
    time.sleep(5)
