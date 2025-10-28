import pytest

@pytest.fixture
def clear_database():
    print('clear_database')
    
@pytest.fixture
def fill_database():
    print('fill_database')    
    
    
@pytest.mark.usefixtures('clear_database')    
def test_read():
    print('test_read')    
    
@pytest.mark.usefixtures(
    'clear_database',
    'fill_database'
    )        
class TestLib:
    def test_1(self):
        ...
        
    def test_2(self):
        ...       
        
