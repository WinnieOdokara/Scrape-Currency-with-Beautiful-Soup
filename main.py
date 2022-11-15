# Beautiful Soup is a Python library for pulling data out of HTML and XML files

from bs4 import BeautifulSoup
import requests

# bs4: beautifulsoup4
# To install 'bs4': 
  # Go to terminal: pip install beautifulsoup4
    # import BeautifulSoup

# Requests: the requests module allows you to send HTTP requests using Python. The HTTP request returns a Response Object with all the response data (content, encoding, status, etc). 
# requests to acces the source code
  # On terminal: pip install requests

def get_currency(in_currency, out_currency):

# in_currency: input   out_currency: output
  # currency code, ex.: USD => BRL

  url = (f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1')
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  # Find span on x-rates source code
    # Go to the website => select the rate => inspect => copy the class
    # get_text() method returns the text inside the Beautiful Soup or Tag('span' in this case) object as a single Unicode string
  
  rate = float(rate[:-4])
# -4 to not output the ISO Code, ex.: USD, BRL

  return rate

current_rate = get_currency('EUR', 'BRL')
print(current_rate)