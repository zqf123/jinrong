# -*- coding: utf-8 -*-
from scrapy import Request, Spider
from spidertest2.items import ProductItem

class SpiderSpider(Spider):
    name = 'jinrong'
    allowed_domains = ['http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;sjzrq;pn50;ddesc;qsd20190413;qed20200113;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb']
    start_urls = ['http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;sjzrq;pn50;ddesc;qsd20190413;qed20200113;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb']
    url = 'http://fund.eastmoney.com/data/fundranking.html#tall;c0;r;sjzrq;pn50;ddesc;qsd20190413;qed20200113;qdii;zq;gg;gzbd;gzfs;bbzt;sfbb'
    def start_requests(self):
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            yield Request(url=self.url, callback=self.parse, meta={'page': page}, dont_filter=True)

    def parse(self, response):
        products = response.xpath('//*[@id="dbtable"]/tbody//tr')
        for product in products:
            item = ProductItem()
            item['序号'] = ''.join(product.xpath('./td[2]//text()').extract()).strip()
            item['基金代码'] = ''.join(product.xpath('.//td[3]//text()').extract()).strip()
            item['基金简称'] = ''.join(product.xpath('.//td[4]//a//text()').extract()).strip()
            item['日期'] = ''.join(product.xpath('./td[5]//text()').extract()).strip()
            item['单位净值'] = ''.join(product.xpath('./td[6]//text()').extract()).strip()
            item['累计净值'] = ''.join(product.xpath('./td[7]//text()').extract()).strip()
            item['日增长率'] = ''.join(product.xpath('./td[8]//text()').extract()).strip().replace('%','')
            item['近1周'] = ''.join(product.xpath('./td[9]//text()').extract()).strip().replace('%','')
            item['近1月'] = ''.join(product.xpath('./td[10]//text()').extract()).strip().replace('%','')
            item['近3月'] = ''.join(product.xpath('./td[11]//text()').extract()).strip().replace('%','')
            item['近6月'] = ''.join(product.xpath('./td[12]//text()').extract()).strip().replace('%','')

            item['近1年'] = ''.join(product.xpath('./td[13]//text()').extract()).strip().replace('%','')
            item['近2年'] = ''.join(product.xpath('./td[14]//text()').extract()).strip().replace('%','')
            item['近3年'] = ''.join(product.xpath('./td[15]//text()').extract()).strip().replace('%','')
            item['今年来'] = ''.join(product.xpath('./td[16]//text()').extract()).strip().replace('%','')
            item['成立来'] = ''.join(product.xpath('./td[17]//text()').extract()).strip().replace('%','')
            # print(item)

            yield item