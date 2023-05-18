import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize('book', ["coders-at-work_207", "the-cathedral-the-bazaar_190"])
def test_check_button_add_to_basket(browser, book):
    browser.get(f"http://selenium1py.pythonanywhere.com/catalogue/{book}/")
    btn_presence = None
    try:
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.ID, "add_to_basket_form")))
        btn_presence = True
    except:
        btn_presence = False

    assert btn_presence == True, f"Книга '{book}' недоступа для покупки"
