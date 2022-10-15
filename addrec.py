import pandas as pd
import csv
import createpdf

def reformat():
    f1 = open('registers/IX F T1.csv', 'r', newline="")
    f2 = open('registers/temp.csv', 'w', newline="")
    myreader = csv.reader(f1)
    mywriter = csv.writer(f2)
    check = 0
    for i in myreader:
        if check == 1:
            mywriter.writerow(i)
        if i[0] == "Student/Subject":
            check = 1
            x = ["S. No", "Student name", "Admission number"]
            for j in range(3, len(i), 4):
                x.append("Del")
                x.append("Del")
                x.append("Del")
                x.append(i[j])
            print(x)
            mywriter.writerow(x)
    f1.close()
    f2.close()
    data = pd.read_csv('registers/temp.csv', sep=',')
    filtered_cols = [i for i in data.columns if not i.startswith("Del") if not i.startswith("S.")]
    data[filtered_cols].to_csv('registers/IX F T1 rf.csv')


def makedict():
    data = pd.read_csv('registers/IX F T1 rf.csv')
    data = data.to_dict(orient='records')
    return data
    #for i in data[1:]:
    #    print(i)
    #print(data)
        # ----------- Adding after module is made ---------------

# test program loop that generates pdfs in results folder (working now)
def grade9():
    data_test= makedict()
    for i in range(1,len(data_test)):
            data_values_test = list(data_test[i].values())
            nameandfile = data_values_test[1]
            createpdf.createpdfs_grade9(nameandfile.upper(),data_test[i],nameandfile)

grade9()