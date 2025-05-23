from profee_tests.pages.main_page_unauthorized import MainPageUnauthorized


def test_too_small_sender_amount():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met()\
    .type_from_amount('5')\
    .too_small_amount()

def test_too_large_sender_amount():
    MainPageUnauthorized()\
    .open_main_url()\
    .preconditions_met()\
    .type_from_amount('15001')\
    .too_large_amount()



