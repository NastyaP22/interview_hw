from stack import Stack


def compare(top_sign: str, next_sign: str) -> bool:
    opens = '([{'
    closers = ')]}'
    return opens.index(top_sign) == closers.index(next_sign)


def test_balance(signs_str: str) -> str:
    test_balance = Stack([])
    if len(signs_str) % 2 != 0:
        return "Несбалансированно"
    balanced = True
    index = 0
    while index < len(signs_str) and balanced:
        next_sign = signs_str[index]
        if next_sign in '([{':
            test_balance.push(next_sign)
        else:
            if test_balance.is_empty():
                balanced = False
            else:
                top_sign = test_balance.pop()
                if not compare(top_sign, next_sign):
                    balanced = False
        index += 1
    if balanced and test_balance.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    print(test_balance('(((([{}]))))'))
    print(test_balance('[([])((([[[]]])))]{()}'))
    print(test_balance('{{[()]}}'))
    print(test_balance('}{}'))
    print(test_balance('{{[(])]}}'))
    print(test_balance('[[{())}]'))