'Scenario'

"""
You have 100 cats.

One day you decide to arrange all your cats in a giant circle.
- Initially, none of your cats have any hats on. 
- You walk around the circle 100 times:
	- always starting at the same spot, with the first cat (cat # 1). 
- Every time you stop at a cat:
	- you either put a hat on it if it doesn’t have one on,
	- or you take its hat off if it has one on.

1. In The first round, you stop at every cat, placing a hat on each one.
2. In The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
3. In The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).

Write a program that simply outputs which cats have hats at the end.

Optional: Make a function that can calculate hats with any amount of rounds and cats.
"""

# ---------------------------------------------------
# 100 cats, 100 rounds

"""
Complexity:
- Time: O(n)
- Space: O(n)
"""

def hundred_cats_with_hats():
    return [i*i for i in range(1, 11)]

# --------------------------------------------------
# General code - any cats/rounds

"""
Complexity:
- Time: O(n^2)
- Space: O(n^2)
"""


def cats_with_hats(num_cats, num_rounds):
    cats = [False] * num_cats  # Initialize the list of cats without hats

    for round in range(1, num_rounds + 1):
        for cat in range(1, num_cats + 1):
            if cat % round == 0:
                cats[cat - 1] = not cats[cat - 1]  # Toggle the cat's hat status

    # Find the indices of cats with hats
    cats_with_hats = [index + 1 for index in range(len(cats)) if cats[index]]
    return cats_with_hats

# Tests
def test_cats_with_hats():
    # Rounds tests
    result1 = cats_with_hats(12, 1)
    assert result1 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result2 = cats_with_hats(12, 11)
    assert result2 == [1, 4, 9, 12]
    result3 = cats_with_hats(12, 12)
    assert result3 == [1, 4, 9]
    result4 = cats_with_hats(12, 13)
    assert result4 == [1, 4, 9]

    # Cats tests
    result5 = cats_with_hats(6, 12)
    assert result5 == [1, 4]
    result6 = cats_with_hats(11, 12)
    assert result6 == [1, 4, 9]
    result7 = cats_with_hats(24, 12)
    assert result7 == [1, 4, 9, 13, 14,
                       15, 17, 18, 19, 20,
                       21, 22, 23, 24]


if __name__ == "__main__":
    print(hundred_cats_with_hats())
    print("Cats with hats:", cats_with_hats(100, 100))
    test_cats_with_hats()
    