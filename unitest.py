import unittest
import code

class TestDataImport(unittest.TestCase):
    def test_import(self):
        data = code.import_data()
        self.assertIsNotNone(data)
        self.assertIsInstance(data, pandas.DataFrame)
        self.assertGreater(data.shape[0], 0)

class TestDataManipulation(unittest.TestCase):
    def setUp(self):
        self.data = code.import_data()

    def test_manipulation(self):
        manipulated_data = code.manipulate_data(self.data)
        self.assertIsNotNone(manipulated_data)
        self.assertIsInstance(manipulated_data, pandas.DataFrame)
        self.assertEqual(manipulated_data.shape, (self.data.shape[0], 2))

class TestScatterPlot(unittest.TestCase):
    def setUp(self):
        self.data = code.import_data()
        self.manipulated_data = code.manipulate_data(self.data)

    def test_scatter_plot(self):
        scatter_plot = code.create_scatter_plot(self.manipulated_data)
        self.assertIsNotNone(scatter_plot)
        self.assertIsInstance(scatter_plot, matplotlib.figure.Figure)

class TestDropdownMenu(unittest.TestCase):
    def setUp(self):
        self.data = code.import_data()
        self.manipulated_data = code.manipulate_data(self.data)

    def test_dropdown_menu(self):
        dropdown_menu = code.create_dropdown_menu(self.manipulated_data)
        self.assertIsNotNone(dropdown_menu)
        self.assertIsInstance(dropdown_menu, dash_core_components.Dropdown)

if __name__ == '__main__':
    unittest.main()
