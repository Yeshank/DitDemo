import inspect

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


import logging

@pytest.mark.usefixtures('browser_invocation')
class BaseClass:


    # Adding the logic for explict wait
    def wait_presence(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(path))

    def wait_clickable(self, path):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(path))

    def message_logging(self, message):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        filehandler = logging.FileHandler('../main/logger.log')
        logger.addHandler(filehandler)
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)
        logger.setLevel(logging.INFO)
        logger.info(message)