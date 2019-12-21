# importing google_images_download module 
from google_images_download import google_images_download  
  
# creating object 
response = google_images_download.googleimagesdownload()  
    
query = 'sad human faces' 
def downloadimages(query): 
    # keywords is the search query 
    # format is the image file format 
    # limit is the number of images to be downloaded 
    # print urs is to print the image file url 
    # size is the image size which can 
    # be specified manually ("large, medium, icon") 
    # aspect ratio denotes the height width ratio 
    # of images to download. ("tall, square, wide, panoramic") 
    arguments = {"keywords": query, 
                 "limit":200, 
                 "print_urls":True, 
                 "size": "medium"} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query,
                     "limit":200, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
    
downloadimages(query) 
  
#Driver Code 
#for query in search_queries: 
    #downloadimages(query)  
    #print()  

    

'''
from google_images_download import google_images_download

DRIVER_PATH = '/usr/local/bin/chromedriver'
args = {'keywords': 'sad human face',               # the query to search in Google Images
        'output_directory': '/sadnew/images',   # the root directory for the images
        'image_directory': 'sad',                   # the subdirectory (images will be stored in '/data/emotion/images/happy')
        'silent_mode': True,                          # limits the number of lines printed to stdout
        'limit': 1000,                                # limit for the number of images returned
        'chromedriver': DRIVER_PATH}

response = google_images_download.googleimagesdownload()
response.download(args)get

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import os
import http.cookiejar as cookielib
import json

def get_soup(url,header):
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')


query = "sad human face"# you can change the query for the image  here
image_type="ActiOn"
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print(url)
#add the directory for your image here
DIR="sadFaces"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    
    try:
            resp=requests.get(img,stream=True)
            path_to_write=os.path.join(os.getcwd(),FILE_NAME.split("_")[0],url[1].split("/")[-1])
            outfile=open(path_to_write,'wb')
            outfile.write(resp.content)
            outfile.close()
            print("Done downloading {} of {}".format(url[0]+1,len(urls)))
    except:
            print("Failed to download url number {}".format(url[0]))
    
    try:
        req = urllib.request(img, headers={'User-Agent' : header})
        raw_img = urllib.urlopen(req).read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print(cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print("could not load : "+img)
        print(e)
  
'''