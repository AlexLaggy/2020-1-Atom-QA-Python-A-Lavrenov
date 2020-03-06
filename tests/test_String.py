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
                assert type(i) == str
            except AssertionError:
                errors.append(f'{i} is not a char')
        assert not errors

    @pytest.mark.parametrize('a', ['а', 'е', 'и'])
    def test3_2(self, a):
        consonants = []
        try:
            assert a in self.string.lower()
        except AssertionError:
            consonants.append([f'Our string has no {a} char'])
        assert not consonants

    def test3_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.string.lower().replace(' ', '') == self.string.lower().replace(' ', '')[::-1]

    def test3_4(self):
        assert self.string.find('hello') == -1

    def test3_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert len(self.string.split()) == 3
