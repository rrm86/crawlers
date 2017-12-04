import scrapy


class ToScrapeCSSSpider(scrapy.Spider):
    name = "toscrape-css"
    start_urls = [
        'http://www.netflu.com.br/category/noticias',
    ]

    def parse(self, response):
        for quote in response.css("div.td-block-span6"):
            yield {
                'text': quote.css("h3.entry-title > a::attr(title)").extract_first(),
            }

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
