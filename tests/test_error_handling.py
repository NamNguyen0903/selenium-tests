import pytest
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
    driver.get('http://localhost/opencart/upload/index.php?route=account/login&language=en-gb')
    yield driver
    driver.quit()
def test_invalid_login(driver):
    # Nhập thông tin đăng nhập không hợp lệ
    email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'input-email'))
    )
    password = driver.find_element(By.ID, 'input-password')

    email.send_keys('invalid@example.com')
    password.send_keys('invalidpassword')

    # Nhấn vào nút đăng nhập
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    import time

    login_button.click()
    time.sleep(0.5)  # Thời gian chờ để đảm bảo thông báo xuất hiện

    # Kiểm tra trực tiếp trong mã nguồn của trang
    page_source = driver.page_source
    if 'Warning: No match for E-Mail Address and/or Password.' in page_source:
        print("Thông báo lỗi hiển thị trong page_source.")
        assert True, "Thông báo lỗi hiển thị thành công"
    else:
        print("Không tìm thấy thông báo lỗi.")
        driver.save_screenshot("error_screen.png")
        assert False, "Không hiển thị thông báo lỗi."