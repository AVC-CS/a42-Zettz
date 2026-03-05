import pytest
import re

def regex_test(expected, lines):
    i = 0 ; match = 0
    for token in expected:
        for j in range(i, len(lines)):
            res = re.search(token, lines[j])
            if res is not None:
                i = j + 1
                match += 1
                break
        else:
            print(f'\033[91m Not Found: {token} \033[0m')
            assert False, f'Expect: {expected}'
    else:
        print(f'\033[91m match count: {match} \033[0m')
        assert match == len(expected), f'Expect: {expected}'


@pytest.mark.T1
def test_main_1():
    # weight=20, distance=100 -> rate=4.80, distance<=500 -> price=4.80
    with open('result1.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'4\.80'], lines)


@pytest.mark.T2
def test_main_2():
    # weight=11, distance=1000 -> rate=4.80, (1000/500)*4.80 = 9.60
    with open('result2.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'9\.60'], lines)


@pytest.mark.T3
def test_main_3():
    # weight=15, distance=2000 -> rate=4.80, (2000/500)*4.80 = 19.20
    with open('result3.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'19\.20'], lines)


@pytest.mark.T4
def test_main_4():
    # weight=5, distance=1000 -> rate=2.20, (1000/500)*2.20 = 4.40
    with open('result4.txt', 'r') as f:
        lines = f.readlines()
    print(lines)
    lines = [line.strip() for line in lines]
    regex_test([r'4\.40'], lines)
