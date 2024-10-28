import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.get('http://localhost/opencart/upload/index.php?route=account/login&language=en-gb')
    yield driver
    driver.quit()

@pytest.mark.usefixtures("driver")
class TestLoginLogout:
    def test_login_logout(self, driver):
        # Điền thông tin đăng nhập với địa chỉ email và mật khẩu
        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'input-email'))
        )
        password = driver.find_element(By.ID, 'input-password')

        # Xác nhận rằng các trường email và password hiển thị trên trang
        assert email.is_displayed(), "Trường 'Email' không hiển thị."
        assert password.is_displayed(), "Trường 'Password' không hiển thị."

        email.send_keys('namtronghlg0903@gmail.com')
        password.send_keys('123456')

        # Tìm và nhấp vào nút đăng nhập
        login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        assert login_button.is_enabled(), "Nút 'Đăng nhập' không khả dụng."
        login_button.click()

        # Xác nhận đăng nhập thành công bằng cách kiểm tra tiêu đề trang
        assert WebDriverWait(driver, 10).until(
            EC.title_contains('My Account')
        ), "Đăng nhập không thành công, không vào được trang 'My Account'."

        # Mở menu "My Account" trên thanh menu
        my_account_menu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'My Account'))
        )
        assert my_account_menu.is_displayed(), "Menu 'My Account' không hiển thị."
        my_account_menu.click()

        # Chọn "Logout" từ menu "My Account" để đăng xuất
        logout_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Logout'))
        )
        assert logout_link.is_displayed(), "Liên kết 'Logout' không hiển thị trong menu 'My Account'."
        logout_link.click()

        # Xác nhận đăng xuất thành công bằng cách kiểm tra tiêu đề trang
        assert WebDriverWait(driver, 10).until(
            EC.title_contains('Account Logout')
        ), "Đăng xuất không thành công, không vào được trang 'Account Logout'."
