# flaskofservice
To start using 'users service'
  Clone this repo and 
  Run 'users.py'

Start Interacting with a service
  
  using POSTMAN view service information;
    run 'GET' http://localhost:5000 
  
  Get users details;
    run 'GET' http://localhost:5000/users
  
  Get Specific user details  
    run 'GET' http://localhost:5000/users/<user_id>
  
  Create a new User
    run 'POST' http://localhost:5000/users and body
                {"name":"<name>","lastName" : "last name"}
    
   Modify User details
    run 'PUT' http://localhost:5000/users/<user_id> and body
                {"name":"<name>","lastName" : "last name"}
                
   Delete Specific user details  
    run 'DELETE' http://localhost:5000/users/<user_id>
