Authorization:Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJpYXQiOjE2MzQxNDI3ODQsImV4cCI6MTYzNDc0NzU4NCwiYXVkIjoiaHR0cHM6Ly91YXQucm9ib3RldXIuY28udWsiLCJpc3MiOiJmZWF0aGVycyIsInN1YiI6ImJmYjRhOTM0LTJiOTQtNDYyNC04OTg1LTFjMTliMzJhYTgwMSIsImp0aSI6ImZiOTg5ZTBlLTk2ZWQtNGY2OC05MGIyLTQzZTA5ZmY0MGQ0OCJ9.NWdAQNpiQDicnKgt50VuWnEt7W7ZlkAu9hENRPTTDlw
Content-Type:application/x-www-form-urlencoded

serviceId:5e03cb9e-322d-49c0-bc6a-3668eb21770e
reactor:Create User account API
payload:{"about":"","name":"Barry","lastName":"Buck","dob":"2021-09-30","age":"38","gender":"Male","saCitizen":"Yes","password":"asdfg","email":"barry@saucecode.tech"}

curl "https://uat.roboteur.co.uk/api/reaction" -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6ImFjY2VzcyJ9.eyJpYXQiOjE2MzQxNDI3ODQsImV4cCI6MTYzNDc0NzU4NCwiYXVkIjoiaHR0cHM6Ly91YXQucm9ib3RldXIuY28udWsiLCJpc3MiOiJmZWF0aGVycyIsInN1YiI6ImJmYjRhOTM0LTJiOTQtNDYyNC04OTg1LTFjMTliMzJhYTgwMSIsImp0aSI6ImZiOTg5ZTBlLTk2ZWQtNGY2OC05MGIyLTQzZTA5ZmY0MGQ0OCJ9.NWdAQNpiQDicnKgt50VuWnEt7W7ZlkAu9hENRPTTDlw" -H "Content-Type: application/json" -d "{\"serviceId\":\"5e03cb9e-322d-49c0-bc6a-3668eb21770e\",\"reactor\":\"Create User account API\",\"payload\":{\"about\":\"\",\"name\":\"Barry\",\"lastName\":\"Buck\",\"dob\":\"2021-09-30\",\"age\":\"38\",\"gender\":\"Male\",\"saCitizen\":\"Yes\",\"password\":\"asdfg\",\"email\":\"barry@saucecode.tech\"}}"