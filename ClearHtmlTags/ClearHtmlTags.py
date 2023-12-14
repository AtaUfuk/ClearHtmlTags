# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os

def clearHtml(html_text):
    # soup = BeautifulSoup(html_text, 'html.parser')
    # def filteredText(tag):
    #     if tag.name in ['svg','div','p','text','ul','li','strong','em','pre','span','b']:
    #         return True
    #     return False
    # cleanText =  [tag.get_text(separator='\n', strip=True) for tag in soup.find_all(filteredText)]
    # cleanedText = ' '.join(cleanText)
    soup=BeautifulSoup(html_text,"html5lib")
    cleanedText=soup.get_text(separator=" ",strip=True)
    return cleanedText.replace("[\'","").replace("\']","")

print("This program written for read html file and remove html tags(write a new file optional)")
inputText = "Please insert html file path:"
htmlPath = input(inputText.encode('utf-8').decode('utf-8'))
writeInputText="If you want to write a new file please insert new file path"
writePath=input(writeInputText.encode('utf-8').decode('utf-8'))
with open(htmlPath,'r') as f:
    lines=f.readlines()

clearedText = clearHtml(str(lines))
if not writePath:
    print(clearedText)
else:
    with open (writePath,'w') as newFile:
        newFile.writelines(clearedText)
        if os.path.exists(writePath):
            print("Your file added")