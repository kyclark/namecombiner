#!/usr/bin/env python3
"""Create married name hybrid"""

import argparse
from itertools import product
from typing import List


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create married name hybrid',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('name', metavar='str', nargs=2, help='Name')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    name1, name2 = args.name
    b1, b2 = beginnings(name1), beginnings(name2)
    e1, e2 = endings(name1), endings(name2)

    for b, e in [(b1, e2), (b2, e1)]:
        print('\n'.join(sorted(['-'.join(p) for p in product(b, e)])))


# --------------------------------------------------
def beginnings(name: str) -> List[str]:
    """Get beginnings"""

    return [name[0:i] for i in range(1, len(name) + 1)]


# --------------------------------------------------
def test_beginnings() -> None:
    """Test beginnings"""

    assert beginnings('foo') == ['f', 'fo', 'foo']


# --------------------------------------------------
def endings(name: str) -> List[str]:
    """Get ending"""

    return [name[i:] for i in range(0, len(name))]


# --------------------------------------------------
def test_endings() -> None:
    """Test endings"""

    assert endings('foo') == ['foo', 'oo', 'o']


# --------------------------------------------------
if __name__ == '__main__':
    main()
