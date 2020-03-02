import pytest
import random


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(1, 100)


class Test2:
    var = 11

    @pytest.mark.parametrize('a', [11, 13, 15])
    def test2_1(self, a):
        errors = []
        print(a)
        try:
            assert a == self.var
        except AssertionError:
            errors.append(f'{a} != self.var')
        assert not errors

    def test2_2(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.var ** 2 <= 49

    def test2_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.var ** 2 == 121

    def test2_4(self):
        assert (self.var * 2) - 10 <= 22

    def test2_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.var + 4 != 15
