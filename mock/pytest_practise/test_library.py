from .library import is_even, is_palindrome
import pytest
@pytest.mark.usefixtures("init")
class TestLibrary:
    @pytest.mark.run(order=2)
    def test_even(self):
        print("running test_even")
        with pytest.raises(TypeError):
            is_even("10")

    @pytest.mark.run(order=1)
    def test_odd(self):
        print("running odd")
        assert is_even(7) == False
    @pytest.mark.smoke
    def test_invalid(self):
        print("running test_invalid")
        with pytest.raises(TypeError):
            raise is_even("hi")

    def test_pal(self):
        print("running test_pal")
        assert is_palindrome("hi") == False

    def test_valid_palindrome(self):
        print("running test_valid_palindrome")
        assert is_palindrome("racecar") == True

class TestYantra:
    @pytest.mark.dependency()
    def test_pakka(self):
        print("running")

    @pytest.mark.dependency(depends=["TestYantra::test_pakka"])
    def test_dep(self):
        print("dep is running")

@pytest.mark.parametrize("username, password", [("u1", "p1"), ("u2", "p2")], scope="class")
class Test_pa:
    def test_1(self, username, password):
        print("passing", username)
        print("passing", password)
    def test_2(self, username, password):
        print("passing", username)
        print("passing", password)