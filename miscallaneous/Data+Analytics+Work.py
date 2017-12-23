
# coding: utf-8

# In[3]:


import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
sns.set()
from matplotlib.backends.backend_pdf import PdfPages
#from mpl_toolkits.basemap import Basemap
import matplotlib.cm as cm
import matplotlib.colors as col
import matplotlib as mpl


# In[ ]:


##OCEAN Scoring

##Openness to Experience
##Conscientiousness (Work Ethic)
##Extraversion
##Agreeableness
##Natural Reactions

##Each facet will have a score from 0-100
##[0,45] : Low
##[46,55] : Medium
##[56,100] : High

#Sample Score: 45    37   61   16   65
#Interpretation: O: (Low) Not very open-minded, traditionalist
#               C: (Low) Not very disciplined work ethic, prefers flexible plans, disorganized
#               E: (High) Very extraverted, outgoing, socially oriented
#               A: (Low) Hard-headed, stubborn
#               N: (High) Easily upset, prone to worry, experiences high amounts of negative emotions


# In[4]:


psycho_data = pd.read_csv("../work/psychometric_info.csv")


# In[58]:


psycho_data.head(42)


# In[61]:


data = pd.DataFrame(index = range(0,len(psycho_data)),columns = ["employee_name","user_id","O","C","E","A","N"])
data.head()


# In[125]:


##Score Ranges
## 0 : Low
## 1 : Mid
## 2 : High


# In[136]:


higho=0
mido = 0
lowo = 0

for i in range(0,len(psycho_data)):
    if (psycho_data.O[i] >=56):
        data.employee_name[i] = psycho_data.employee_name[i]
        data.user_id[i] = psycho_data.user_id[i]
        data.O[i] = int(2)
        higho = higho + 1
    elif ((psycho_data.O[i]>=46)&(psycho_data.O[i] < 56)):
        data.employee_name[i] = psycho_data.employee_name[i]
        data.user_id[i] = psycho_data.user_id[i]
        data.O[i] = int(1)
        mido = mido + 1
    elif (psycho_data.O[i] < 46):
        data.employee_name[i] = psycho_data.employee_name[i]
        data.user_id[i] = psycho_data.user_id[i]
        data.O[i] = int(0)
        lowo = lowo + 1


# In[137]:


highc=0
midc = 0
lowc = 0

for i in range(0,len(psycho_data)):
    if (psycho_data.C[i] >=56): 
        data.C[i] = int(2)
        highc = highc + 1
    elif ((psycho_data.C[i]>=46)&(psycho_data.C[i] < 56)):
        data.C[i] = int(1)
        midc = midc + 1
    elif (psycho_data.C[i] < 46):
        data.C[i] = int(0)
        lowc = lowc + 1


# In[138]:


highe=0
mide = 0
lowe = 0

for i in range(0,len(psycho_data)):
    if (psycho_data.E[i] >=56): 
        data.E[i] = int(2)
        highe = highe + 1
    elif ((psycho_data.E[i]>=46)&(psycho_data.E[i] < 56)):
        data.E[i] = int(1)
        mide = mide + 1
    elif (psycho_data.E[i] < 46):
        data.E[i] = int(0)
        lowe = lowe + 1


# In[139]:


higha=0
mida = 0
lowa = 0

for i in range(0,len(psycho_data)):
    if (psycho_data.A[i] >=56): 
        data.A[i] = int(2)
        higha = higha + 1
    elif ((psycho_data.A[i]>=46)&(psycho_data.A[i] < 56)):
        data.A[i] = int(1)
        mida = mida + 1
    elif (psycho_data.A[i] < 46):
        data.A[i] = int(0)
        lowa = lowa + 1


# In[140]:


highn=0
midn = 0
lown = 0

for i in range(0,len(psycho_data)):
    if (psycho_data.N[i] >=56): 
        data.N[i] = int(2)
        highn = highn + 1
    elif ((psycho_data.N[i]>=46)&(psycho_data.N[i] < 56)):
        data.N[i] = int(1)
        midn = midn + 1
    elif (psycho_data.N[i] < 46):
        data.N[i] = int(0)
        lown = lown + 1


# In[141]:


data.head(42)


# In[142]:


print(higho,highc,highe,higha,highn)


# In[143]:


print(mido,midc,mide,mida,midn)


# In[144]:


print(lowo,lowc,lowe,lowa,lown)

