#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Gleb Vasilev"

from test.basic_page_test import *
from pages.reg_page import *


class RegPageTest(BasicPageTest):

    def run(self):
        login_page_obj = RegPage(self.driver)
        login_page_obj.start()
