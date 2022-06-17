import pytest
testdata=[[1,1,1]]
@pytest.mark.parametrize("a,b,c",testdata)
def test1(a,b,c):
    assert a*b==c
    print("inside the test11")