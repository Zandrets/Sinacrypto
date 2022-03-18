from random import random
from tokenize import PseudoExtras
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
#BASH CODE echo "$(cat italia |while read -r line;do printf "%s" "$(echo $line |awk '{print $5}'), $(echo $line |awk '{print $11}'), , ,";done)"

montenegro=[1.97, 99, 28, 1, 1.94, 92, 19, 3, 2.02, 109, 18, 1, 1.89, 85, 27, 1, 2.00, 102, 25, 2, 1.87, 89, 23, 1, 1.87, 85, 26, 1, 1.96, 100, 15, 1, 1.97, 108, 18, 3, 1.89, 103, 22, 2, 1.90, 80, 20, 1, 1.89, 95, 20, 1, 1.95, 91, 20, 1]
hungria=[1.98, 96, 20, 3, 2.03, 108, 27, 2, 1.91, 91, 18, 3, 1.92, 91, 19, 3, 2.02, 105, 20, 3, 1.96, 101, 21, 3, 1.95, 97, 32, 2, 1.95, 96, 24, 2, 1.96, 94, 22, 3, 1.93, 96, 19, 3, 1.97, 108, 28, 2, 2.02, 110, 24, 3, 1.98, 85, 22, 2]
italia=[1.90, 97, 23, 3,1.90, 88, 17, 3,1.84, 84, 19, 3,1.91, 98, 22, 3,1.89, 90, 21, 2,1.86, 85, 20, 2,1.91, 80, 23, 3,1.95, 96, 25, 1,1.98, 91, 20, 3,1.92, 102, 28, 2,1.92, 102, 24, 3,1.95, 92, 23, 3,1.96, 93, 19, 3]
serbia=[1.94, 92, 21, 3,2.02, 105, 17, 3,1.89, 92, 26, 3,1.93, 98, 20, 3,1.94, 95, 22, 3,1.97, 97, 20, 3,1.88, 85, 26, 3,1.93, 96, 18, 3,1.97, 91, 18, 3,1.96, 101, 18, 3,1.87, 93, 17, 3,1.95, 91, 20, 3,2.01, 100, 23, 3]
australia=[1.94, 93, 20, 1,1.93, 99, 16, 2,1.92, 95, 21, 1,1.95, 98, 29, 1,2.00, 104, 19, 1,1.96, 97, 21, 1,1.87, 88, 19, 1,1.93, 100, 19, 1,1.89, 84,  21, 1,1.92, 91, 17, 1,1.89, 84, 20, 1,1.88, 93, 26, 1,1.95, 91, 24, 1]
kasahistan=[1.83, 82, 26, 1,1.86, 90, 28, 1,1.83, 83, 22, 1,1.92, 103, 29, 1,1.83, 83, 21, 1,1.93, 95, 16, 1,1.83, 80, 20, 1,2.02, 85, 27, 1,1.92, 103, 25, 1,1.92, 110, 23, 1,1.94, 100, 24, 1,1.83, 83, 21, 1,1.97, 77, 20, 1]
united_states=[2.01, 103, 21, 3,1.88, 88, 19, 3,1.98, 103, 19, 3,1.96, 105, 20, 3,1.98, 106, 19, 3,1.91, 97, 18, 3,1.98, 115, 18, 3,2.01, 100, 19, 1,1.96, 106, 22, 1,1.93, 87, 22, 1,1.93, 112, 23, 3,1.85, 81, 21, 3,1.96, 83, 21, 1]


stat=[]
pes=[]
mon_age=[]
mon_prior=[]
for fill in range(0, len(montenegro), 4):
    stat.append(montenegro[fill])
    pes.append(montenegro[fill+1])
    mon_age.append(montenegro[fill+2])
    mon_prior.append(montenegro[fill+3])

mon_stat = np.array(stat)
mon_pes = np.array(pes)
mon_IMC = mon_pes / mon_stat ** 2

stat=[]
pes=[]
hun_age=[]
hun_prior=[]
for fill in range(0, len(hungria), 4):
    stat.append(hungria[fill])
    pes.append(hungria[fill+1])
    hun_age.append(hungria[fill+2])
    hun_prior.append(hungria[fill+3])

hun_stat = np.array(stat)
hun_pes = np.array(pes)
hun_IMC = hun_pes / hun_stat ** 2 

stat=[]
pes=[]
ita_age=[]
ita_prior=[]
for fill in range(0, len(italia), 4):
    stat.append(italia[fill])
    pes.append(italia[fill+1])
    ita_age.append(italia[fill+2])
    ita_prior.append(italia[fill+3])

ita_stat = np.array(stat)
ita_pes = np.array(pes)
ita_IMC = ita_pes / ita_stat ** 2

stat=[]
pes=[]
ser_age=[]
ser_prior=[]
for fill in range(0, len(serbia), 4):
    stat.append(serbia[fill])
    pes.append(serbia[fill+1])
    ser_age.append(serbia[fill+2])
    ser_prior.append(serbia[fill+3])

ser_stat = np.array(stat)
ser_pes = np.array(pes)
ser_IMC = ita_pes / ita_stat ** 2

stat=[]
pes=[]
aus_age=[]
aus_prior=[]
for fill in range(0, len(australia), 4):
    stat.append(australia[fill])
    pes.append(australia[fill+1])
    aus_age.append(australia[fill+2])
    aus_prior.append(australia[fill+3])

aus_stat = np.array(stat)
aus_pes = np.array(pes)
aus_IMC = aus_pes / mon_stat ** 2

stat=[]
pes=[]
kas_age=[]
kas_prior=[]
for fill in range(0, len(kasahistan), 4):
    stat.append(kasahistan[fill])
    pes.append(kasahistan[fill+1])
    kas_age.append(kasahistan[fill+2])
    kas_prior.append(kasahistan[fill+3])

kas_stat = np.array(stat)
kas_pes = np.array(pes)
kas_IMC = kas_pes / mon_stat ** 2

stat=[]
pes=[]
usa_age=[]
usa_prior=[]
for fill in range(0, len(united_states), 4):
    stat.append(united_states[fill])
    pes.append(united_states[fill+1])
    usa_age.append(united_states[fill+2])
    usa_prior.append(united_states[fill+3])

usa_stat = np.array(stat)
usa_pes = np.array(pes)
usa_IMC = usa_pes / mon_stat ** 2

count=0
mon_count=0
ser_count=0
hun_count=0
ita_count=0
aus_count=0
usa_count=0
kas_count=0

IMC=0
age=0
peso=0
altura=0

for persona in range(0, 13):
    if mon_prior[persona] == 3:
        IMC=IMC+mon_IMC[persona]
        age=age+mon_age[persona]
        peso=peso+mon_pes[persona]
        altura=altura+mon_stat[persona]
        count=count+1
        mon_count=mon_count+1
    if hun_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+hun_pes[persona]
        altura=altura+hun_stat[persona]
        count=count+1
        hun_count=hun_count+1
    if ita_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ita_pes[persona]
        altura=altura+ita_stat[persona]
        count=count+1
        ita_count=ita_count+1
    if ser_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ser_pes[persona]
        altura=altura+ser_stat[persona]
        count=count+1
        ser_count=ser_count+1
    if aus_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+aus_pes[persona]
        altura=altura+aus_stat[persona]
        count=count+1
        aus_count=aus_count+1
    if kas_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+kas_pes[persona]
        altura=altura+kas_stat[persona]
        count=count+1
        kas_count=kas_count+1
    if usa_prior[persona] == 3:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+usa_pes[persona]
        altura=altura+usa_stat[persona]
        count=count+1
        usa_count=usa_count+1

print("Para ser medallista de oro: ")
print("IMC ideal: ", IMC/count," edad ideal: ", age/count, " altura ideal: ", altura/count, " peso ideal: ", peso/count)

count=0
mon_count=0
ser_count=0
hun_count=0
ita_count=0
aus_count=0
usa_count=0
kas_count=0
IMC=0
age=0
peso=0
altura=0

for persona in range(0, 13):
    if mon_prior[persona] >= 2:
        IMC=IMC+mon_IMC[persona]
        age=age+mon_age[persona]
        peso=peso+mon_pes[persona]
        altura=altura+mon_stat[persona]
        count=count+1
        mon_count=mon_count+1
    if hun_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+hun_pes[persona]
        altura=altura+hun_stat[persona]
        count=count+1
        hun_count=hun_count+1
    if ita_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ita_pes[persona]
        altura=altura+ita_stat[persona]
        count=count+1
        ita_count=ita_count+1
    if ser_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ser_pes[persona]
        altura=altura+ser_stat[persona]
        count=count+1
        ser_count=ser_count+1
    if aus_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+aus_pes[persona]
        altura=altura+aus_stat[persona]
        count=count+1
        aus_count=aus_count+1
    if kas_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+kas_pes[persona]
        altura=altura+kas_stat[persona]
        count=count+1
        kas_count=kas_count+1
    if usa_prior[persona] >= 2:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+usa_pes[persona]
        altura=altura+usa_stat[persona]
        count=count+1
        usa_count=usa_count+1

print("Para ser medallista: ")
print("IMC ideal: ", IMC/count," edad ideal: ", age/count, " altura ideal: ", altura/count, " peso ideal: ", peso/count)

count=0
mon_count=0
ser_count=0
hun_count=0
ita_count=0
aus_count=0
usa_count=0
kas_count=0
IMC=0
age=0
peso=0
altura=0

for persona in range(0, 13):
    if mon_prior[persona] >= 1:
        IMC=IMC+mon_IMC[persona]
        age=age+mon_age[persona]
        peso=peso+mon_pes[persona]
        altura=altura+mon_stat[persona]
        count=count+1
        mon_count=mon_count+1
    if hun_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+hun_pes[persona]
        altura=altura+hun_stat[persona]
        count=count+1
        hun_count=hun_count+1
    if ita_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ita_pes[persona]
        altura=altura+ita_stat[persona]
        count=count+1
        ita_count=ita_count+1
    if ser_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+ser_pes[persona]
        altura=altura+ser_stat[persona]
        count=count+1
        ser_count=ser_count+1
    if aus_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+aus_pes[persona]
        altura=altura+aus_stat[persona]
        count=count+1
        aus_count=aus_count+1
    if kas_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+kas_pes[persona]
        altura=altura+kas_stat[persona]
        count=count+1
        kas_count=kas_count+1
    if usa_prior[persona] >= 1:
        IMC=IMC+hun_IMC[persona]
        age=age+hun_age[persona]
        peso=peso+usa_pes[persona]
        altura=altura+usa_stat[persona]
        count=count+1
        usa_count=usa_count+1

print("Para representar a un pais: ")
print("IMC ideal: ", IMC/count," edad ideal: ", age/count, " altura ideal: ", altura/count, " peso ideal: ", peso/count)

IMC=np.array(list(zip(aus_IMC,hun_IMC,ita_IMC,kas_IMC,mon_IMC,ser_IMC,usa_IMC)))
ages=np.array(list(zip(aus_age, hun_age, ita_age, kas_age,mon_age,ser_age,usa_age)))
perfect=IMC/ages
kmeans=KMeans(n_clusters=3)
ideal_imc=kmeans.fit(IMC)

#ideal_age=kmeans.fit(ages)
#centroid=kmeans.cluster_centers_
#print("Ideal para Australia(imc/edad): ",centroid[0])
#print("Ideal para Hungria(imc/edad): ",centroid[1])
#print("Ideal para Italia(imc/edad): ",centroid[2])
#print("Ideal para Kasahistan(imc/edad): ",centroid[3])
#print("Ideal para Montenegro(imc/edad): ",centroid[4])
#print("Ideal para Serbia(imc/edad): ",centroid[5])
#print("Ideal para USA(imc/edad): ",centroid[6])

mon= plt.scatter(mon_IMC, mon_age, c="#ff0000")
hun= plt.scatter(hun_IMC, hun_age, c="#00ff00")
ita= plt.scatter(ita_IMC, ita_age, c="#0000ff")
ser= plt.scatter(ser_IMC, ser_age, c="#000000")
aus= plt.scatter(aus_IMC, aus_age, c="#ffff00")
kas= plt.scatter(aus_IMC, aus_age, c="#ff00ff")
usa= plt.scatter(aus_IMC, aus_age, c="#00ffff")
zero=plt.scatter(0,0)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')
#plt.scatter(kmens.cluster_centers_[:, 0], kmens.cluster_centers_[:, 1], s=300, c='yellow', label = 'Centroids')

plt.xlabel('IMC')
plt.ylabel('tiempo')
plt.show()