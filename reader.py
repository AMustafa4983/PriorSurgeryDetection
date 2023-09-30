import pandas as pd 

df = pd.read_csv('/home/abdelrahman/Desktop/Dr. Tim/new/radiology_report_gt.csv')

c = 0
for text in df['Text']:
    with open(f'/home/abdelrahman/Desktop/Dr. Tim/new/reports/report_{c}.txt', 'w') as f:
        f.write(text)
    c+=1