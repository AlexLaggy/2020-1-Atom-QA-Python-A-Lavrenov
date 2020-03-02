import pytest
import random
from mimesis import Transport


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(1, 100)


class Test4:
    jobs = [Transport().car() for _ in range(5)]
    dictionary = {i: string for i, string in enumerate(jobs)}

    def test4_1(self):
        errors = []
        for key, value in self.dictionary.items():
            try:
                assert len(value.split()) < 3
            except AssertionError:
                errors.append(f'{value} with key {key} has more than 2 words')
        assert not errors

    @pytest.mark.parametrize('a', ['Volvo', 'Perodua'])
    def test4_2(self, class_fixture, a):
        print(f'class fixture:{class_fixture}')
        errors = []
        for item in self.dictionary.values():
            try:
                for i in a:
                    assert item.find(i) != -1
                    continue
            except AssertionError:
                errors.append(f'{item} can\'t search')
        assert not errors

    def test4_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert 'Volvo' not in self.dictionary.values()

    def test4_4(self):
        assert 5 in self.dictionary.keys()

    def test4_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        errors = []
        val = self.dictionary[0]
        try:
            assert val not in self.dictionary.values()
        except AssertionError:
            errors.append(f'{val} already exists in values')
        assert not errors
