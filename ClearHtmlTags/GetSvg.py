from bs4 import BeautifulSoup as bSoup

def GetClearedHtml(html_text):
    soup=bSoup(html_text,"html5lib")
    cleaned_text=soup.get_text(separator="\n",strip=True)
    return cleaned_text;

html_path= input("Please enter html path:")
with open(html_path,'r') as f:
    read_file=f.readlines()
soup=bSoup(str(read_file),"html.parser")
svgText=soup.find_all("svg")
clearedHtmlText=GetClearedHtml(str(read_file))
print(svgText)
print("Fully:\n"+clearedHtmlText)

