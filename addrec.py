import pandas as pd
import csv
import createpdf


def reformat(target_file):
    f1 = open(target_file, 'r', newline="")
    fname = target_file.removeprefix("registers/")
    fname = fname.removesuffix(".csv")
    print(fname)
    f2 = open('registers/temp.csv', 'w', newline="")
    myreader = csv.reader(f1)
    mywriter = csv.writer(f2)
    check = 0
    for i in myreader:
        if check == 1:
            mywriter.writerow(i)
        if i[0] == "Student/Subject":
            check = 1
            if target_file[:12] == 'registers/12':
                x = ["S. No", "Student name", "Admission number"]
                for j in range(3, len(i), 4):
                    x.append(i[j] + "UT1")
                    x.append(i[j] + "UT2")
                    x.append(i[j] + "TM1")
                    x.append('Del')
                mywriter.writerow(x)

            else:
                x = ["S. No", "Student name", "Admission number"]
                step = 4
                # dynamically add value of step here due to new registers having more criteria for marking total (basically del kitni jagah daalna hai)
                for j in range(3, len(i), step):
                    x.append("Del")
                    x.append("Del")
                    x.append("Del")
                    x.append(i[j])
                mywriter.writerow(x)
    f1.close()
    f2.close()
    data = pd.read_csv('registers/temp.csv', sep=',')
    filtered_cols = [i for i in data.columns if not i.startswith("Del") if not i.startswith("S.")]
    print('hi')
    print(filtered_cols)
    data[filtered_cols].to_csv('registers/' + fname + '_rf.csv')
    return 'registers/' + fname + '_rf.csv'


def makedict(filename):
    data = pd.read_csv(filename)
    data = data.to_dict(orient='records')
    for i in data:
        tempx = []
        for j in i.keys():
            if i[j] != i[j]:
                tempx.append(j)

        for j in tempx:
            del i[j]

    return data[1:]
    # for i in data[1:]:
    #    print(i)
    # print(data)
    # ----------- Adding after module is made ---------------


# test program loop that generates pdfs in results folder (working now)
def grade9(filename_p):
    data_test = makedict(filename_p)
    for i in data_test:
        for j in i.keys():
            if type(i[j]) is str:
                i[j] = i[j][0:-3]
    for i in range(1, len(data_test)):
        data_values_test = list(data_test[i].values())
        nameandfile = data_values_test[1]
        createpdf.createpdfs_grade9(nameandfile.upper(), data_test[i], nameandfile)


def grade11(filename_p):
    data_test = makedict(filename_p)
    for i in data_test:
        for j in i.keys():
            if type(i[j]) is str:
                i[j] = i[j][0:-3]
    print(data_test)
    for i in range(1, len(data_test)):
        data_values_test = list(data_test[i].values())
        nameandfile = data_values_test[1]
        createpdf.createpdfs_grade11(nameandfile.upper(), data_test[i], nameandfile)


def grade12(filename_p):
    selectedtest = None
    filename = filename_p
    data_test = makedict(filename)
    cl = choices()
    data_test = c_implement(data_test, cl)
    for i in data_test:
        for j in i.keys():
            if type(i[j]) is str:
                i[j] = i[j][0:-3]
    print(data_test)
    for i in range(1, len(data_test)):
        data_values_test = list(data_test[i].values())
        nameandfile = data_values_test[1]
        createpdf.createpdfs_grade12(nameandfile.upper(), data_test[i], nameandfile)


def choices():
    filename = 'choices/Transcripts form.csv'
    data = pd.read_csv(filename)
    data = data.to_dict(orient='records')
    choicelist = []
    templist = []
    for i in data:
        for j in i:
            if j != 'Timestamp' and j != 'Username':
                templist.append(i[j].strip())
            if i[j] in ['UT1', 'UT2', 'TERM1']:
                choicelist.append(templist)
                templist = []

    return choicelist


def c_implement(reglist, clist):
    cdict = {}
    for i in reglist:
        for j in clist:
            if i['Student name'].lower() == j[0].lower():
                cdict[i['Student name']] = j[2]
                break
            else:
                cdict[i['Student name']] = 'TERM1'

    newreg = []
    treg = {}
    keylist = list(reglist[0].keys())
    print(keylist)
    ut1k = [i for i in keylist if not i.endswith('UT1') if not i in ['Unnamed: 0', 'Student name', 'Admission number']]
    ut2k = [i for i in keylist if not i.endswith('UT2') if not i in ['Unnamed: 0', 'Student name', 'Admission number']]
    tm1k = [i for i in keylist if not i.endswith('TM1') if not i in ['Unnamed: 0', 'Student name', 'Admission number']]

    for i in reglist:
        if cdict[i['Student name']] == 'UT1':
            for j in ut1k:
                del i[j]
        if cdict[i['Student name']] == 'UT2':
            for j in ut2k:
                del i[j]
        if cdict[i['Student name']] == 'TERM1':
            for j in tm1k:
                del i[j]

    return(reglist)

