import os
import pandas as pd
distRoot = "./dist/"

sourcePath = './source.csv'

source = pd.read_csv(sourcePath)

print(source)

# make departments
for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'].strip()+'/'
    if not os.path.isdir(employeeFolder):
        print(employeeFolder)
        os.mkdir(employeeFolder)

for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'].strip()+'/'+ row['Forename'].strip() + " " +row['Surname'].strip()+'/'
    if not os.path.isdir(employeeFolder):
        os.mkdir(employeeFolder)

folders = ['folder1', 'folder2', 'folder3']

for index, row in source.iterrows():
    for folder in folders:
        employeeFolder = './dist/'+row['Department'].strip()+'/'+ row['Forename'].strip() + " " +row['Surname'].strip()+'/'+folder+'/'
        if not os.path.isdir(employeeFolder):
            os.mkdir(employeeFolder)