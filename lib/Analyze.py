#!/usr/bin/python
# -*- coding: utf-8 -*-
from textblob import TextBlob
from bs4 import BeautifulSoup
import requests


class Analyze_factory:

    def __init__(self, term):
        self.term = term
        self.sentiment = 0
        self.subjectivity = 0
        self.urls = []
        self.baseurl = \
            'https://www.google.com/search?q={0}&source=lnms&tbm=nws'.format(self.term)
        for numb in range(0, 60, 10):
            self.urls.append(self.baseurl + '&start={}'.format(numb))

    def run(self):
        textToMine = ''
        for url in self.urls:
            response = requests.get(url)
            textToMine += response.text
        soup = BeautifulSoup(textToMine, 'html.parser')
        headline_results = soup.find_all('div', class_='st')
        for text in headline_results:
            blob = TextBlob(text.get_text())
            self.sentiment += blob.sentiment.polarity \
                / len(headline_results)
            self.subjectivity += blob.sentiment.subjectivity \
                / len(headline_results)

        return {
            'term': self.term,
            'sentiment': self.sentiment,
            'subjectivity': self.subjectivity,
            'headline_results': len(headline_results),
            }
