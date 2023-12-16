# Data_science_assessment-
Data science and machine learning assessment submission 
# Using biopython to explore the olfactory response of the cabbage aphids to different volatile cues 

In this experiment, different volatile cues were collected from cabbage plant which serves as a sustaible host plant for the cabbage aphids. These volatile cues ranged from plants without any infestation (HC = healthy cabbage), aphids infested cabbage plants (AC) as conspecific cues, diamondback moth larvae infested cabbage (DC) as heterospecific cues and a solvent control (CN). Aphids were exposed to the various odour cues in a four-choice laboratory olfactometer bioassay, and the time spent in each of the arms of the olfactomer was recorded (time spent = min). Using python, I demonstrate how the collected data could be explored, visualized, manipulated and also analyzed. This work is currently still in progress so data should be treated with caution. 
# # Visualising the data and test for normality  
It is best to always visualize our data, and to check if the asumption of normality has been met before proceeding to choosing the right statistical analysis. First, I will be creating a bar chart to have a visual description of the data and then performing tests of normality. There are several libraries in python that could be called for this, hence I will be calling them all in this part. The other libraries have useful functions too which would come handy as we progress further.

To create a bar chat, we allocate the different groups into categories while specifying their values. Essentially, we want the means to be capture on the bar chart hence we use the mean function. Then next, ploting the figure, in this demonstration, I allocated different colours to the different groups and also added labels on the y and x axis and a title above for easy understanding

Visually inspecting the data set, we could see that there are differences but we cannot conclusively say if this is true statistically, hence there is need to run a statistical analysis, but to do this, we need to first check for the assumptions of normal distribution before deciding on which stat tool to use. There are several ways of checking for normal distrubution, but in this demonstration, I will be employing the Q-Q plot, Shapiro and a histogram of normal distribution to check the assumption. First, I exlored the Q-Q plot data visualization of normal distrubution to see if my data were normally distributed using the import statsmodel.api as sm library earlier imported. 

Next the Shapiro-Wilk's Test for normal distribution was performed. Remember we already imported the library:from scipy.stats import shapiro previously for this test. Here, I also used the else if function to tell us in plain English if the data were normally distrubuted as shown:
Finally, I visually inspected my data using the histogram to see if it assumes a bell curve shape of normal distribution.


# Analysing data using appropriate statistical test
The three test of normality confirms that the data aren't normally distributed hence a parametric one-way statistical test would not be appropriate to use. An alternative to this is the Kruskal Wallis one way test which is a non-parametric statistical test and most suitable for the data set. Before using Kruskal-Wallis statistic, it was first imported from the library scipy and also executed using the codes shown below. I also used the else if function to communicate with me in plain English if I should reject the null hypothesis or not.

From the result shown here, Kruskal-Wallis test statistics and also the P-value indicates that statistically, there lies significant differences in the response of the insect to the various volatile cue it was exposed to, but it did not show us where exactly. Hence, there is need to run a post-hoc test to point out where the difference is.

I used a Dunn's post-hoc test by importing it from the scikit_posthocs library as shown. 

After running the post-hoc test and printing the result, it represented the different treatments using numbers i.e., 1 = HC, 2 = AC, 3 = DC and 4 = CN with the associated P-Value to show where significant differences lies. Although, the result could be interpreted that the odours from aphids infested cabbage were monstly attracted to the aphids in the olfactory bioassay because it shows a p-value of 0.016 which is less than 0.05 as against the solvent control, showing us exactly where there is a significant difference. But for a much more easier interpretation, I will be running the post-hoc again using the melt function to include the variable names rather than using numbers to represent them.

# Creating a final figure for report and or manuscript writing
Finally, having ran the analysis and understood the data, there is need to create an appealing figure for the final report. Here, I created a box plot to visually represent my data showing the mean, standard error and error bars for my report using the reported codes.
