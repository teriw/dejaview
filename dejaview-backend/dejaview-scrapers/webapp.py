from bottle import route, run, template
import scrape


@route('/scrape/<address>/<addressId>')
def handler(address, addressId):
    data = scrape.scrapetheworld(address)
    return template('<b>Scraping address : <br> {{address}} <br>{{addressId}} <br> {{data}}</b>', address=address, addressId=addressId, data=data)


run(host='localhost', port=8080)

#http://localhost:8080/test/test