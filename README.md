# 14D004 Scraping Project

## Project Description

The data and code in this repository allows users to scrape all the available courses on [datacamp.com](https://www.datacamp.com/courses) and scape all job posts on [jobsinbarcelona.es](http://jobsinbarcelona.es/) using [scrapy](https://scrapy.org/) an open source and collaborative framework for extracting the data you need from websites.

- The code was written Python 3.6 and Scrapy 1.5.1

### **[Datacamp](https://www.datacamp.com/courses):** 
On the datacamp course page itself, you can search for courses of interest or browse all the courses by technology. 
<p align="center">
  <img src="./img/datacamp_1.png" alt="browse_by_tech"
       width="480" height="330">
</p>

The `datacamp.py` script extracts all of the course titles within these six technologies, along with their course description, author, authors occupation and URL. 

<p align="center">
  <img src="./img/datacamp_2.png" alt="browse_by_tech"
       width="500" height="280">
</p>

### **[Jobs in barcelona](http://jobsinbarcelona.es/):** 
Jobs in Barcelona is a platform of tech orientated jobs in Barcelona.
<p align="center">
  <img src="./img/jobsinbarca_1.png" alt="browse_by_tech"
       width="500" height="300">
</p>

The `jobsinbarcelona.py` script scrapes all of the job listings along with the company, location, published date, job source and URL.

<p align="center">
  <img src="./img/jobsinbarca_2.png" alt="browse_by_tech"
       width="500" height="330">
</p>

### **[Datacamp Instructors](https://www.datacamp.com/instructors):** 
On the datacamp instructors page, you can find the details of all of the various course instructors. 
<p align="center">
  <img src="./img/data_instruct_1.png" alt="browse_by_tech"
       width="500" height="330">
</p>

The `datacamp_instruct.py` script extracts all of the instructor's titles along with their subscriber count,  occupation and URL. Furthermore, the script extracts their personal descriptions from their "Full Bios" (see example below). 

<p align="center">
  <img src="./img/data_instruct_2.png" alt="browse_by_tech"
       width="550" height="160">
</p>

## Folders 

- **datacamp**: Scrapy datacamp project stored here
- **jobsinbarcelona**: Scrapy jobsinbarcelona project stored here
- **datacamp_instructors**: Scrapy datacamp instructors project stored here

Each of which is a directory with the following contents (datacamp used for example):
```
datacamp/
    scrapy.cfg            # deploy configuration file
    datacamp.csv          # scaped data exported as .csv
    datacamp.json          # scaped data exported as .json

    datacamp/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file (not used)

        middlewares.py    # project middlewares file (not used)

        pipelines.py      # project pipelines file (not used)

        settings.py       # project settings file (not used)

        spiders/          # a directory with the spiders
            __init__.py
            datacamp.py   # This is the code for our datacampe Spider
```

## Prerequisites
### Installing Scrapy

Install the latest version of Scrapy (I recommend using [Anaconda](https://www.anaconda.com/download/))

- Anaconda distribution
```bash
conda install scrapy
```
- PyPI
```bash
pip install scrapy
```

## How to run the Spiders

To put the spiders to work, go to the relevant project’s top-level directory (i.e. datacamp, jobsinbarcelona or datacamp_instructors) and run:
```bash
scrapy crawl datacamp
```
or
```bash
scrapy crawl jobsinbarcelona
```
or
```bash
scrapy crawl datacamp_instructors
```

## Storing the scraped data

The simplest way to store the scraped data is by using Feed exports, with the following command:
```bash
scrapy crawl datacamp -o datacamp.csv
```
or
```bash
scrapy crawl jobsinbarcelona -o jobsinbarcelona.csv
```
or
```bash
scrapy crawl datacamp_instruct -o datacamp_instructors.csv
```

That will generate a datacamp.csv, jobsinbarcelona.csv and datacamp_instructors.csv file containing all the scraped items. 

You can also use other formats, like JSON:
```bash
scrapy crawl datacamp -o datacamp.json
```

Note: for historical reasons, Scrapy appends to a given file instead of overwriting its contents. If you run this command twice without removing the file before the second time, you’ll end up with a broken file. 
