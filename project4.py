#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import pandas to create dataframes
import pandas as pd


# In[2]:


# read text file
#df = pd.read_csv('humanGeno.txt', sep='\t')
df = pd.read_csv('/work2/07475/vagheesh/stampede2/forOthers/forBIO321G/humanGeno.txt', sep='\t')


# In[3]:


# Preview dataframe (will not work as a .py file)
df


# In[4]:


# Create set class that retains order, adding new vals only works properly for lists of length <= 2
class setList:
    def __init__(self):
        self.items = []
    
    def add_val(self, val):
        if(type(val) == list):
            rev = val.copy()
            rev.reverse()
            if(val not in self.items and rev not in self.items):
                self.items.append(val)
        elif(val not in self.items):
            self.items.append(val)


# In[5]:


# Create all possible unique pairs of the species, not including Chimp, Neanderthal, and Denisovan
species = ['Dai', 'British', 'Yoruba', 'Mbuti', 'Papuan']
combinations = setList()

for i in species:
    for q in species:
        temp = setList()
        temp.add_val(i)
        temp.add_val(q)
        if(len(temp.items) == 1): 
            continue
        combinations.add_val(temp.items)

# Print pairs
for x, y in combinations.items:
    print(x, y)      


# In[6]:


# Create list to store species types and abba baba values
abba_baba = []
choice = ['Neanderthal', 'Denisovan']

# loop through full dataframe and count up how often abba and baba patterns are present for each species combination
for nean_denis in choice:
    for x, y in combinations.items:
        ABBA = 0
        BABA = 0

        # abba case 1
        temp = df[df['Chimp'] == 0]
        temp = temp[temp[nean_denis] == 2]
        temp = temp[temp[x] == 2]
        temp = temp[temp[y] == 0]
        ABBA += len(temp)
        
        # abba case 2
        temp = df[df['Chimp'] == 2]
        temp = temp[temp[nean_denis] == 0]
        temp = temp[temp[x] == 0]
        temp = temp[temp[y] == 2]
        ABBA += len(temp)
        
        # baba case 1
        temp = df[df['Chimp'] == 2]
        temp = temp[temp[nean_denis] == 0]
        temp = temp[temp[x] == 2]
        temp = temp[temp[y] == 0]
        BABA += len(temp)
        
        # baba case 2
        temp = df[df['Chimp'] == 0]
        temp = temp[temp[nean_denis] == 2]
        temp = temp[temp[x] == 0]
        temp = temp[temp[y] == 2]
        BABA += len(temp)

        # print the species combination and abba baba values
        print('Chimp', nean_denis, x, y)
        print('ABBA value:', ABBA)
        print('BABA value:', BABA)
        print()

        # add species and abba baba values to abba_baba list
        abba_baba.append(['Chimp', nean_denis, x, y, ABBA, BABA])


# In[7]:


# Compute a D-stat for each species combination and print out values in a readable way
for i in abba_baba:
    abba = i[4]
    baba = i[5]
    print(f'{i[0]:<7}{i[1]:<13}{i[2]:<8}{i[3]}')
    print('ABBA value:', abba)
    print('BABA value:', baba)
    print('D-statistic:', (baba - abba)/(baba + abba))
    print()


# In[8]:


# Create five new dataframes, each missing 20,000 rows
df_missing_chunk_1 = df.drop(df.index[0:19999])
df_missing_chunk_2 = df.drop(df.index[20000:39999])
df_missing_chunk_3 = df.drop(df.index[40000:59999])
df_missing_chunk_4 = df.drop(df.index[60000:79999])
df_missing_chunk_5 = df.drop(df.index[80000:])

# Add each dataframe to the list dfs_chunked
dfs_chunked = [df_missing_chunk_1, df_missing_chunk_2, df_missing_chunk_3, df_missing_chunk_4, df_missing_chunk_5]
dfs_chunked


# In[9]:


# Create new list abba_baba_chunked to store the df used, the species combination, and the abba baba values
abba_baba_chunked = []
choice = ['Neanderthal', 'Denisovan']

# num represents the df used
num = 1

# loop through chunked dataframes and count up how often abba and baba patterns are present for each species combination
for df in dfs_chunked:
    for nean_denis in choice:
        for x, y in combinations.items:
            ABBA = 0
            BABA = 0

            # abba case 1
            temp = df[df['Chimp'] == 0]
            temp = temp[temp[nean_denis] == 2]
            temp = temp[temp[x] == 2]
            temp = temp[temp[y] == 0]
            ABBA += len(temp)
            
            # abba case 2
            temp = df[df['Chimp'] == 2]
            temp = temp[temp[nean_denis] == 0]
            temp = temp[temp[x] == 0]
            temp = temp[temp[y] == 2]
            ABBA += len(temp)
            
            # baba case 1
            temp = df[df['Chimp'] == 2]
            temp = temp[temp[nean_denis] == 0]
            temp = temp[temp[x] == 2]
            temp = temp[temp[y] == 0]
            BABA += len(temp)
            
            # baba case 2
            temp = df[df['Chimp'] == 0]
            temp = temp[temp[nean_denis] == 2]
            temp = temp[temp[x] == 0]
            temp = temp[temp[y] == 2]
            BABA += len(temp)

            # print the dataset number, species combination, and abba baba values
            print('Dataset', num)
            print('Chimp', nean_denis, x, y)
            print('ABBA value:', ABBA)
            print('BABA value:', BABA)
            print()

            # add the dataset number, species combination, and abba baba values to abba_baba list
            abba_baba_chunked.append([num, 'Chimp', nean_denis, x, y, ABBA, BABA])
    num += 1


# In[10]:


# group the items in abba_baba_chunked by species combination
grouped = []
for i in range(20):
    temp = [abba_baba_chunked[i], abba_baba_chunked[i + 20], abba_baba_chunked[i + 40], abba_baba_chunked[i + 60], abba_baba_chunked[i + 80], [abba_baba[i][4],abba_baba[i][5]]]
    grouped.append(temp)
grouped


# In[11]:


# create function that returns mean of a list of values
def mean(nums):
    return sum(nums) / len(nums)


# In[12]:


tab = '\t'

# Create empty humanSeqD.txt file and write header labels
with open("humanSeqD.txt", "w") as output:
    output.write(f'Pop1{tab}Pop2{tab}Pop3{tab}Pop4{tab}ABBA{tab}BABA{tab}JackMean{tab}JackError{tab}Z\n')


# In[13]:


bold = '\033[1m'
end_bold = '\033[0m'
tab = '\t'

# loop through the grouped list, open the humanSeqD.txt in preparation to append
output = open('humanSeqD.txt', 'a')
for group in grouped:
    # print the species combination for this group and the Dstats label
    print(f'{bold}{group[0][1]:<7}{group[0][2]:<13}{group[0][3]:<8}{group[0][4]}{end_bold}')
    print('D-statistics: ')

    # loop through each chunked version of this group and compute Dstat
    stats = []
    for uniq in group:
        if(len(uniq) == 2): continue
        abba = uniq[5]
        baba = uniq[6]
        Dstat = (baba - abba)/(baba + abba)
        stats.append(Dstat)
        print(f'{Dstat:<12}', end = '\t')

    # loop through the amount of Dstats previously obtained and compute the jackknife mean
    means = []
    for i in range(len(stats)):
        temp = stats.copy()
        temp.remove(stats[i])
        means.append(mean(temp))
    jackknife = mean(means)

    # loop through the means previously obtained and compute the jackknife standard error
    jkse_calc = []
    for i in means:
        jkse_calc.append((i - jackknife) ** 2)
    jackknife_se = (sum(jkse_calc) / 4) ** (1/2)

    # compute the z-score
    z = jackknife / jackknife_se

    # print out values in a readable way
    print()
    print('Jackknife Mean:', jackknife)
    print('Jackknife Standard Error:', jackknife_se)
    print('Z-score:', z)
    print('\n')
    
    # Add values to the output file, end with a newLine
    output.write(f'{group[0][1]}{tab}{group[0][2]}{tab}{group[0][3]}{tab}{group[0][4]}{tab}')
    output.write(f'{group[5][0]}{tab}{group[5][1]}{tab}{jackknife}{tab}{jackknife_se}{tab}{z}\n')
output.close()

# set permissions to output file?
#import os
#os.chmod('humanSeqD.txt', 750)

# In[14]:


# create new df from the previously written file
df = pd.read_csv('humanSeqD.txt', sep='\t')


# In[15]:


# preview it to check for errors (will not work as a .py file)
df

