# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider
from scrapy.http import Request

class DatacampInstructSpider(scrapy.Spider):
    name = 'datacamp_instruct'
    allowed_domains = ['datacamp.com']
    start_urls = ['https://www.datacamp.com/instructors']


    def parse(self, response):
        instructors = response.xpath('//*[@class="dc-card dc-card--content dc-card--bordered instructor-block"]')
        for instructor in instructors:
            instructor_title = instructor.xpath('normalize-space(.//*[@class="instructor-block__name dc-u-mb-12"]/text())').extract_first()
            instructor_subs = instructor.xpath('normalize-space(.//*[@class="instructor-block__students-subscribed"]/text())').extract_first()
            instructor_occupation = instructor.xpath('normalize-space(.//*[@class="instructor-block__description-text"]/text())').extract_first()
            instructor_link = instructor.xpath('.//*[@class="dc-u-mt-24"]/a/@href').extract_first()
            instructor_link = instructor_link.replace('/instructors','https://www.datacamp.com/instructors')

            yield scrapy.Request(instructor_link,
                                callback = self.parse_instructors,
                                meta={'instructor_title': instructor_title,
                                'instructor_subs': instructor_subs,
                                'instructor_occupation': instructor_occupation,
                                'instructor_link': instructor_link})

        next_page_url = response.xpath('.//*[@class="dc-btn dc-btn--tertiary instructors__button dc-u-mb-48"]/@href').extract_first()
        if next_page_url:
            yield scrapy.Request(response.urljoin(next_page_url), callback=self.parse)

    def parse_instructors(self, response):
        instructor_title = response.meta['instructor_title']
        instructor_subs = response.meta['instructor_subs']
        instructor_occupation = response.meta['instructor_occupation']
        instructor_link = response.meta['instructor_link']

        instructor_description = response.xpath('normalize-space(//*[@class="instructor-header__bio dc-u-color-white"])').extract()

        yield {'Instructor Title': instructor_title,
                'Instructor Subscribers': instructor_subs,
                'Instructor Occupation': instructor_occupation,
                'Instructor Link': instructor_link,
                'Instructor Description': instructor_description}



