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
                assert type(value) is not dict
            except AssertionError:
                errors.append(f'{value} is a dict, we can\'t get it')
        assert not errors

    @pytest.mark.parametrize('a', [1, None])
    def test5_2(self, class_fixture, a):
        print(f'class fixture:{class_fixture}')
        assert a in self.s

    def test5_3(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert 15 not in self.s

    def test5_4(self):
        assert self.s.issuperset({1, 'OMG'})

    def test5_5(self, class_fixture):
        print(f'class fixture:{class_fixture}')
        assert self.s == {1, 3, 'OMG', None}
