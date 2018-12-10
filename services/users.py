import json
from flask import request, Flask, jsonify
from werkzeug.exceptions import abort

app = Flask( __name__ )
usersFile = '../data/users.json'

with open(usersFile) as json_data:
    users = json.load(json_data )


# Default app endpoint
@app.route( "/" )
def default():
    return "Welcome to demo Users service app"


# add a routing to service
@app.route( "/users", methods=['GET'] )
def get_users():
    return jsonify({'users': users}),200


@app.route( "/users/<int:id>/" )
def get_user(id):
    for user in users:
        if id == user[ 'id' ]:
            print( user )
            return jsonify( {'user': user} ), 200


@app.route( "/users", methods=[ "POST" ] )
def create_user():
    if not request.json or 'name' not in request.json:
        abort( 400 )
    print( request.json )
    user = {
        'id': users[ -1 ][ 'id' ] + 1,
        'name': request.json[ 'name' ],
        'lastName': request.json[ 'lastName' ]
    }
    users.append( user )
    return jsonify( {'user': user} ), 201


@app.route( "/users/<int:id>/", methods=[ "DELETE" ] )
def delete_user(id):
    print("Users" + users)
    for user in users:
        if id == user[ 'id' ]:
            users.remove(user)
            print(users)
            with open( usersFile, 'w' ) as outfile:
                json.dump( users, outfile, sort_keys=True, indent=4)
            return jsonify( {'user': user} ), 200


@app.route( "/users", methods=[ "PUT" ] )
def modify_user():
    if not request.json or 'name' not in request.json:
        abort( 400 )
    print( request.json )
    user = {
        'id': users[ -1 ][ 'id' ] + 1,
        'name': request.json[ 'name' ],
        'lastName': request.json[ 'lastName' ]
    }
    users.append( user )
    with open( usersFile, 'w' ) as outfile:
        json.dump( users, outfile, indent=4)
    return jsonify( {'user': user} ), 201


if __name__ == "__main__":
    app.run()
