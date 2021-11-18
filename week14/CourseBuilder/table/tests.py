from django.test import TestCase

from .table import read_csv_file, write_csv_file


class TableTest(TestCase):

    def test_read_csv(self):
        table = read_csv_file('Documents/Test/animals.csv')
        self.assertEqual(table, [['1', 'Dog'], ['2', 'Cat'], ['3', 'Bird'], ['4', 'Fish']])

    def test_write_csv(self):
        table = read_csv_file('Documents/Test/animals.csv')
        self.assertEqual(table, [['1', 'Dog'], ['2', 'Cat'], ['3', 'Bird'], ['4', 'Fish']])
        write_csv_file('Documents/Test/animals.csv', table)
        table = read_csv_file('Documents/Test/animals.csv')
        self.assertEqual(table, [['1', 'Dog'], ['2', 'Cat'], ['3', 'Bird'], ['4', 'Fish']])
