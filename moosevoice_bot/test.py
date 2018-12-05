from bs4 import BeautifulSoup


st = "weqrwerqwr<br/>ewr<b>vbev</b>we<br/>sdwvsdvsb<br/>"

soup = BeautifulSoup(st, features="html.parser")

s = BeautifulSoup(st.replace("<br/>", "\n"), features="html.parser")

print(s)