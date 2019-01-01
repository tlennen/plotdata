"""This is a project to take in .csv files and plot them with a best fit line."""
import csv

def create_function_dataset():
    with open('test.csv', mode='w') as csv_file:
        fieldnames = ['x-position','y-position']
        plot_t = csv.DictWriter(csv_file, delimiter=',', quotechar='"',
                                lineterminator='\n',quoting=csv.QUOTE_MINIMAL,fieldnames=fieldnames)
        for x in range(-100,100):
            plot_t.writerow({'x-position':x,'y-position':x})
            """Models y=x, can be made into other functions"""

if __name__ == '__main__':
    create_function_dataset()