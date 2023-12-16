#!/usr/bin/env python
# coding: utf-8

# # Using biopython to explore the olfactory response of the cabbage aphids to different volatile cues 

# In this experiment, different volatile cues were collected from cabbage plant which serves as a sustaible host plant for the cabbage aphids. These volatile cues ranged from plants without any infestation (HC = healthy cabbage), aphids infested cabbage plants (AC) as conspecific cues, diamondback moth larvae infested cabbage (DC) as heterospecific cues and a solvent control (CN). Aphids were exposed to the various odour cues in a four-choice laboratory olfactometer bioassay, and the time spent in each of the arms of the olfactomer was recorded (time spent = min). Using python, I demonstrate how the collected data could be explored, visualized, manipulated and also analyzed. 

# # Importing and loading the data set

# In[2]:


#First we import pandas as pd 

import pandas as pd


# In[3]:


#Next we load in our data using the below function

df = pd.read_csv('Multiple_choice_olfactory_test.csv')


# In[4]:


#To check and see if the data have been successfully loaded, we type in df which here represents the data set
df


# # Visualising the data and test for normality  

# It is best to always visualize our data, and to check if the asumption of normality has been met before proceeding to choosing the right statistical analysis. First, I will be creating a bar chart to have a visual description of the data and then performing tests of normality. There are several libraries in python that could be called for this, hence I will be calling them all in this part. The other libraries have useful functions too which would come handy as we progress further.

# In[6]:


import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from numpy.random import seed
from numpy.random import randn
import numpy as np
import statsmodels.api as sm
from scipy.stats import shapiro


# To create a bar chat, we allocate the different groups into categories while specifying their values. Essentially, we want the means to be capture on the bar chart hence we use the mean function. Then next, ploting the figure, in this demonstration, I allocated different colours to the different groups and also added labels on the y and x axis and a title above for easy understanding

# In[8]:


categories = ['HC', 'AC', 'DC', 'CN']
values = [df['HC'].mean(), df['AC'].mean(), df['DC'].mean(), df['CN'].mean()]


# In[10]:


plt.figure(figsize=(8, 6))
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold']
plt.bar(categories, values, color=colors)
plt.xlabel('Treatments')
plt.ylabel('Time spent in olfactometer in Min')
plt.title('Aphids response to different odour cues')


# Visually inspecting the data set, we could see that there are differences but we cannot conclusively say if this is true statistically, hence there is need to run a statistical analysis, but to do this, we need to first check for the assumptions of normal distribution before deciding on which stat tool to use. There are several ways of checking for normal distrubution, but in this demonstration, I will be employing the Q-Q plot, Shapiro and a histogram of normal distribution to check the assumption.  First, I exlored the Q-Q plot data visualization of normal distrubution to see if my data were normally distributed using the import statsmodel.api as sm library earlier imported above.

# Using the following code it should plot a Q-Q plot of normal distrubution. 
# Studying the look of the plot, we could infer on the Q-Q plot that the data utilized were not normally distributed because they did not assume a straight line.

# In[15]:


sm.qqplot(df, line='s')
plt.title('Q-Q Plot')
plt.show()


# Next the Shapiro-Wilk's Test for normal distribution was performed. Remember we already imported the library:from scipy.stats import shapiro previously for this test. Here, I also used the else if function to tell us in plain English if the data were normally distrubuted as shown:

# In[12]:


statistic, p_value = shapiro(df)
print(f"Shapiro-Wilk Test:\nStatistic: {statistic}, P-value: {p_value}")

if p_value > 0.05:
    print("The data appears to be normally distributed.")
else:
    print("The data does not appear to be normally distributed.")


# Finally, I visually inspected my data using the histogram to see if it assumes a bell curve shape of normal distribution.
# 

# In[16]:


sns.histplot(df, kde=True, stat='density', color='blue', bins=30)
plt.title('Histogram of Data')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()


# # Analysing data using appropriate statistical test

# The three test of normality confirms that the data aren't normally distributed hence a parametric one-way statistical test would not be appropriate to use. An alternative to this is the Kruskal Wallis one way test which is a non-parametric statistical test and most suitable for the data set. Before using Kruskal-Wallis statistic, it was first imported from the library scipy and also executed using the codes shown below. I also used the else if function to communicate with me in plain English if I should reject the null hypothesis or not. 

# In[17]:


from scipy.stats import kruskal


# In[18]:


statistic, p_value = kruskal(df['HC'].to_list(),
               df['AC'].to_list(),
                df['DC'].to_list(),
                df['CN'].to_list()
               )
print("Kruskal-Wallis Statistic:", statistic)
print("P-value:", p_value)
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis. There are significant differences between groups.")
else:
    print("Fail to reject the null hypothesis. There is no significant difference between groups.")


# We could potentially use another method which is shorter than the one above instead of using .to_list() function:

# In[22]:


h_statistic, p_value = stats.kruskal(df['HC'], df['AC'], df['DC'], df['CN'])


# In[21]:


print(f"H Statistic: {h_statistic}")
print(f"P-Value: {p_value}")


# From the result shown here, Kruskal-Wallis test statistics and also the P-value indicates that statistically, there lies significant differences in the response of the insect to the various volatile cue it was exposed to, but it did not show us where exactly. Hence, there is need to run a post-hoc test to point out where the difference is. 

# #I used a Dunn's post-hoc test by importing it from the scikit_posthocs library as shown below: 

# In[29]:


from scikit_posthocs import posthoc_dunn


# In[30]:


posthoc_results = posthoc_dunn([df['HC'], df['AC'], df['DC'], df['CN']], p_adjust='holm')


# After running the post-hoc test and printing the result, it represented the different treatments using numbers i.e., 1 = HC, 2 = AC, 3 = DC and 4 = CN with the associated P-Value to show where significant differences lies. Although, the result could be interpreted that the odours from aphids infested cabbage were monstly attracted to the aphids in the olfactory bioassay because it shows a p-value of 0.016 which is less than 0.05 as against the solvent control, showing us exactly where there is a significant difference. But for a much more easier interpretation, I will be running the post-hoc again using the melt function to include the variable names rather than using numbers to represent them.

# In[31]:


print("\nDunn's post hoc test results:")
print(posthoc_results)


# In[27]:


data_melted = pd.melt(df.reset_index(), id_vars=['index'], value_vars=['HC', 'AC', 'DC', 'CN'])
result_dunn = posthoc_dunn(data_melted, val_col='value', group_col='variable', p_adjust='holm')


# #Now we can see the variable names printed on to the post-hoc for easy understanding and interpretation of the results 

# In[28]:


print("\nDunn's test results:")
print(result_dunn)


# # Creating a final figure for report and or manuscript writing 

# Finally, having ran the analysis and understood the data, there is need to create an appealing figure for the final report. Here, I created a box plot to visually represent my data showing the mean, standard error and error bars for my report using the below codes:

# In[34]:


data = [df['HC'], df['AC'], df['DC'], df['CN']]


# In[35]:


means = [np.mean(d) for d in data]
std_errors = [np.std(d) / np.sqrt(len(d)) for d in data]


# In[36]:


plt.boxplot(data, showmeans=True)
plt.errorbar(range(1, len(data) + 1), means, yerr=std_errors, fmt='ro', markersize=8, label='Mean ± SE')
plt.title('Box Plot showing the treatments and mean time spent in the olfactometer')
plt.xlabel('Treatments')
plt.ylabel('Total time spent (min)')
plt.xticks(range(1, len(data) + 1), ['HC', 'AC', 'DC', 'CN'])
plt.legend()
plt.show()


# The end
