# -*- coding: utf-8 -*-
import os
import glob
from scrapy import Spider
from scrapy.http import Request


class DatacampSpider(Spider):
    name = 'datacamp'
    allowed_domains = ['datacamp.com']
    start_urls = ['http://datacamp.com/courses/']

    def parse(self, response):
        technologies = response.xpath('//*[@class="col-lg-4 col-sm-6"]/a/@href').extract()
        for tech in technologies:
            absolute_url = response.urljoin(tech)
            yield Request(absolute_url, callback=self.parse_tech)

    def parse_tech(self, response):
        courses = response.xpath('//*[@class="course-block "]')
        for course in courses:
            course_title = course.xpath('.//*[@class="course-block__title"]/text()').extract()
            course_description = course.xpath('normalize-space(.//*[@class="course-block__description"]/text())').extract()
            course_author = course.xpath('normalize-space(.//*[@class="course-block__author-name"]/text())').extract()
            course_author_occupation = course.xpath('normalize-space(.//*[@ class="course-block__author-occupation"]/text())').extract()
            course_url = course.xpath('.//*[@ class="course-block__link ds-snowplow-link-course-block"]/@href').extract_first()
            course_url = course_url.replace('/courses','https://www.datacamp.com/courses')

            yield{'Course Title': course_title,
            'Course Description': course_description,
            'Course Author': course_author,
            'Course Author Occupation': course_author_occupation,
            'Course URL': course_url,
            }
    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file, 'datacamp.csv')

    

