
vowels = ["a","e","i","o","u"]

def vowel_count(string):
    count = 0
    for x in string:
        if x in vowels:
            count = count+1
    return count

def test_name():
    assert vowel_count("Hatib Zubair") == 0


