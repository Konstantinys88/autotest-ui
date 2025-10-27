import pytest

def test_user_login():
    print('test')

class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...    
        
def test_assert_positive():
    assert(2 + 2) == 4        
    
# def test_assert_negative():
    # assert(2 + 2) == 5, "(2 + 2) != 5"            
    
    
    
    
@pytest.mark.test_1
def test_1():
    print('test_1')
    
@pytest.mark.test_1
@pytest.mark.test_2     
def test_2():
    print('test_2')
       
@pytest.mark.test_3       
def test_3():
    print('test_3')
           