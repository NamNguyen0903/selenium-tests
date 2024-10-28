import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time  # Import time module for sleep function


@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get('http://localhost/opencart/upload/index.php?route=common/home&language=en-gb')
    yield driver
    driver.quit()


def test_responsive_design(driver):
    # Danh sách các kích thước màn hình để kiểm tra tính phản hồi của trang
    sizes = [800, 1024, 1440]

    # Kiểm tra từng kích thước màn hình
    for size in sizes:
        # Thiết lập kích thước cửa sổ trình duyệt
        driver.set_window_size(size, 800)
        time.sleep(2)  # Thời gian chờ để trang điều chỉnh giao diện

        # Xác minh thanh điều hướng (.navbar) hiển thị ở kích thước hiện tại
        navbar = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.navbar'))
        )
        assert navbar.is_displayed(), f"Thanh điều hướng không hiển thị ở kích thước {size}px"

        # In thông báo xác nhận kiểm tra thành công với kích thước màn hình
        print(f'Test passed for screen width {size}')
