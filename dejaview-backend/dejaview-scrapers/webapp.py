from bottle import route, run, template
import scrape


@route('/scrape/<address>/<geoloc>')
def handler(address, geoloc):
    links = scrape.scrapetheworld(address)
    return template('<b>Scraping address {{address}} {{geoloc}} {{links}}</b>', address=address, geoloc=geoloc, links=links)


run(host='localhost', port=8080)

#http://localhost:8080/test/test