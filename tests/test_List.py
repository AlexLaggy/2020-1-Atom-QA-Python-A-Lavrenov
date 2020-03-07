import pytest
import random


@pytest.fixture(scope='class')
def class_fixture():
    return random.randint(1, 100)


class Test1:
    mas = [i for i in range(10)][::2]

    def test1_1(self):
        errors = []
        for i in self.mas:
            try:
                assert i % 2 == 0
            except AssertionError:
                errors.append(f'{i} not even')
        assert not errors

    @pytest.mark.parametrize('a', [[1, 5, 7]])
    def test1_2(self, a):
        for i in self.mas:
            assert i ** 2 <= 1000

    def test1_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert len(self.mas + [class_fixture]) == 6

    def test1_4(self):
        tmp = self.mas[::-1]
        self.mas.reverse()
        assert self.mas == tmp

    def test1_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.mas[2] == 4
