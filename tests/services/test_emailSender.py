import unittest
from src.services.emailSender import EmailSender
from src.appConfig import initAppConfig


class TestEmailSender(unittest.TestCase):

    def test_run(self) -> None:
        """tests the function that sends email
        """
        appConfig = initAppConfig()
        # print(appConfig)
        emailConfig = appConfig["emailConfig"]
        emailApi = EmailSender(
            emailConfig['emailAddress'], emailConfig["username"],
            emailConfig["password"], emailConfig['host'])
        emailApi.sendEmail(
            ['nagasudhir@posoco.in'], "Testing email sender in python", 'Hello from python script!', "data.xlsx")
        self.assertTrue(1 == 1)
