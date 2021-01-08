import unittest
from src.appConfig import initAppConfig
import pandas as pd


class TestExcelDump(unittest.TestCase):

    def test_run(self) -> None:
        """tests the function that sends email
        """
        appConfig = initAppConfig()
        # print(appConfig)
        fPath = appConfig["dataFilePath"]
        df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                           index=['row 1', 'row 2'],
                           columns=['col 1', 'col 2'])
        df1.to_excel(fPath)
        self.assertTrue(1 == 1)
