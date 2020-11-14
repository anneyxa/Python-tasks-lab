from divisor import greatest_common_divisor
from logicchecker import LogicChecker

if __name__ == '__main__':
    # print(greatest_common_divisor())
    print('--------------------------------------')
    expr_checker = LogicChecker("")
    print(expr_checker())  # false
    expr_checker = LogicChecker("a & b | a")
    print(expr_checker())  # true
    expr_checker = LogicChecker("((s|w)")
    print(expr_checker())  # false
    expr_checker = LogicChecker("~~a")
    print(expr_checker())  # true
    expr_checker = LogicChecker("a|&b")
    print(expr_checker())  # false
    expr_checker = LogicChecker("~(~a|c)&(a&b)|a|b")
    print(expr_checker())  # true
    expr_checker = LogicChecker("~(~aa|c)&(a&b)")
    print(expr_checker())  # false
