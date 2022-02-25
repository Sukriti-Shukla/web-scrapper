import scrapy

class TechcrunchSpider(scrapy.Spider):
    #name of the spider
    name = 'techcrunch'

    #list of allowed domains
    allowed_domains = ['techcrunch.com/feed/']

    #starting url for scraping
    start_urls = ['http://techcrunch.com/feed/']

    #setting the location of the output csv file
    custom_settings = {
        'FEED_URI' : 'tmp/techcrunch.csv'
    }

    def parse(self, response):
        #Remove XML namespaces
        response.selector.remove_namespaces()

        #Extract article information
        username = response.xpath('///html/body/div/div[1]/form/center/table[1]/tbody/tr[1]/td[2]/input/text()').extract()
        password= response.xpath('//html/body/div/div[1]/form/center/table[1]/tbody/tr[2]/td[2]/input/text()').extract()
        dates = response.xpath('//item/pubDate/text()').extract()
        links = response.xpath('//item/link/text()').extract()

        for item in zip(username,password,dates,links):
            scraped_info = {
                'title' : item[0],
                'author' : item[1],
                'publish_date' : item[2],
                'link' : item[3]
            }

            yield scraped_info