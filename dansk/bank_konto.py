
import csv
from datetime import date
import os

csv_fil_navn = 'konto_oversigt.csv'

valuta = 'kr.'


def tilføj_indkomst(beløb, besked):
    with open(csv_fil_navn, 'a', newline='') as csvfil:
        skriver = csv.writer(csvfil)
        skriver.writerow([date.today(), beløb, '', besked])


def tilføj_udgift(beløb, besked):
    with open(csv_fil_navn, 'a', newline='') as csvfil:
        skriver = csv.writer(csvfil)
        skriver.writerow([date.today(), '', beløb, besked])


def få_sum_indkomst():
    sum = 0
    #print('Getting sum of income...')
    with open(csv_fil_navn, newline='') as csvfil:
        læser = csv.reader(csvfil)
        next(læser)
        next(læser)
        for række in læser:
            #print(f'Debug: Row: {row}')
            if række[1] != '':
                sum += int(række[1])
    return sum


def få_sum_udgift():
    sum = 0
    #print('Getting sum of expense...')
    with open(csv_fil_navn, newline='') as csvfil:
        læser = csv.reader(csvfil)
        next(læser)
        next(læser)
        for række in læser:
            #print(f'Debug: Row: {row[2]}')
            if række[2] != '':
                sum += int(række[2])
    return sum


def print_historie():
    sum = 0
    with open(csv_fil_navn, newline='') as csvfil:
        læser = csv.reader(csvfil)
        next(læser)
        next(læser)
        print()
        for række in læser:
            if række[1] != '':
                sum += int(række[1])
                besked = ændre_besked(række[3])
                print(f'Indkomst:\t{række[0]}\t{række[1]} {valuta}\t{besked}\tTotal: {sum}'.expandtabs(6))
            elif række[2] != '':
                sum -= int(række[2])
                besked = ændre_besked(række[3])
                print(f'Udgift:\t{række[0]}\t{række[2]} {valuta}\t{besked}\tTotal: {sum}'.expandtabs(6))


def ændre_besked(besked):
    if len(besked) < 7:
        ny_besked = besked
        for i in range(10-len(besked)):
            ny_besked += ' '
    elif len(besked) > 7:
        ny_besked = ''
        for i in range(7):
            ny_besked += besked[i]
        ny_besked += '...'
    return ny_besked


def print_rækker():
    with open(csv_fil_navn, newline='') as csvfil:
        læser = csv.reader(csvfil)
        for række in læser:
            print(række)


def lav_csv_fil():
    with open(csv_fil_navn, 'w') as csvfil:
        skriver = csv.writer(csvfil)
        skriver.writerow(['Indtastet:','Indkomst','Udgift','Besked'])


def slet_indhold():
    input_slet = input('Er du sikker på at slette alt indhold? (j/n)\n>')
    if input_slet == 'n':
        return
    with open(csv_fil_navn, 'w') as csvfil:
        skriver = csv.writer(csvfil)
        skriver.writerow(['Indtastet:','Indkomst','Udgift','Besked'])


def main():
    while True:
        input_start = input('\nGøre hvad? (i/u/sum/print/slet)\n>').lower()
        if input_start == 'i':
            while True:
                input_indkomst = input('Tast beløb af indkomst:\n>')
                if not input_indkomst.isdigit():
                    print('Prøv igen\n')
                else:
                    break
            input_besked = input('Tast indkomst besked:\n>')
            tilføj_indkomst(input_indkomst, input_besked)
        elif input_start == 'u':
            while True:
                input_udgift = input('Tast beløb af udgift:\n>')
                if not input_udgift.isdigit():
                    print('Prøv igen\n')
                else:
                    break
            input_besked = input('Tast udgift besked\n>')
            tilføj_udgift(input_udgift, input_besked)
        elif input_start == 'sum':
            sum = få_sum_indkomst() - få_sum_udgift()
            print(f'{sum}')
        elif input_start == 'print':
            print_historie()
        elif input_start == 'rækker':
            print_rækker()
        elif input_start == 'slet':
            slet_indhold()
        elif input_start == '':
            break
        else:
            print('Prøv igen')


if __name__ == '__main__':
    try:
        if not os.path.exists(f'./{csv_fil_navn}'):
            lav_csv_fil()
        main()
    except KeyboardInterrupt:
        print('\nLukket af bruger')
