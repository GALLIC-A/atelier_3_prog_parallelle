import requests
import time
start=time.time()
data1=list(range(1,5001))
data2=list(range(5001,10001))

resp1=requests.post('http://localhost:5001/compute',json={"numbers":data1})
resp2=requests.post('http://localhost:5002/compute',json={"numbers":data2})

total=resp1.json()['result']+resp2.json()['result']
print("Somme des carrés (calcul distribué) : ",total)
print(" temps de calcul distribué : ",time.time()-start)