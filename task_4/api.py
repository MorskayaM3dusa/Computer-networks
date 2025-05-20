from parser import prelaunch, parser_func, init_driver

from flask import Flask, jsonify, request

from base import read_data, write_data


app = Flask(__name__)

@app.route('/parser', methods=['GET'])
def parser():
    url = request.args.get('url')
    driver = init_driver()
    driver.get(url)
    prelaunch(driver)
    data = parser_func(driver)
    driver.quit()
    write_data(data)
    watches_data = read_data()
    return jsonify(watches_data)

if __name__ == '__main__':
    app.run(debug=True)