import applications.salary as salary
import applications.db.people as people

def print_hi(name):
    print(f'Hi, {name}')

def work():
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    work()

