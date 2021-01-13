import cs50
import sys
import csv

STRList = []
LargestSTR = []
consecutive = []
# main function to consolidate all functions and execute program


def main():
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")

    else:
        data = sys.argv[1]
        sequence = sys.argv[2]
        extract(data)

        for i in range(0, len(STRList)):
            LargestSTR.append(largest(STRList[i], sequence))

        compare(data)


# function to extract the STRs provided by the database


def extract(database):
    with open(database, 'r') as file:
        reader = csv.reader(file)

        # loop to find the number of STRs
        for row in reader:
            length = len(row[0]) - 1

        file.seek(0)
        line1 = next(reader)

        # loop to store STR names in the STRList
        for i in range(1, len(line1)):
            STRList.append(line1[i])


# function to find the largest consecutive occurrence of a specific STR in given sequence


def largest(STR, seq):
    file = open(seq, 'r')
    contents = file.read()

    # create null list that is the size of sequence
    for i in range(0, len(contents)):
        consecutive.append(0)

    # loop to call countconsec for each position in sequence
    for i in range(0, len(contents)):
        consecutive[i] = countconsec(STR, contents[i:])

    file.close()
    return max(consecutive)


# function to find the consecutive occurences of thread in sequence from its start


def countconsec(thread, seq):

    threadlen = len(thread)
    count = 0

    # loop to find number of consecutive occurrences
    for i in range(0, len(seq), threadlen):
        if thread == seq[i: i + threadlen]:
            count += 1
        else:
            return count
    return count


# function to compare the list of largest STR for given sequence with csv file to find match


def compare(dnabase):
    with open(dnabase, 'r') as csv_file:

        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        flag = False
        counter = 0

        # loop to iterate through each row of the csv file
        for row in csv_reader:
            # loop to iterate through every value in the corresponding row and comparing with list
            for i in range(1, len(row)):
                if int(row[i]) == LargestSTR[i - 1]:
                    flag = True
                else:
                    flag = False
                    break

            if flag == True:
                print(row[0])
                counter = 1

        if counter == 0:
            print("No match")


main()
