# -*- coding: utf-8 -*-
import pytest
from _pytest.fixtures import SubRequest
import random


@pytest.mark.parametrize('os', ['mac','win','lin'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'deb'])
@pytest.mark.parametrize('numbers, string ', [(1,'fdfd'),(2, 'dsfs'),(3,'7876'), (4, '43242')])
def test_numbers(os, browser,numbers: int, string ):
    assert numbers > 0 and isinstance(string, str)
    print(f'num:{numbers}, str: {string}')
    
@pytest.fixture(params=['chromium', 'webkit', 'deb'])
def browser(request: SubRequest):
    return request.param

def test_open_browser(browser):
    print(f'Вызов browser: {browser}')

@pytest.mark.parametrize("user", [1, 2])
class TestOperation():
    @pytest.mark.parametrize('account', ["credit", "debit"])
    def test_user_with_operration(self, user, account):
        print('user_with')
        
    def test_user_without_operation(self, user):
        print('user_without')
        
@pytest.mark.parametrize(
    'numbers', 
    [32132,3232,'23423423'],
    ids=[
        "sana",
        'bomz',
        'Леха'
    ]
)
def test_identifiers(numbers: str):
    pass

@pytest.mark.flaky(reruns=3, reruns_delay=5)
def test_reruns():
    assert random.choice([True,False])