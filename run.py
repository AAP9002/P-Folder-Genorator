import os
import pandas as pd
distRoot = "./dist/"

sourcePath = ''

source = pd.read_csv(sourcePath, header=1)

print(source)

# make departments
for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'][2:].strip()+'/'
    print(employeeFolder)
    if not os.path.isdir(employeeFolder):
        os.mkdir(employeeFolder)

for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'][2:].strip()+'/'+ row['Column1'].strip()+'/'
    if not os.path.isdir(employeeFolder):
        os.mkdir(employeeFolder)

for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'][2:].strip()+'/'+ row['Column1'].strip()+'/1. Contract/'
    if not os.path.isdir(employeeFolder):
        os.mkdir(employeeFolder)

for index, row in source.iterrows():
    employeeFolder = './dist/'+row['Department'][2:].strip()+'/'+ row['Column1'].strip()+'/2. Training/'
    if not os.path.isdir(employeeFolder):
        os.mkdir(employeeFolder)