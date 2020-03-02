import pytest
import random


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(1, 100)


class Test5:
    s = {1, 3, 'OMG', None}

    def test5_1(self):
        errors = []
        for value in self.s:
            try:
                assert type(value) is str
            except AssertionError:
                errors.append(f'{value} is not a string')
        assert not errors

    @pytest.mark.parametrize('a', [int, dict])
    def test5_2(self, class_fixture, a):
        print(f'class fixture:{class_fixture}')
        for item in self.s:
            if type(item) == a:
                return
        assert False

    def test5_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert 15 not in self.s

    def test5_4(self):
        assert self.s.issubset({15, 'Hello'})

    def test5_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.s.pop() == 3
