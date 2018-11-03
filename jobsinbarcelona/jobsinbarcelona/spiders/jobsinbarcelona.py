# -*- coding: utf-8 -*-
import os
import glob
import scrapy

class JobsinbarcelonaSpider(scrapy.Spider):
    name = 'jobsinbarcelona'
    allowed_domains = ['jobsinbarcelona.es']
    start_urls = ['http://jobsinbarcelona.es/']

    def parse(self, response):

        new_jobs = response.xpath('//*[@class="job job-ad new standard"]') + response.xpath('//*[@class="job job-ad standard"]')
        for new_job in new_jobs:
            job_title = new_job.xpath('.//*[@class="job-title"]/a/text()').extract()
            job_company = new_job.xpath('.//*[@class="job-details-company"]/text()').extract()
            job_location = new_job.xpath('.//*[@class="job-details-location"]/text()').extract()
            job_date = new_job.xpath('.//*[@class="job-publication-date"]/text()').extract()
            job_source = new_job.xpath('.//*[@class="job-source"]/text()').extract() 
            job_link = new_job.xpath('.//*[@class="job-link"]/@href').extract_first()

            yield{'Job Title': job_title,
            'Job Company': job_company,
            'Job Location': job_location,
            'Job Date': job_date,
            'Job Source': job_source,
            'Job Link': job_link
            }

        next_page_url = response.xpath('//*[@class="pagination"]/li[7]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file, 'jobsinbarcelona.csv')
            

      






