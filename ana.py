#!/usr/bin/env python

import argparse

PROG="""ANA"""

DESCRIPTION="""
This cute little script takes two strings and tests if
they form an anagram.
"""


def is_anagram(lhs, rhs):
    """
    Core logic checking if lhs and rhs form an anagram.

    The underlying logic is simple and naive which is to
    lowercase both strings, then split up both anagrams 
    into a list of solitary characters, sorting both lists
    and returning if both lists are equal.

    :param lhs: left hand side anagram
    :param rhs: right hand side anagram
    :return bool
    """
    _lhs = sorted(list(lhs.lower()))
    _rhs = sorted(list(rhs.lower()))
    return _lhs == _rhs 

def main():
    cli = argparse.ArgumentParser(prog=PROG, description=DESCRIPTION)
    cli.add_argument("str_1", help="The first string to check", type=str) 
    cli.add_argument("str_2", help="The second string to check", type=str) 
    args = cli.parse_args()

    result = is_anagram(args.str_1, args.str_2)

    print(result)

if __name__ == '__main__':
    main()

