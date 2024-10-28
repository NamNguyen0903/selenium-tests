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
    driver.get('http://localhost/opencart/upload/index.php?route=common/home&language=en-gb')
    yield driver
    driver.quit()


def test_navigation(driver):
    # Tìm hình ảnh sản phẩm "MacBook" trên trang với thời gian chờ linh hoạt
    macbook_image = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='MacBook']"))
    )
    assert macbook_image.is_displayed(), "Hình ảnh của MacBook không hiển thị."

    # Cuộn trang xuống để thấy được hình ảnh của "MacBook"
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", macbook_image)

    # Đợi hình ảnh có thể nhấp vào và thực hiện nhấp với thời gian chờ linh hoạt
    clickable_macbook = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//img[@alt='MacBook']"))
    )
    clickable_macbook.click()

    # Kiểm tra URL có chứa 'product' để xác nhận điều hướng thành công
    WebDriverWait(driver, 30).until(EC.url_contains("product"))
    assert "product" in driver.current_url, \
        f"Không điều hướng đến trang sản phẩm. Current URL: {driver.current_url}"

    # Thông báo URL hiện tại để xác nhận
    print(f"Current URL after click: {driver.current_url}")