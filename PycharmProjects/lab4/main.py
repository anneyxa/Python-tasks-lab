from divisor import greatest_common_divisor
from logicchecker import LogicExprChecker

if __name__ == '__main__':
    # print(greatest_common_divisor())
    print('--------------------------------------')
    expr_checker = LogicExprChecker("")
    print(expr_checker())  # false
    expr_checker = LogicExprChecker("a & b | a")
    print(expr_checker())  # true
    expr_checker = LogicExprChecker("((s|w)")
    print(expr_checker())  # false
    expr_checker = LogicExprChecker("~~a")
    print(expr_checker())  # true
    expr_checker = LogicExprChecker("a|&b")
    print(expr_checker())  # false
    expr_checker = LogicExprChecker("~(~a|c)&(a&b)|a|b")
    print(expr_checker())  # true
    expr_checker = LogicExprChecker("~(~aa|c)&(a&b)")
    print(expr_checker())  # false
    expr_checker = LogicExprChecker("~~1|0")
    print(expr_checker())  # true
