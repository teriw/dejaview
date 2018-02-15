from bottle import route, run, template
import scrape


#@route('/scrape/<address>/<addressId>')
@route('/scrape/<address>')
def handler(address):
    data = scrape.scrapetheworld(address)
    return template('<b>Scraping address : <br> {{address}} <br> {{data}}</b>', address=address, data=data)


run(host='localhost', port=8080)

#http://localhost:8080/test/test