loan_money = 1000000
number_loan_year = 10
number_loan_month = 12 * number_loan_year
year_lpr = 4.65 / 100
month_lpr = year_lpr / 12


def rande45(value):
    from decimal import Context
    rounding = "ROUND_HALF_UP"
    r = str(value).find(".")
    value = str(value)[:r + 5]
    res = float(Context(prec=r + 4, rounding=rounding).create_decimal(value))
    return res


# 等额本息 Equal principal and interest
def equal_principal_interest_tool(money: float, monthlpr: float, loan_month: int) -> list:
    # 还款总信息
    month_pay_list = []
    # 每月还款总额
    month_pay = rande45((money * monthlpr * (1 + monthlpr) ** loan_month) / ((1 + monthlpr) ** loan_month - 1))

    # 当期后剩余贷款金额
    def now_left_loan_money():

        left_loan_money = money * (1 + monthlpr) - month_pay
        return rande45(left_loan_money)

    # 当期利息
    def now_interest():
        nonlocal money
        interest = money * monthlpr
        money = now_left_loan_money()
        return interest

    for k in range(loan_month):

        # 剩余贷款金额
        left_loan_money = rande45(now_left_loan_money())
        # 当期利息
        interest = rande45(now_interest())
        # 本期本金
        principal = rande45(month_pay - interest)

        if principal > left_loan_money:
            left_loan_money = 0

        month_pay_list.append([k + 1, month_pay, principal, interest, left_loan_money])

    return month_pay_list


# 等额本金 Equal principal
def equal_principal(money, monthlpr, loan_month):
    month_pay = (money / loan_month) + (money - 0) * monthlpr
    return month_pay


def print_format(repayment_infos: list):
    for k in repayment_infos:
        print(k)


# print_format(equal_principal_interest(loan_money, month_lpr, number_loan_month))
