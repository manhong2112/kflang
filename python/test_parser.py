from unittest import Test, starttest, unittest

import env
from interp import parse
from type import Quote, String


@Test
def test_parser():
    """
    New Parser
    """
    test_suite = [
        '"\\n"', String("\n"),
        '"123"', String("123"),
        '"\n"', String("\n"),
        '(printf "\\n")', ["printf", String("\n")],
        '(+ 1 1)', ["+", 1, 1],
        "		(+(+ 1				1)1		)", ["+", ["+", 1, 1], 1],
        '((+(+ 1 1) 1)(+ 1 1)(+ 1 1))', [["+", ["+", 1, 1], 1], ["+", 1, 1], ["+", 1, 1]],
        "'x", ["quote", "x"], # (quote x)
        "'(x)", ["quote", ["x"]], # (quote (x))
        "'(x (x))", ["quote", ["x", ["x"]]],
        "'((x)((x)(x))(x))", ["quote", [['x'], [['x'], ['x']], ['x']]],
        ";一個空語句會不會掛啊..", None,
        '(', SyntaxError,
        ')', SyntaxError,
        "\\", SyntaxError,
        "'", SyntaxError
    ]
    def _fun(_, y):
        a = parse(y)
        if len(a) > 0:
            return a[0]
        else:
            return None
    unittest(lambda: None, _fun, test_suite)

def main():
    starttest()

if __name__ == '__main__':
    main()
