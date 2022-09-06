#!/usr/bin/env python
# coding: utf-8

# # Doctor-Hospital Matching With Hungarian Algorithm

# Import numpy module

# In[1]:


import numpy as np  
import pandas as pd

# Input the number of doctors, hospitals and capacity of the hospital

# In[2]:
# the cap*hosp > doc

doc = int(input("Enter number of doctors:"))
hosp = int(input("Enter number of hospitals:"))
cap = int(input("Enter the capacity of the hospitals:"))


# Input the preference of each doctor

# In[3]:


preference = []
p = []
for i in range(doc):
    p = eval(input("Enter preference for doctor " + str(i+1) + ":"))
    preference.append(p)
print(preference)


# Create a matrix with doctors' preferences.

# In[4]:


matrix_1 = np.array(preference)
matrix_2 = np.tile(matrix_1,cap)
print(matrix_2)


# If the matrix is rectangular, modify it into a n x n square matrix and assign a number higher than the number of hospitals to the dummy row elements.

# In[5]:


row_num,col_num = np.shape(matrix_2)
if row_num != col_num:
    d = hosp+1
    if row_num < col_num:
        arr = np.array([d for _ in range(col_num)])
        x=np.stack([arr for _ in range(col_num-row_num)], axis=0)
        matrix_2 = np.append(matrix_2,x,axis=0)
    else:
        arr = np.array([d for _ in range(row_num)])
        x=np.stack([arr for _ in range(row_num-col_num)], axis=1)
        matrix_2 = np.append(matrix_2,x,axis=1)  
print(matrix_2)


# Now the hungarian algorithm is implemented. 
# 
# Subtract row minima and row maxima

# In[6]:


row_num,col_num = np.shape(matrix_2)
for r in range(row_num):
    matrix_2[r,:]=matrix_2[r,:]-np.min(matrix_2[r,:])

for cl in range(col_num):
    matrix_2[:,cl]=matrix_2[:,cl]-np.min(matrix_2[:,cl])
    
print(matrix_2)


# Cover all zeros with a minimum number of lines, create additional zeros if the number of lines is less than n. Optimal assignment is then implemented.

# In[7]:


zero_index = np.argwhere(matrix_2 == 0)
print(zero_index)


# In[8]:

# find the zero which have the same row or col with other zero. then they should be covered by the same line

list_x =[]
list_y = []

for i in range(len(zero_index)):

    for j in range(i + 1 ,len(zero_index)):
        if zero_index[i,0] == zero_index[j,0]:
            
            list_x.append(zero_index[i,0])
            n =  1
        elif zero_index[i,1] == zero_index[j,1]:
            n = 1
            list_y.append(zero_index[i,1])


# In[9]:


#determine the end
def end_loop(matrix_2):
#mark different zero. Then find if every row has a zero to determine the end of loop

    row_uncovered = np.ones(row_num, dtype=bool)
    col_uncovered = np.ones(col_num, dtype=bool)

    marked = np.zeros((row_num, col_num), dtype=int)

    for i, j in zip(*np.where(matrix_2 == 0)):
        if col_uncovered[j] and row_uncovered[i]:
            marked[i, j] = 1
            col_uncovered[j] = False
            row_uncovered[i] = False

    row_uncovered[:] = True
    col_uncovered[:] = True

    marked = (marked == 1)
    col_uncovered[np.any(marked, axis=0)] = False

    if marked.sum() < row_num:
        return 1
    else:
        return 0
    
flag = end_loop(matrix_2)
print(flag)


# In[10]:


#optimal assignment

def same_row_col(zero_index):
    list_m =[]
    list_n = []

# find zero has the same row and col with other.
    for i in range(len(zero_index)):
        for j in range(i+1 ,len(zero_index)):
            if zero_index[i,0] == zero_index[j,0]:          
                list_m.append(zero_index[i,0])
            elif zero_index[i,1] == zero_index[j,1]:
                list_n.append(zero_index[i,1])

    
           
# find the zero doesn't is single. So it must be output
    list_a = []
    list_b = []
    for i in range(len(zero_index)):
        if not(zero_index[i,0] in list_m and zero_index[i,1] in list_n):
            list_a.append(zero_index[i,0])
            list_b.append(zero_index[i,1])
 
# find the other zero to output

    for i in range(len(zero_index)):
        for j in range(i+1 ,len(zero_index)):
            if zero_index[i,0] in list_m and zero_index[i,1] in list_n:          
                list_a.append(zero_index[i,0])
                list_b.append(zero_index[i,1])
                list_m.remove(zero_index[i,0])
                list_n.remove(zero_index[i,1])
 
                

    return list_a, list_b

                
# output the optimal assignment        

def final_assignment(matrix_3):
    zero_index = np.argwhere(matrix_3 == 0)
    
    list_doctor = []
    list_hospital = []


    list_doctor, list_hospital = same_row_col(zero_index)

 
    return list_doctor, list_hospital


# In[11]:

# if flag == 0 , it means that we have the optimal assignment. So we can end the loop. Then we can output the optimal assignment.

if flag:

    while (flag):

#this is the step to update matrix following the step on the internet

        #find the single zero index, not in the same row or same col with other zero, these zero can use either its row or line but not cover the min uncovered number

        list_single_x = []
        list_single_y = []
        for i in range(len(zero_index)):
            if zero_index[i,0] not in list_x and zero_index[i,1] not in list_y:
                list_single_x.append(zero_index[i,0])
                list_single_y.append(zero_index[i,1])
                

        
        #find the min uncovered number and its index

        min_update = matrix_2.max()
        min_row_index = 0
        min_col_index = 0
        for i in range(row_num):
            for j in range(col_num):
                if i not in list_x and j not in list_y:
                    if matrix_2[i,j]!=0 and matrix_2[i,j] < min_update:
                        min_update = matrix_2[i,j]
                        min_row_index = i
                        min_col_index = j
            
    
        
        #find the min uncovered number and its index

        min_update = matrix_2.max()
        min_row_index = 0
        min_col_index = 0
        for i in range(row_num):
            for j in range(col_num):
                if i not in list_x and j not in list_y:
                    if matrix_2[i,j]!=0 and matrix_2[i,j] < min_update:
                        min_update = matrix_2[i,j]
                        min_row_index = i
                        min_col_index = j
            
   
        # determine row or col of single zero which to use, and figure out the covered rows and cols
        for i in range(len(list_single_x)):
            if list_single_x[i] == min_row_index:
                list_y.append(list_single_y[i])
            else:
                list_x.append(list_single_x[i])
      
        
        #substract the min num from all uncovered elements and add it to all elements that are covered twice. Then get the updated matrix.
       
        for i in range(row_num):
            for j in range(col_num):
                if i in list_x and j in list_y:
                    matrix_2[i,j] = matrix_2[i,j] + min_update
                elif i not in list_x and j not in list_y:
                    matrix_2[i,j] = matrix_2[i,j] - min_update
                    
        flag = end_loop(matrix_2)


# 

# In[12]:

# output the optimal assignment with the dummy number

doc_final, hosp_final = final_assignment(matrix_2)


# In[13]:

# remove the dummy number and get the final output
doc_final = [x+1 for x in doc_final]
hosp_final = [x+1 for x in hosp_final]
print(doc_final[:doc],hosp_final[:doc])

# show the data clearly

doc_final = [x+1 for x in doc_final]
hosp_final = [x+1 for x in hosp_final]
doc_final = doc_final[:doc]
hosp_final = hosp_final[:doc]
print(doc_final, hosp_final)
df = pd.DataFrame({'Doctor' : doc_final[:doc], 'Hospital' : hosp_final[:doc]})   
print(df)

"""Some challenges we faced while implementing this algorithm were including the capacity of hospitals and an infinite loop during step 3 of the Hungarian algorithm.
There are a few pitfalls in the method and code that can be improved. They are as follows:
1) Only same capacity for all hospitals can be implemented.
2) When the hospital capacity is more and more doctors prefer a particular hospital,there might be cases where some hospitals are not assigned any doctors.
3) The code of Hungarian algorithm implemented here can be further optimised for larger matrices as overflow errors are possible. """
