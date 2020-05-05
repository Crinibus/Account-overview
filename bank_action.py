
import csv
from datetime import date
import os

csv_file_name = 'account_overview.csv'

currency = 'USD'


def add_income(amount, message):
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date.today(), amount, '', message])


def add_expense(amount, message):
    with open(csv_file_name, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date.today(), '', amount, message])


def get_sum_income():
    sum = 0
    #print('Getting sum of income...')
    with open(csv_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        next(reader)
        for row in reader:
            #print(f'Debug: Row: {row}')
            if row[1] != '':
                sum += int(row[1])
    return sum


def get_sum_expense():
    sum = 0
    #print('Getting sum of expense...')
    with open(csv_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        next(reader)
        for row in reader:
            #print(f'Debug: Row: {row[2]}')
            if row[2] != '':
                sum += int(row[2])
    return sum


def print_history():
    sum = 0
    with open(csv_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        next(reader)
        print()
        for row in reader:
            if row[1] != '':
                sum += int(row[1])
                message = change_message(row[3])
                print(f'Income:\t{row[0]}\t{row[1]} {currency}\t{message}\tTotal: {sum}'.expandtabs(6))
            elif row[2] != '':
                sum -= int(row[2])
                message = change_message(row[3])
                print(f'Expense:\t{row[0]}\t{row[2]} {currency}\t{message}\tTotal: {sum}'.expandtabs(6))


def change_message(message):
    if len(message) < 7:
        new_message = message
        for i in range(10-len(message)):
            new_message += ' '
    elif len(message) > 7:
        new_message = ''
        for i in range(7):
            new_message += message[i]
        new_message += '...'
    return new_message


def print_rows():
    with open(csv_file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)


def create_csv_file():
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Entered:','Income','Expense','Message'])


def delete_content():
    input_delete = input('Are you sure to delete all content? (y/n)\n>')
    if input_delete == 'n':
        return
    with open(csv_file_name, 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Entered:','Income','Expense','Message'])


def main():
    while True:
        input_start = input('\nWhat todo? (i/e/sum/print/d)\n>').lower()
        if input_start == 'i':
            while True:
                input_income = input('Enter amount of income:\n>')
                if not input_income.isdigit():
                    print('Try again\n')
                else:
                    break
            message_input = input('Enter income message:\n>')
            add_income(input_income, message_input)
        elif input_start == 'e':
            while True:
                input_expense = input('Enter amount of expense:\n>')
                if not input_expense.isdigit():
                    print('Try again\n')
                else:
                    break
            message_input = input('Enter income message\n>')
            add_expense(input_expense, message_input)
        elif input_start == 'sum':
            sum = get_sum_income() - get_sum_expense()
            print(f'{sum}')
        elif input_start == 'print':
            print_history()
        elif input_start == 'rows':
            print_rows()
        elif input_start == 'd':
            delete_content()
        elif input_start == '':
            break
        else:
            print('Try again')


if __name__ == '__main__':
    try:
        if not os.path.exists(f'./{csv_file_name}'):
            create_csv_file()
        main()
    except KeyboardInterrupt:
        print('\nClosed by user')
