#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from pages.basic_page import *


class RegPage(BasicPage):

    def __init__(self, driver):

        super(RegPage, self).__init__(driver)
        self.__auth_link = 'https://samara.hh.ru/account/signup?backurl=%2Fapplicant%2Fresumes%2Fnew&from=header_new'

        # XPATH
        self.__xpath_name_box = '//input[@name="firstName"]'
        self.__xpath_last_name_box = '//input[@name="lastName"]'
        self.__xpath_mail_box = '//input[@name="login"]'
        self.__xpath_pass_box = '//span[text()="Зарегистрироваться"]'

    def __execute(self):
        self.driver.get(self.__auth_link)
        # wait for page to load
        self._wait_to_load()
        # enter the name
        name = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_name_box)))
        name.click()
        name.send_keys(self._config["user_name"])
        # enter the last name
        last_name = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_last_name_box)))
        last_name.click()
        last_name.send_keys(self._config["user_last_name"])
        # enter the mail
        login = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_mail_box)))
        login.click()
        login.send_keys(self._config["user_email"])
        # enter the pass
        password = WebDriverWait(self.driver, self._wait_time).until(ec.visibility_of_element_located((
            By.XPATH, self.__xpath_pass_box)))
        password.click()
        # wait for page to load
        self._wait_to_load()

    def start(self):
        self.__execute()