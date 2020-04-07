import pandas as pd 
import numpy as np
import getopt, sys 
import matplotlib.pyplot as plt

argumentList = sys.argv[1:] 
options = "f:"
long_options = ["file"] 
try: 
    arguments, values = getopt.getopt(argumentList, options, long_options) 
    for currentArgument, currentValue in arguments: 
  
        if currentArgument in ("-f", "--file"): 
            features_file=currentValue
            print(features_file)
except getopt.error as err: 
    print (str(err)) 

print(features_file)
# AUextracted= pd.read_csv('./OpenFace_2.2.0_win_x64/OpenFace_2.2.0_win_x64/processed/P6.csv')
AUextracted= pd.read_csv(features_file)
AUextracted_Selected = AUextracted[[' confidence',' success',' AU01_r',' AU02_r',' AU04_r',' AU05_r',' AU06_r',' AU07_r',' AU09_r',' AU10_r',' AU12_r',' AU14_r',' AU15_r',' AU17_r',' AU20_r',' AU23_r',' AU25_r',' AU26_r',' AU45_r']]
new_AUextracted_Selected = AUextracted_Selected[AUextracted_Selected[' confidence'] >= 0.80]
new_AUextracted_Selected = new_AUextracted_Selected[new_AUextracted_Selected[' success'] == 1]
new_AUextracted_Selected = new_AUextracted_Selected.reset_index(drop=True)
# print("new_AUextracted_Selected",new_AUextracted_Selected)
##############__Model___#######################
# O = AU - 1,2,5,25,26
# C = AU - 1,4,6,9,11  /instead of 11 took 10
# E = AU - 6,12,25,26
# A = AU - 6,12,15,25
# N = AU - 1,2,4,11,20  /instead of 11 took 9


Ocount=0
Ccount=0
Ecount=0
Acount=0
Ncount=0

Osum=[]
Csum=[]
Esum=[]
Asum=[]
Nsum=[]

for i in new_AUextracted_Selected.index:
  if new_AUextracted_Selected[' AU01_r'][i]>0 and new_AUextracted_Selected[' AU02_r'][i]>0 and new_AUextracted_Selected[' AU05_r'][i]>0 and new_AUextracted_Selected[' AU25_r'][i]>0 and new_AUextracted_Selected[' AU26_r'][i]>0 :
  	Ocount=Ocount+1
  	Osum.append(np.mean([new_AUextracted_Selected[' AU01_r'][i],new_AUextracted_Selected[' AU02_r'][i],new_AUextracted_Selected[' AU05_r'][i],new_AUextracted_Selected[' AU25_r'][i],new_AUextracted_Selected[' AU26_r'][i]]))

  if new_AUextracted_Selected[' AU01_r'][i]>0 and new_AUextracted_Selected[' AU04_r'][i]>0 and new_AUextracted_Selected[' AU06_r'][i]>0 and new_AUextracted_Selected[' AU09_r'][i]>0 and new_AUextracted_Selected[' AU10_r'][i]>0 :
  	Ccount=Ccount+1
  	Csum.append(np.mean([new_AUextracted_Selected[' AU01_r'][i],new_AUextracted_Selected[' AU04_r'][i],new_AUextracted_Selected[' AU06_r'][i],new_AUextracted_Selected[' AU09_r'][i],new_AUextracted_Selected[' AU10_r'][i]]))

  if new_AUextracted_Selected[' AU06_r'][i]>0 and new_AUextracted_Selected[' AU12_r'][i]>0 and new_AUextracted_Selected[' AU25_r'][i]>0 and new_AUextracted_Selected[' AU26_r'][i]>0 :
  	Ecount=Ecount+1
  	Esum.append(np.mean([new_AUextracted_Selected[' AU06_r'][i],new_AUextracted_Selected[' AU12_r'][i],new_AUextracted_Selected[' AU25_r'][i],new_AUextracted_Selected[' AU26_r'][i]]))

  if new_AUextracted_Selected[' AU06_r'][i]>0 and new_AUextracted_Selected[' AU12_r'][i]>0 and new_AUextracted_Selected[' AU15_r'][i]>0 and new_AUextracted_Selected[' AU25_r'][i]>0 :
  	Acount=Acount+1
  	Asum.append(np.mean([new_AUextracted_Selected[' AU06_r'][i],new_AUextracted_Selected[' AU12_r'][i],new_AUextracted_Selected[' AU15_r'][i],new_AUextracted_Selected[' AU25_r'][i]]))

  if new_AUextracted_Selected[' AU01_r'][i]>0 and new_AUextracted_Selected[' AU02_r'][i]>0 and new_AUextracted_Selected[' AU04_r'][i]>0 and new_AUextracted_Selected[' AU09_r'][i]>0 and new_AUextracted_Selected[' AU20_r'][i]>0 :
  	Ncount=Ncount+1
  	Nsum.append(np.mean([new_AUextracted_Selected[' AU01_r'][i],new_AUextracted_Selected[' AU02_r'][i],new_AUextracted_Selected[' AU04_r'][i],new_AUextracted_Selected[' AU09_r'][i],new_AUextracted_Selected[' AU20_r'][i]]))

print("Counts :: Ocount: ",Ocount,"Ccount: ",Ccount,"Ecount: ",Ecount,"Acount: ",Acount,"Ncount: ",Ncount)
# print("Sums :: Osum: ",Osum,"Csum: ",Csum,"Esum: ",Esum,"Asum: ",Asum,"Nsum: ",Nsum)
if Osum == [] :
	Osum=[0]
if Csum == [] :
	Csum=[0]
if Esum == [] :
	Esum=[0]
if Asum == [] :
	Asum=[0]
if Nsum == [] :
	Nsum=[0]

print("Means :: Osum: ",np.mean(Osum),"Csum: ",np.mean(Csum),"Esum: ",np.mean(Esum),"Asum: ",np.mean(Asum),"Nsum: ",np.mean(Nsum))
total_percent = Ocount+Ccount+Ecount+Acount+Ncount
Osum_percent=(Ocount/total_percent)*100
Csum_percent=(Ccount/total_percent)*100
Esum_percent=(Ecount/total_percent)*100
Asum_percent=(Acount/total_percent)*100
Nsum_percent=(Ncount/total_percent)*100

print("Percentages :: Osum_percent: ",Osum_percent,"Csum_percent: ",Csum_percent,"Esum_percent: ",Esum_percent,"Asum_percent: ",Asum_percent,"Nsum_percent: ",Nsum_percent)

O_normalize=Osum_percent*np.mean(Osum)
C_normalize=Csum_percent*np.mean(Csum)
E_normalize=Esum_percent*np.mean(Esum)
A_normalize=Asum_percent*np.mean(Asum)
N_normalize=Nsum_percent*np.mean(Nsum)

print("Normalizes :: O_normalize: ",O_normalize,"C_normalize: ",C_normalize,"E_normalize: ",E_normalize,"A_normalize: ",A_normalize,"N_normalize: ",N_normalize)

final_score_total=O_normalize+C_normalize+E_normalize+A_normalize+N_normalize
O_score=(O_normalize/final_score_total)*10
C_score=(C_normalize/final_score_total)*10
E_score=(E_normalize/final_score_total)*10
A_score=(A_normalize/final_score_total)*10
N_score=(N_normalize/final_score_total)*10

print("Final Scores :: O_score: ",O_score,"C_score: ",C_score,"E_score: ",E_score,"A_score: ",A_score,"N_score: ",N_score)

slices_percentages = [O_score,C_score,E_score,A_score,N_score]
BigFive = ['Openness','Conscientiousness','Extraversion','Agreeableness','Neuroticism']
colors = ['green','orange','darkviolet','yellow','red']
exploding=[0.1,0.1,0.1,0.1,0.1]

plt.pie(slices_percentages,explode=exploding, labels=BigFive, colors=colors, startangle=90, autopct='%.1f%%')
plt.title('Big Five Personality based on Facial Features(Pie Chart)')
plt.legend(BigFive,loc="best")
plt.savefig('./static/pie_plot.png')
plt.close()
plt.clf()
# plt.show()

index = np.arange(len(BigFive))
plt.bar(index, slices_percentages)
plt.xlabel('Big Five', fontsize=10)
plt.ylabel('Scores', fontsize=10)
plt.xticks(index, BigFive, fontsize=10,rotation=20)
plt.title('Big Five Personality based on Facial Features(Bar Graph)')
plt.savefig('./static/bar_plot.png')
plt.clf()
plt.close()
# plt.show()