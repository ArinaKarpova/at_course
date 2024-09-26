import pytest
import allure



@allure.feature('Login')
@allure.story('Login with valid credentials')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Авторизаиця с корректными учетными данными')
@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, password, username):
    with allure.step('Открыть страницу авторизации'):
        login_page.navigate()
    with allure.step('Ввести в форму авторизации недействительные учетные данные'):
        login_page.login(username, password)
    with allure.step('Отображается приветственное сообщение с именем пользователя'):
        dashboard_page.assert_welcome_message(f"Welcome {username}")
