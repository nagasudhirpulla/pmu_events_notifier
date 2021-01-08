import unittest
from src.appConfig import initAppConfig


class TestAppConfig(unittest.TestCase):
    def test_existence(self) -> None:
        """tests the function that gets app config
        """
        appConfig = initAppConfig()
        self.assertFalse(appConfig == None)
        self.assertTrue("persons" in appConfig)
        self.assertTrue("hrsOffset" in appConfig)

    def test_personsConfig(self) -> None:
        """tests the function that gets persons details from app config
        """
        appConfig = initAppConfig()
        persons = appConfig["persons"]
        self.assertTrue(isinstance(persons, list))
