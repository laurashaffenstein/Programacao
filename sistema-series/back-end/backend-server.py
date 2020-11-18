from config import *
from models import Serie


@app.route('/get-series', methods=['get'])
def get_series():
    db_series = db.session.query(Serie).all()
    json_series = [ serie.json() for serie in db_series ]
    response = jsonify(json_series)
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route('/create-series', methods=['post'])
def create_series():
    response = jsonify({"status": "201", "result": "ok", "details": "Serie created"})
    data = request.get_json()
    try:
        new_serie = Serie(**data)
        db.session.add(new_serie)
        db.session.commit()
    except Exception as e:
        response = jsonify({"status": "400", "result": "error", "details ": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response 

@app.route('/delete-series/<int:id>', methods=['DELETE'] )
def delete_series(id):
    response = jsonify({"status": "200", "result": "ok", "details": "Serie deleted"})
    try:
        Serie.query.filter(Serie.id == id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"status": "400" , "result": "error", "details": str(e)})
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(debug=True)