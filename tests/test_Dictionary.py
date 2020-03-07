import pytest
import random
import copy
from mimesis import Transport


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(0, 4)


class Test4:
    jobs = [Transport().car() for _ in range(5)]
    dictionary = {i: string for i, string in enumerate(jobs)}

    def test4_1(self):
        errors = []
        for key, value in self.dictionary.items():
            try:
                assert len(value.split()) >= 1
            except AssertionError:
                errors.append(f'{value} with key {key} has more than 2 words')
        assert not errors

    @pytest.mark.parametrize('a', ['Пятерка', 'Ока'])
    def test4_2(self, a):
        assert a not in self.dictionary.values()

    def test4_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        tmp = copy.deepcopy(self.dictionary)
        assert id(tmp) != id(self.dictionary.values())

    def test4_4(self):
        assert 0 in self.dictionary.keys()

    def test4_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        errors = []
        val = class_fixture
        try:
            assert val in self.dictionary.keys()
        except AssertionError:
            errors.append(f'{val} already exists in values')
        assert not errors
