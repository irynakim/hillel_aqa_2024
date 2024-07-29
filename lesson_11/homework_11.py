"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
Логує подію входу в систему.
username: Ім'я користувача, яке входить в систему.
status: Статус події входу:
* success - успішний, логується на рівні інфо
* expired - пароль застаріває і його слід замінити, логується на рівні warning
* failed  - пароль невірний, логується на рівні error
"""

import logging
import pytest

# Створення та налаштування логера
logging.basicConfig(
    filename='login_system.log', force=True,
    level=logging.INFO,
    # format='%(asctime)s - %(message)s'
    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("log_event")


@pytest.mark.parametrize('username,status',
                         [('success_user', 'success'),
                          ('expired_user2', 'expired'),
                          ('failed_user3', 'failed')],
                         ids=['success_user', 'expired_user', 'failed_user'])
def test_log_event(username, status):
    log_message = f"Login event - Username: {username}, Status: {status}"
    logger.info(log_message)
    # Логування події

    f = open("login_system.log", "r")
    text = f.read()
    last_word = text.split()
    log_status = last_word[-1]
    pass

    verification_log_message = f"Verification result - Username: {username}, Status: {status}"
    if log_status == "success":
        logger.info(verification_log_message)
    elif log_status == "expired":
        logger.warning(verification_log_message)
    else:
        logger.error(verification_log_message)
