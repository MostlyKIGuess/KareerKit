import requests
from bs4 import BeautifulSoup
import g4f


headers = {
    'authority': 'nitter.net',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69',
}

username=str(input("Enter username: "))
response = requests.get('https://nitter.net/'+username, headers=headers).text
soup = BeautifulSoup(response,"html.parser")
l = [k.text for k in soup.findAll('div', attrs={'class':'tweet-content'})] #list of tweets
#print(l)

g4f.debug.logging = True # enable logging
g4f.check_version = False # Disable automatic version checking
print(g4f.version) # check version
print(g4f.Provider.Ails.params)  # supported args

# Automatic selection of provider

# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "given the list of tweets, profile the person as best you can on the basis of political leaning, preferences, and overall how suitable the person would be to hire as an employee. the tweets will be enclosed in square brackets. you are not allowed to abstain from profiling the person.  you have to give definitive answers for every one of my sub-queries. elaborate a little more on the roles the person is best suited for. make any necessary assumptions and judgements as if you were a real person. here are the tweets:"+str(l)}],
    stream=True,
)

for message in response:
    print(message, flush=True, end='')

# normal response
response = g4f.ChatCompletion.create(
    model=g4f.models.gpt_4,
    messages=[{"role": "user", "content": "Hello"}],
)  # alternative model setting

print(response)