from selene import browser, be, have
import os
import allure
from selenium.webdriver.common.keys import Keys

class MainPageUnauthorized:
    def __init__(self):
        self.send_from_country = browser.element("#select-from_country")
        self.send_to_country = browser.element('#select-to_country > div > div.pfx-select__indicators.css-1wy0on6')
        self.send_from_amount = browser.element('#from_amount')
        self.send_to_amount = browser.element('#to_amount')
        self.type_to_country_name = browser.element('#to_country')

    @allure.step('Open main URL')
    def open_main_url(self):
        browser.open('/ru')
        return self

    @allure.step('Page loaded')
    def preconditions_met(self):
        self.send_from_amount.with_(timeout=10).should(be.visible)
        return self

    @allure.step('Chose from country')
    def chose_from_country(self, country):
        self.send_from_country.click()
        browser.element('.pfx-select-option__label').type(str(country) + Keys.ENTER)
        return self

    @allure.step('Chose to country')
    def chose_to_country(self, country):
        self.send_to_country.click()
        self.type_to_country_name.should(be.visible).type(country)
        browser.all('div.pfx-select-option').element_by(have.text(country)).click()
        return self

    @allure.step('Type from amount')
    def type_from_amount(self, amount):
        self.send_from_amount.click()
        self.send_from_amount.send_keys(Keys.COMMAND, 'a')  # для Windows/Linux
        self.send_from_amount.send_keys(Keys.DELETE)
        self.send_from_amount.type(str(amount) + Keys.ENTER)
        return self

    @allure.step('Type to amount')
    def type_to_amount(self, amount):
        self.send_to_amount.click.type(amount).press_enter()
        return self

    @allure.step('Too small amount error')
    def should_too_small_amount(self):
        browser.element('.pfx-input__error').should(have.text('Не менее 5,85 EUR'))
        return self

    @allure.step('Too large amount error')
    def should_too_large_amount(self):
        browser.element('.pfx-input__error').should(have.text('Меньше 15 000 EUR'))
        return self

    @allure.step('promorate block is visible')
    def should_promo_terms_is_visible(self):
        browser.element('.PromoCurrencyRateMessage_badge__content__o2lfr').should(be.visible)

    @allure.step('promorate block is not visible')
    def should_promo_terms_is_not_visible(self):
        browser.element('.PromoCurrencyRateMessage_badge__content__o2lfr').should(be.not_.visible)








