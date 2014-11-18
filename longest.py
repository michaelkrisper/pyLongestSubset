#! /usr/bin/env python3
# coding=utf-8
"""
Sucht die Länge der längsten aufsteigenden Teilfolge.
"""

__author__ = "Michael Krisper"
__email__ = "michael.krisper@gmail.com"
__date__ = "2014-11-18"


def main():
    folge = [9, 1, 19, 2, 3, 4, 5, 6, 7, 1, 2, 3, 3, 5, 0]

    count = 0
    max_count = 0
    last_item = float("-inf")
    for item in folge:
        if item > last_item:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 1
        last_item = item
    print(max_count)


if __name__ == "__main__":
    main()