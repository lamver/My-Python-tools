import time
from tqdm import tqdm

mylist = [1,2,3,4,5,6,7,8]

c=0
for i in tqdm(mylist):
    c+=1
time.sleep(1)