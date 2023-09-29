print('START main')
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees


def main():
    return f'{get_employees()} - {calculate_salary()}'


print(datetime.today())

if __name__ == '__main__':
    print(main())

print('END main')
