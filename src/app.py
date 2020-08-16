import requests
from bs4 import BeautifulSoup

# request = requests.get("https://www.google.com")
# toget google.com's html sourcecode
# print (request.content)


# https://www.johnlewis.com/herman-miller-aeron-office-chair-graphite/p3177252
# <p class="price price--large"> $1,099.00 </p>

request = requests.get("https://www.johnlewis.com/herman-miller-aeron-office-chair-graphite/p3177252")
content = request.content
print ("Target acquired!")
soup = BeautifulSoup(content, "html.parser")
print ("Soup made!")
element = soup.find("p", {"class": "price price--large"})
print ("Element found")
str_price = element.text.strip()
print (str_price)
amount = int(''.join(d for d in str_price if d.isdigit()))/100
print (amount)
if amount <= 800:
    print ('Buy the chair ASAP!')
    print (u"The current price of the chair is \u00A3{}.".format(amount))
#u print the string in unicode where \u00A3 is the unicode for '£'
elif amount <=1000:
    print ("Buy the chair if you really want it!")
    print ("The current price of the chair is {}.".format(amount))
else:
    print ("Don't buy the chair!")
    print (u"The current price of the chair is \u00A3{}.".format(amount))