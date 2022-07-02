from application.salary import calculate_salary
from application.people import get_employees
from datetime import datetime

def main():
    calculate_salary()
    get_employees()
    print(f'Текущая дата и время ------> {datetime.today()}')


if __name__ == '__main__':
    main()