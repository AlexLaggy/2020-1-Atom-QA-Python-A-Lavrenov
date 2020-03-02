import pytest
import random


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(1, 100)


class Test3:
    string = 'Аргентина Манит Негра'

    def test3_1(self):
        errors = []
        for i in self.string:
            try:
                assert i.isupper()
            except AssertionError:
                errors.append(f'{i} is not in upper case')
        assert not errors

    @pytest.mark.parametrize('a', ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'])
    def test3_2(self, class_fixture, a):
        print(f'class fixture:{class_fixture}')
        consonants = []
        for i in self.string:
            try:
                assert i.lower() in a
            except AssertionError:
                consonants.append([f'{i} is a consonant'])
        assert not consonants

    def test3_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.string.lower().replace(' ', '') == self.string.lower().replace(' ', '')[::-1]

    def test3_4(self):
        assert self.string.find('hello') != -1

    def test3_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert len(self.string.split()) == 2
