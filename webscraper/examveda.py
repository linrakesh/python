import requests
from bs4 import BeautifulSoup

source = requests.get("https://www.examveda.com/commerce/practice-mcq-question-on-accounting/?page=2",'lxml').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

for article in soup.find_all('article',class_='question single-question question-type-normal'):
    try:
        question_no = article.find('div', class_="question-number")
        question = article.find('div', class_="question-main").text
        parts = article.find('div', class_="question-options")
        answer = article.find('span', class_="color").text
        answer_content = article.find('div', class_="page-content")
        answer_key = answer_content.find('strong').text
        #print(answer_content.prettify())
        solution = article.find('span').text

        print(question_no.text, question)
        parts = article.find('div', class_="question-options")
        i = 1
        for option in parts.find_all('label'):
            if(i % 2 == 0):
                print(option.text)
            i = i+1
        print(answer, answer_key)
        
    except:
        pass

