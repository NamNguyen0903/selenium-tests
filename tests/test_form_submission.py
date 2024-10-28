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
    driver.get('http://localhost/opencart/upload/index.php?route=information/contact&language=en-gb')
    yield driver
    driver.quit()

def test_form_submission(driver):
    # Kiểm tra trường 'Name' có hiển thị và nhập dữ liệu
    name = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'input-name'))
    )
    assert name.is_displayed(), "Trường 'Name' không hiển thị."
    name.send_keys('John Doe')

    # Kiểm tra trường 'Email' có hiển thị và nhập dữ liệu
    email = driver.find_element(By.ID, 'input-email')
    assert email.is_displayed(), "Trường 'Email' không hiển thị."
    email.send_keys('john@example.com')

    # Kiểm tra trường 'Enquiry' có hiển thị và nhập dữ liệu
    enquiry = driver.find_element(By.ID, 'input-enquiry')
    assert enquiry.is_displayed(), "Trường 'Enquiry' không hiển thị."
    enquiry.send_keys('Đây là tin nhắn kiểm thử.')

    # Kiểm tra nút 'Submit' có thể nhấp và thực hiện gửi form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    assert submit_button.is_enabled(), "Nút 'Submit' không hoạt động."
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0, -200);")
    driver.execute_script("arguments[0].click();", submit_button)

    # Chờ trang xác nhận tải xong bằng cách kiểm tra URL hoặc tiêu đề trang
    WebDriverWait(driver, 10).until(EC.url_contains("success"))
    assert "success" in driver.current_url, "Không điều hướng đến trang xác nhận thành công."

    # Kiểm tra nội dung trong phần tử #content
    new_content = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'content'))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", new_content)

    # Kiểm tra nội dung xác nhận thành công
    assert "Your enquiry has been successfully sent to the store owner!" in new_content.text, \
        "Nội dung thông báo thành công không đúng sau khi chuyển trang."