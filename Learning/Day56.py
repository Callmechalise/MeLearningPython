import multiprocessing
import requests
def downloadfile(url,name):
    response=requests.get(url)
    open(f"file/filre{name}.jpeg","wb").write(response.content);
url="https://images.pexels.com/photos/1213447/pexels-photo-1213447.jpeg"
pros=[]
for i in range(10):
    #downloadfile(url,i) normal call
    #how dads do:
    p = multiprocessing.Process(target=downloadfile, args=(url, i))
    p.start()
    pros.append(p)
for p in pros:
    p.join()