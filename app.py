from flask import Flask, jsonify, request, Response, session
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
import json
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017')
db = client['UnipiLibrary']  # Use the correct database name here
users = db['users']
books = db['books']
reservations = db['reservations']

app.config['MONGO_URI'] = "mongodb://localhost:27017/UnipiLibrary"
mongo = PyMongo(app)




def is_admin(user_email):
    
    admin_emails = ['tzigkounakismanolis@gmail.com']
    return user_email in admin_emails

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.json
    _username = _json['username']
    _surname = _json['surname']
    _email = _json['email']
    _password = _json['password']
    _date_of_birth = _json['date_of_birth']

    if _username and _surname and _email and _password and _date_of_birth and request.method == 'POST':
        users = mongo.db.users

        # Check if the user with the given email already exists
        existing_user = users.find_one({'email': _email})
        if existing_user:
            resp = jsonify("User with the provided email already exists")
            resp.status_code = 409  # Conflict status code
            return resp

        user_data = {
            'username': _username,
            'surname': _surname,
            'email': _email,
            'password': _password,
            'date_of_birth': _date_of_birth
        }
        users.insert_one(user_data)
        resp = jsonify("User added successfully")
        resp.status_code = 200
        return resp
    else:
        return not_found()

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not found' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp



@app.route('/login', methods=['POST'])
def login():
    data = None
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content", status=500, mimetype='application/json')
    if data is None:
        return Response("bad request", status=500, mimetype='application/json')
    if "email" not in data or "password" not in data:
        return Response("Information incomplete", status=500, mimetype="application/json")

    # Query the database to find a user with the given username
    user = mongo.db.users.find_one({"email": data["email"]})
    if user is None:
        return Response("User not found", status=404, mimetype="application/json")

    # Check if the provided password matches the stored password
    if user["password"] == data["password"]:
        # Generate a session token or user ID for authentication (you can implement this part)

        # For now, let's just return a success message with the user's ID
        return Response(f"Logged in. Your UserID is: {str(user['_id'])}", status=200, mimetype='application/json')
    else:
        return Response("Wrong username or password.", status=400, mimetype='application/json')


@app.route('/delete/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    _json = request.json
    _email = _json['email']  # Assuming you send the admin's email in the request body

    # Check if the user making the request is an admin
    if is_admin(_email):
        # Proceed with user deletion
        user_id_obj = ObjectId(user_id)
        result = users.delete_one({'_id': user_id_obj})
        if result.deleted_count > 0:
            resp = jsonify("User deleted successfully")
            resp.status_code = 200
            return resp
        else:
            resp = jsonify("User not found")
            resp.status_code = 404
            return resp
    else:
        resp = jsonify("Only admins are allowed to delete users")
        resp.status_code = 403  # Forbidden status code
        return resp
    

@app.route('/add_book', methods=['POST'])
def add_book():
    _json = request.json
    _email = _json['email']  # Assuming you send the admin's email in the request body

    # Check if the user making the request is an admin
    if is_admin(_email):
        # Check if a book with the same title already exists
        existing_book = books.find_one({'title': _json['title']})
        if existing_book:
            resp = jsonify("A book with the same title already exists")
            resp.status_code = 409  # Conflict status code
            return resp

        # Proceed with adding the book
        book_data = {
            'title': _json['title'],
            'author': _json['author'],
            'published': _json['published'],
            'available': _json['available'],  # Set this field to True or False based on availability
            'days_reservation': _json['days_reservation'],
            'pages': _json['pages'],
            'summary': _json['summary']
        }
        books.insert_one(book_data)
        resp = jsonify("Book added successfully")
        resp.status_code = 200
        return resp
    else:
        resp = jsonify("Only admins are allowed to add books")
        resp.status_code = 403  # Forbidden status code
        return resp
@app.route('/delete_book/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    _json = request.json
    _email = _json['email']  # Assuming you send the admin's email in the request body

    # Check if the user making the request is an admin
    if is_admin(_email):
        # Proceed with book deletion
        book_id_obj = ObjectId(book_id)
        result = books.delete_one({'_id': book_id_obj})
        if result.deleted_count > 0:
            resp = jsonify("Book deleted successfully")
            resp.status_code = 200
            return resp
        else:
            resp = jsonify("Book not found")
            resp.status_code = 404
            return resp
    else:
        resp = jsonify("Only admins are allowed to delete books")
        resp.status_code = 403  # Forbidden status code
        return resp



@app.route('/search_books', methods=['POST'])
def search_books():
    _json = request.json
    _email = _json['email']# Assuming you send the admin's email in the request body
    user = mongo.db.users.find_one({"email": _email})
    if user is None:
        return Response("User not found", status=404, mimetype="application/json")
    _title = _json.get('title', None)
    _author = _json.get('author', None)
    _available = _json.get('available', None)
    _published = _json.get('published', None)
    # Check if the user making the request is an admin
        # Build the search query based on the provided criteria
    search_query = {}
    if _title:
        search_query['title'] = _title
    if _author:
        search_query['author'] = _author
    if _available is not None:
        search_query['available'] = _available
    if not is_admin(_email):
        if _published:
            search_query['published'] = _published

    # Perform the search operation in the database using 'books'

        
    result_books = list(books.find(search_query, {'_id': 1, 'published': 1, 'title': 1, 'author': 1, 'available': 1}))
    

    # Check if books were found
    if result_books:
        # Convert ObjectId to string for each book's _id field
        for book in result_books:
            book['_id'] = str(book['_id'])

        return jsonify(result_books)
    else:
        resp = jsonify("No books found based on the search criteria")
        resp.status_code = 404
        return resp
    
        


@app.route('/reserve_book', methods=['POST'])
def reserve_book():
    _json = request.json
    _title = _json['title']
    _author = _json['author']
    _email = _json['email']
    _phone = _json['phone']

    # Check if the book exists in the collection
    book = books.find_one({'title': _title, 'author': _author})
    if not book:
        resp = jsonify("Book not found")
        resp.status_code = 404
        return resp
    

    # Check if the book is already reserved
    if not book['available']:
        resp = jsonify("Book is not available for reservation")
        resp.status_code = 409  # Conflict status code
        return resp


    # Calculate the reservation end date based on the book's 'days_reservation' field
    days_reservation = book.get('days_reservation', 7)  # Default to 7 days if not provided
    reservation_data = {
        'book_id': str(book['_id']),
        'title': _title,
        'author': _author,
        'email': _email,
        'phone': _phone,
        'reservation_end_date': days_reservation  # You can calculate the end date based on the current date
    }
    # Update the book's 'available' field to False (not available for reservation)
    books.update_one({'_id': ObjectId(book['_id'])}, {'$set': {'available': False}})


    # Insert the reservation data into the 'reservations' collection
    reservation_id = reservations.insert_one(reservation_data).inserted_id

    # Return the reservation ID as part of the response
    response_data = {
        'reservation_id': str(reservation_id),
        'message': 'Book reserved successfully'
    }
    return jsonify(response_data), 200

@app.route('/user_reservations', methods=['GET'])
def user_reservations():
    _email = request.args.get('email')  # Retrieve the email from the URL query parameter

    # Find all reservations made by the user with the given email
    user_reservations = list(reservations.find({'email': _email}, {'_id': 0}))

    if user_reservations:
        return jsonify(user_reservations)
    else:
        resp = jsonify("No reservations found for the user")
        resp.status_code = 404
        return resp

@app.route('/reservation_details/<reservation_id>', methods=['GET'])
def reservation_details(reservation_id):
    # Find the reservation with the given reservation_id
    reservation = reservations.find_one({'_id': ObjectId(reservation_id)})

    if reservation:
        # Convert the ObjectId to a string for JSON serialization
        reservation['_id'] = str(reservation['_id'])
        return jsonify(reservation)
    else:
        resp = jsonify("Reservation not found")
        resp.status_code = 404
        return resp

@app.route('/return_book/<reservation_id>', methods=['PUT'])
def return_book(reservation_id):
    # Find the reservation with the given reservation_id
    reservation = reservations.find_one({'_id': ObjectId(reservation_id)})

    if reservation:
        # Get the book_id from the reservation
        book_id = reservation['book_id']

        # Update the book's 'available' field to make it available for reservation
        book = books.find_one({'_id': ObjectId(book_id)})
        if book:
            books.update_one({'_id': ObjectId(book_id)}, {'$set': {'available': True}})

            # Delete the reservation from the reservations collection
            reservations.delete_one({'_id': ObjectId(reservation_id)})

            return jsonify("Book returned successfully and available for reservation"), 200
        else:
            resp = jsonify("Book not found")
            resp.status_code = 404
            return resp
    else:
        resp = jsonify("Reservation not found")
        resp.status_code = 404
        return resp



if __name__ == "__main__":
    app.run(debug=True)

