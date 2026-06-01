from flask import Flask, make_response, request 
app = Flask(__name__)
@app.route("/")
def index():
    return "Hello, World!"
@app.route("/no-content")
def no_content():
    return {"message": "This is a no content response"}, 204
@app.route("/exp")
def exp():
    resp=make_response({"message": "This is an example response"}, 200)
    resp.status = "200 OK"
    return resp
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]
@app.route("/data")
def get_data():
    try:
        if data and len(data) > 0:
            return {"data": data}, 200
        else:
            return {"message": "No data available"}, 404
    except NameError as e:
        return {"error": str(e)}, 500
@app.route("/name-search")
def name_search():

    name = request.args.get("name")

    if not name:
        return {"error": "Name parameter is required"}, 400

    results = []

    for item in data:
        if (name.lower() in item["first_name"].lower() or
            name.lower() in item["last_name"].lower()):
            results.append(item)

    if results:
        return {"results": results}, 200
    else:
        return {"message": "No matching records found"}, 404
@app.route("/count")
def count():
    try:
        return {"count": len(data)}, 200
    except NameError as e:
        return {"error": str(e)}, 500
@app.route("/person/<uuid:id>")
def get_person(id):
    try:
        for item in data:
            if item["id"] == str(id):
                return {"person": item}, 200
        return {"message": "Person not found"}, 404
    except NameError as e:
        return {"error": str(e)}, 500
@app.route("/person/<uuid:id>", methods=["DELETE"])
def delete_person(id):
    try:
        for person in data:
            if person["id"] == str(id):
                data.remove(person)
                return {"message": "Person deleted successfully"}, 200
        return {"message": "Person not found"}, 404
    except NameError as e:
        return {"error": str(e)}, 500
@app.route("/person", methods=["POST"])
def create_person():
    new_person = request.get_json()
    if not new_person:
        return {"error": "Invalid input"}, 400
    try:
        data.append(new_person)
        return {"message": "Person created successfully", "person": new_person}, 201  
    except NameError as e:
        return {"error": str(e)}, 500
    return {"message": f"{new_person['id']}"}, 200
@app.errorhandler(404)
def not_found(error):
    return {"error": "Resource not found"}, 404
if __name__ == "__main__":
    app.run(debug=True)
