from profee_tests.pages.main_page_unauthorized import MainPageUnauthorized


def test_too_small_sender_amount():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met()\
    .type_from_amount('5')\
    .should_too_small_amount()

def test_too_large_sender_amount():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met()\
    .type_from_amount('15001')\
    .should_too_large_amount()

def test_india_promo_less1100eur():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met() \
    .chose_to_country('Индия')\
    .should_promo_terms_is_visible()

def test_india_no_promo_more1100eur():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met()\
    .type_from_amount('1101') \
    .chose_to_country('Индия')\
    .should_promo_terms_is_not_visible()

def test_redirect_to_auth_page_from_start_button():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met() \
    .tap_start_button() \
    .auth_page_check_text()

def test_redirect_to_auth_page_from_login_button():
    MainPageUnauthorized()\
    .open_main_url()\
    .tap_login_button() \
    .auth_page_check_text()

def test_redirect_to_auth_page_from_enter_button():
    MainPageUnauthorized()\
    .open_main_url()\
    .tap_enter_button() \
    .auth_page_check_text()

def test_change_language_to_en():
    MainPageUnauthorized()\
    .open_main_url() \
    .preconditions_met() \
    .tap_language_button() \
    .select_english() \
    .should_be_en()











