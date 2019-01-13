from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import itertools
import multiprocessing
import random
import time


def get_cards(x):
    """From number to digits.

    Args:
        x: a number from 0 to 80.

    Returns:
        a tuple of four numbers corresponding to the four features
    """
    x1 = x // 27
    x2 = (x % 27) // 9
    x3 = (x % 9) // 3
    x4 = x % 3
    return (x1, x2, x3, x4)


def is_set(a, b, c):
    """Whether three cards form a set."""
    a_cards = get_cards(a)
    b_cards = get_cards(b)
    c_cards = get_cards(c)
    for i in range(4):
        if a_cards[i] == b_cards[i] and b_cards[i] == c_cards[i]:
            continue
        elif (a_cards[i] != b_cards[i] and b_cards[i] != c_cards[i]
              and c_cards[i] != a_cards[i]):
            continue
        else:
            return False
    return True


def has_set(nums):
    """Whether a list of numbers contains a set."""
    assert len(nums) >= 3
    for combination in itertools.combinations(nums, 3):
        a, b, c = combination
        if is_set(a, b, c):
            return True
    return False


def probability_set_approx(k, num_trials=1000000):
    """Probability of k cards containing a set, approximated."""
    start_time = time.time()
    count = 0
    for _ in range(num_trials):
        nums = random.sample(range(81), k)
        if has_set(nums):
            count += 1
    end_time = time.time()
    return count, num_trials, end_time - start_time


def probability_set(k):
    """Probability of k cards containing a set, exact number."""
    start_time = time.time()
    count = 0
    total = 0
    for nums in itertools.combinations(range(81), k):
        total += 1
        if has_set(nums):
            count += 1
    end_time = time.time()
    return count, total, end_time - start_time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start",
        default=12,
        type=int,
        help="Number of cards to start with the simulation.")
    parser.add_argument(
        "--end",
        default=18,
        type=int,
        help="Number of cards to end with the simulation.")
    parser.add_argument(
        "--num_trials",
        default=100000,
        type=int,
        help="Number of trials. The larger the number, "
             "the more accurate the result is. "
             "If this number is zero or negative, we will use accurate "
             "simulation instead of approximated simulation.")
    args = parser.parse_args()

    for k in range(args.start, args.end + 1):

        if args.num_trials <= 0:
            count, total, duration = probability_set(k)
        else:
            count, total, duration = probability_set_approx(k, args.num_trials)

        print("Probability of {} cards containing a set: {} / {} = {}, "
              "time spent: {}s".format(
                  k, count, total, count / total, duration))


if __name__ == "__main__":
    main()
