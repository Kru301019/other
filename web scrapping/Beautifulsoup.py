from bs4 import BeautifulSoup

with open('H:\My Drive\Year 2\other\other-1\web scrapping\mypage.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    courseCards = soup.find_all('div', class_='card')
    for courseCard in courseCards:
        courseName = courseCard.h5.text
        coursePrice = courseCard.a.text.split()[-1]
        print(f'{courseName} costs {coursePrice}')
  