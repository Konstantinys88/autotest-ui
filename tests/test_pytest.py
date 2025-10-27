import pytest

# @pytest.fixture(autouse=True)
# def analitics_data():
#     print('Анализ данных')
    
# @pytest.fixture(scope='session')    
# def settings():
#     print('session')
    
# @pytest.fixture(scope='class')    
# def settings2():
#     print('class')    
    
@pytest.fixture
def fixture_test():
    print('fixture_test')    
        
    

class TestUserLogin:
    @pytest.mark.test_1
    def test_1(self):
        ...
        
        
    @pytest.mark.test_2    
    def test_2(self):
        ...    
        
class TestUserLogin2:
    @pytest.mark.test_1
    def test_3(self):
        ...
        
        
    @pytest.mark.test_2    
    def test_4(self, fixture_test):
        print('test 4')           
        
def test_assert_positive():
    assert(2 + 2) == 4        
    
@pytest.mark.skip(reason="Всё пропало")    
def test_assert_negative():
    assert(2 + 2) == 5, "(2 + 2) != 5"            
    
    
    
    


    result = divide(10, 2)    
           