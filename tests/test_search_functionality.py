# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# @pytest.fixture(scope="function")
# def driver():
#     driver = webdriver.Chrome()
#     driver.get('http://localhost/opencart/upload/index.php?route=common/home&language=en-gb')
#     yield driver
#     driver.quit()
#
# def test_search_functionality(driver):
#     # Wait for the search box to appear
#     search_box = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.NAME, 'search'))
#     )
#
#     # Wait for the search button to appear
#     search_button = WebDriverWait(driver, 10).until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-light.btn-lg'))
#     )
#
#     # Enter the search term
#     search_box.send_keys('Macbook')
#
#     # Click on the search button
#     search_button.click()
#     time.sleep(5)  # Adjust delay if needed based on loading time
#
#     # Print success message
#     print("Search was successful, and results have been displayed.")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture(params=["chrome", "firefox"], scope="function")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get('http://localhost/opencart/upload/index.php?route=common/home&language=en-gb')
    yield driver
    driver.quit()

def test_search_functionality(driver):
    # Đợi hộp tìm kiếm xuất hiện và kiểm tra xem nó có hiển thị không
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, 'search'))
    )
    assert search_box.is_displayed(), "Hộp tìm kiếm không hiển thị."

    # Đợi nút tìm kiếm xuất hiện và kiểm tra xem nó có hiển thị không
    search_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-light.btn-lg'))
    )
    assert search_button.is_displayed(), "Nút tìm kiếm không hiển thị."

    # Nhập từ khóa tìm kiếm và nhấn nút tìm kiếm
    search_box.send_keys('Macbook')
    search_button.click()
    time.sleep(5)  # Để thời gian cho kết quả tìm kiếm tải xong

    try:
        # Kiểm tra xem phần chứa kết quả tìm kiếm có hiển thị không
        search_results = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'product-list'))
        )
        assert search_results.is_displayed(), "Không có sản phẩm nào hiển thị trong kết quả tìm kiếm."
        print("Tìm kiếm thành công và kết quả đã được hiển thị.")
    except Exception as e:
        print("Không hiển thị kết quả tìm kiếm")
        raise e
