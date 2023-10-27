from main import *

def test_count_occurrences():
    assert count_occurrences("banana","a") == 3
    assert count_occurrences("'It rained on his lousy tombstone, and it rained on the grass on his stomach. It rained all over the place.' — The Catcher in the Rye by JD Salinger", "rained") == 3
    assert count_occurrences("Austin High", "i") == 2

def test_reverse():
    assert reverse("reversed") == "desrever"
    assert reverse("lived") == "devil"
    assert reverse("Austin High") == "hgiH nitsuA"

def test_replace_cat():
    assert replace_cat("concatenate") == "condogenate"
    assert replace_cat("Cats! I love cats!") == "Dogs! I love dogs!"