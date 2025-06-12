import pandas as pd

file_path = "C:/Users/User/OneDrive/Desktop/Project AI/data/AI Questions.xlsx"
result_df = pd.DataFrame()

D8c = "D8c"
df = pd.read_excel(file_path, sheet_name=D8c, header=8)
df = df.drop(columns=['<<Back to content', "UE27\nEU27"], errors='ignore')  

education = ["Bachelor or equivalent", "Master or equivalent", "Doctoral or equivalent"]

for level in education: 
    row = df.loc[df.apply(lambda row: row.astype(str).str.contains(level).any(), axis=1)]
        
    if not row.empty:
        numeric_values = row.iloc[0, 1:].values
        
        result_df[level] = numeric_values

#--- In your view, what impact do the most recent digital tech, including AI cunrrently have on your current job? ---#
QB1_4 = ["QB1_4"]
for sheet in QB1_4:
    df = pd.read_excel(file_path, sheet_name=sheet, header=8)
    df = df.drop(columns=['<<Back to content', "UE27\nEU27"], errors='ignore')
    
    row = df.loc[df.apply(lambda row: row.astype(str).str.contains("Total 'Positive'").any(), axis=1)]
        
    if not row.empty:
        numeric_values = row.iloc[0, 1:].values
        
        result_df[f"{sheet} Total 'Positive'"] = numeric_values


# --- 1. Due to the use of robots and Artificial Intelligence, more jobs will disappear than new jobs will be created --- #
#---  2. Robots and Artificial Intelligence are a good thing for society, because they help people do their jobs or carry out daily tasks at home ---# 
# --- 3. Robots and Artificial Intelligence are technologies that require careful management --- #
# --- 4. Artificial Intelligence is necessary as it can do jobs that are seen as boring or repetitive --- #
# --- 5. Robots and Artificial Intelligence steal peoples' jobs --- #
# --- 6. Robots and Artificial Intelligence increase the pace at which workers complete tasks --- #
# --- 7. Robots and Artificial Intelligence have a negative impact on communication between colleagues --- #
# --- 8. Robots and Artificial Intelligence can be used to make accurate decisions in the workplace --- #

QB6 = ["QB6_1", "QB6_2", "QB6_3", "QB6_4", "QB6_5", "QB6_6", "QB6_7", "QB6_8"]

for sheet in QB6:
    df = pd.read_excel(file_path, sheet_name=sheet, header=8)
    df = df.drop(columns=['<<Back to content', "UE27\nEU27"], errors='ignore')
    
    row = df.loc[df.apply(lambda row: row.astype(str).str.contains("Total 'Agree'").any(), axis=1)]
    
    row = row.loc[row.iloc[:, 1:].apply(lambda x: pd.to_numeric(x, errors='coerce').lt(1).all(), axis=1)]
    
    if not row.empty:
        numeric_values = row.iloc[0, 1:].values
        
        result_df[f"{sheet} Total 'Agree'"] = numeric_values


# --- How important, if at all, do you think the following rules would be in addressing risks and maximizing the benefits of digital technologies, including AI, in the workplace?--- #
#--- 1. protecting workers privacy ---#
#--- 2. prohibiting automated decision making ---#
#--- 3. limitng auotmated monitoring people ---#
#--- 4. Enforcing more transparency in the use of digital technologies to handle HR decision-making ---#
#--- 5. Involving workers and their representatives in the design and adoption of new technologies ---#
QB11 = ["QB11_1", "QB11_2", "QB11_3", "QB11_4", "QB11_5"]

for sheet in QB11:
    df = pd.read_excel(file_path, sheet_name=sheet, header=8)
    df = df.drop(columns=['<<Back to content', "UE27\nEU27"], errors='ignore')
    
    row = df.loc[df.apply(lambda row: row.astype(str).str.contains("Total 'Important'").any(), axis=1)]
    
    row = row.loc[row.iloc[:, 1:].apply(lambda x: pd.to_numeric(x, errors='coerce').lt(1).all(), axis=1)]
    
    if not row.empty:
        numeric_values = row.iloc[0, 1:].values
        
        result_df[f"{sheet} Total 'Important'"] = numeric_values


# ---  Gathering additional information on applicants for a job --- # 
# --- Selecting applicants for a job --- #
# --- Allocating tasks to workers or managing their working schedules and shifts --- #
# --- Collecting, processing, and storing workers' personal data --- #
# --- Improving workers' safety and security --- # 
# --- Monitoring workers ---#
# --- Assessing workers' performance --- #
# --- Automatically firing workers --- #
QB8 = ["QB8_1", "QB8_2", "QB8_3", "QB8_4", "QB8_5", "QB8_6", "QB8_7", "QB8_8"]

for sheet in QB8:
    df = pd.read_excel(file_path, sheet_name=sheet, header=8)
    df = df.drop(columns=['<<Back to content', "UE27\nEU27"], errors='ignore')
    
    row = df.loc[df.apply(lambda row: row.astype(str).str.contains("Total 'Positively'").any(), axis=1)]
    
    row = row.loc[row.iloc[:, 1:].apply(lambda x: pd.to_numeric(x, errors='coerce').lt(1).all(), axis=1)]
    
    if not row.empty:
        numeric_values = row.iloc[0, 1:].values
        
        result_df[f"{sheet} Total 'Positively'"] = numeric_values


#--- HANDLING NULL VALUES ---#
from sklearn.impute import KNNImputer
from sklearn.metrics import mean_squared_error
import numpy as np

result_df.replace("-", np.nan, inplace=True)
df = result_df.apply(pd.to_numeric, errors='coerce')

imputer = KNNImputer(n_neighbors=2)
df = pd.DataFrame(imputer.fit_transform(result_df), columns=result_df.columns, index=result_df.index)
df.to_excel("data/education_data.xlsx", index=False)
