# Sukurti programa, kuria paleidu priimtu du parametrus islaidas ir iplaukas
# Programat turi paskaiciuoti islaidu ir imoku vidurkius, metu.
# Paskaiciuoti vienos dienos vidurkius
# Pajamu ir islaidu santykius proc
# Pajamu ketvircio rezultatus
# Pusmecio islaidu rezultatus
# Viska suloginti

import logging

logging.basicConfig(filename='accounting.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')


class Accountant:
    def monthly_average(self, amount: float) -> float:
        logging.info(f'Receipt amount of monthly average calculation: {amount/12}')
        return amount/12
    def daily_average(self, amount: float) -> float:
        return amount /365
    def ratio(self, income: float, expenses: float) -> float:
        return round(income/expenses, 2)

class Income(Accountant):
    def __init__(self, income: float):
        self.income = income
    def quoterly_income(self) -> float:
        return self.income / 4

class Expenses(Accountant):
    def __init__(self, expenses:float):
        self.expenes = expenses
    def half_year_expenses(self) -> float:
        return self.expenes / 2


def main() -> None:
    income = float(input('Enter your yearly income '))
    expenses = float(input('Enter your yearly expenses '))
    logging.info(f'log entered income amount: {income}')
    logging.info(f'log entered expenses amoun: {expenses}')
    inc = Income(income)
    exp = Expenses(expenses)
    print(f'quoterly income: {inc.quoterly_income()}')
    print(f'daily expenses: {exp.daily_average(expenses)}')




if __name__ == '__main__':
    main()
    