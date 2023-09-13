# Note: Changes for pull request

from bs4 import BeautifulSoup
import requests

url = "https://medium.com/towards-data-science/a-practical-guide-to-linear-regression-3b1cb9e501a6"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
paragraph = doc.find("p", id="f23b")
outText = paragraph.text

print(outText)

# Saving Extracted Content to Text File
out = "out.txt"
with open(out, "w") as file:
    file.write(str(outText))
    file.close()


# Local File
# with open('index.html', 'r') as f:
#     doc = BeautifulSoup(f, "html.parser")

# print(doc.prettify())
