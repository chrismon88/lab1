import camelCase
from unittest import TestCase

class TestCamelCase(TestCase):

    def test_camelcase_sentence(self):

        self.assertEqual('helloWorld', camelCase.parser('Hello World'))
        self.assertEqual(' ', camelCase.parser(' '))
        self.assertEqual('helloWorld', camelCase.parser('      Hello    World    '))
