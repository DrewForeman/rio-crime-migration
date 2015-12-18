import csv
import os
import glob

main_dir = '/Users/drewforeman/Documents/rioexp/Estadual_Data/*'


def access_murders(file):
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        murders = [float(alldata[6][5]), float(alldata[6][7]), float(alldata[6][9]), float(alldata[6][11])]
    return murders



def access_drugs(file):                                                                 #need to fix this one so that it reads the two dif lines 
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        if alldata[38][0] == '':
            drugs = [alldata[41][5], alldata[41][7], alldata[41][9], alldata[41][11]]
        else:
            drugs = [alldata[40][5], alldata[40][7], alldata[40][9], alldata[40][11]]
    return drugs



def access_arms(file):
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        if alldata[38][0] == '':
            arms = arms = [alldata[40][5], alldata[40][7], alldata[40][9], alldata[40][11]]
        else:
            arms = [alldata[39][5], alldata[39][7], alldata[39][9], alldata[39][11]]
    return arms



def access_AdR(file):
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        if alldata[38][0] == '':
            AdR = [float(alldata[50][5]), float(alldata[50][7]),float(alldata[50][9]), float(alldata[50][11])]
        else:
            AdR = [float(alldata[49][5]), float(alldata[49][7]),float(alldata[49][9]), float(alldata[49][11])]
    return AdR


def access_furtos(file):
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        if alldata[38][0] == '':
            furtos = [alldata[56][5], alldata[56][7], alldata[56][9], alldata[56][11]]
        else:
            furtos = [alldata[55][5], alldata[55][7], alldata[55][9], alldata[55][11]]
    return furtos



def access_roubos(file):
    with open(file) as f1:
        alldata = csv.reader(f1)
        alldata = list(alldata)
        if alldata[38][0] == '':
            roubos = [alldata[55][5], alldata[55][7], alldata[55][9], alldata[55][11]]
        else:
            roubos = [alldata[54][5], alldata[54][7], alldata[54][9], alldata[54][11]]
    return roubos



def agg_data(file,function):
    # new_list = []

    files=glob.glob(main_dir)   
    new_list = []
    for file in files: 
        if file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual.py' \
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_murders.csv'\
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_drugs.csv'\
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_roubos.csv'\
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_furtos.csv'\
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_AdR.csv'\
        and file != '/Users/drewforeman/Documents/rioexp/Estadual_Data/estadual_arms.csv':

        # print file 
            value = function(file)
            new_list.append(value)

    return new_list


def clean_strdata(given_list):                                                      # fixes the problem of data that has tabs and commas
    clean_list = []                                                                 # and cannot be read as a float
    for pt in given_list:
        sub_list = []
        for item in pt:
            item = list(item)
            for i in item:
                if i == '\t' or i == ',' or i ==' ':
                    item.remove(i)
            sub_list.append(float(''.join(item)))
        clean_list.append(sub_list)
    return clean_list

    # return new_list

# print agg_data(main_dir)

murder_data = agg_data(main_dir,access_murders)
murder_titles = ['Capital Murder', 'Baixada Murder', 'Niteroi Murder', 'Interior Murder']
print murder_titles
print murder_data,'\n'

with open("estadual_murders.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(murder_titles)
    writer.writerows(murder_data)



drugs_data = clean_strdata(agg_data(main_dir,access_drugs))
drugs_titles = ['Capital Drugs', 'Baixada Drugs', 'Niteroi Drugs', 'Interior Drugs']
print drugs_titles
print drugs_data,'\n'

with open("estadual_drugs.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(drugs_titles)
    writer.writerows(drugs_data)



arms_data = clean_strdata(agg_data(main_dir,access_arms))
arms_titles = ['Capital Arms', 'Baixada Arms', 'Niteroi Arms', 'Interior Arms']
print arms_titles
print arms_data,'\n'

with open("estadual_arms.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(arms_titles)
    writer.writerows(arms_data)



AdR_data = agg_data(main_dir,access_AdR)
AdR_titles = ['Capital AdR', 'Baixada AdR', 'Niteroi AdR', 'Interior AdR']
print AdR_titles
print AdR_data,'\n'

with open("estadual_AdR.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(AdR_titles)
    writer.writerows(AdR_data)



furtos_data = clean_strdata(agg_data(main_dir,access_furtos))
furtos_titles = ['Capital Furtos', 'Baixada Furtos', 'Niteroi Furtos', 'Interior Furtos']
print furtos_titles
print furtos_data,'\n'

with open("estadual_furtos.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(furtos_titles)
    writer.writerows(furtos_data)



roubos_data = clean_strdata(agg_data(main_dir,access_roubos))
roubos_titles = ['Capital Roubos', 'Baixada Roubos', 'Niteroi Roubos', 'Interior Roubos']
print roubos_titles
print roubos_data,'\n'

with open("estadual_roubos.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerow(roubos_titles)
    writer.writerows(roubos_data)




