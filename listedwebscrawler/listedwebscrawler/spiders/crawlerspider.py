import scrapy

count=0

class crawlerspider(scrapy.Spider):
    name = "crawler"

    def start_requests(self):
        yield scrapy.Request(
            'https://www.google.com/search?q=site:youtube.com+openinapp.co',
            callback=self.parse,
            meta={
                'handle_httpstatus_list': [302],
            },
        )

    def parse(self, response):
        for links in response.css('.egMi0.kCrYT a'):
            yield {
                'link':links.attrib['href']
            }
            global count
            count+=1
            if(count==10000):
                return
            
        next_page = response.css('a.nBDE1b.G5eFlf').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

