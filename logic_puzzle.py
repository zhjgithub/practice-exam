"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

import itertools


def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    Monday, Tuesday, Wednesday, Thursday, Friday = days = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(days))
    result = next(
        person_day_sort(
            Hamming=Hamming,
            Knuth=Knuth,
            Minsky=Minsky,
            Simon=Simon,
            Wilkes=Wilkes)
        for Hamming, Knuth, Minsky, Simon, Wilkes in orderings
        if Knuth == Simon + 1  # 6
        for programmer, writer, manager, designer, _ in orderings
        if programmer != Wilkes  # 2
        if Minsky != writer  # 4
        if Knuth == manager + 1  # 10
        if designer != Thursday  # 7
        for laptop, droid, tablet, iphone, _ in orderings
        if laptop == Wednesday  # 1
        if set([programmer, droid]) == set([Wilkes, Hamming])  # 3
        if Knuth != manager and tablet != manager  # 5
        if tablet != Friday  # 8
        if designer != droid  # 9
        if set([laptop, Wilkes]) == set([Monday, writer])  # 11
        if iphone == Tuesday or tablet == Tuesday  # 12
    )

    return result


def person_day_sort(**names):
    return sorted(names, key=lambda name: names[name])


def test():
    "tests."
    assert logic_puzzle() == ['Wilkes', 'Simon', 'Knuth', 'Hamming', 'Minsky']
    print('tests success')


if __name__ == '__main__':
    test()
