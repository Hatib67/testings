import pytest


@pytest.mark.parametrize("n,final",[(5,50),(6,60),(7,21)])
def test_mul(n,final):
    assert 10*n == final


@pytest.mark.parametrize("username, password",[("DragonSlayer67","m35gt7"),("kingboy77","getaway88")])
def test_login(username,password):
   print(username)
   print(password)