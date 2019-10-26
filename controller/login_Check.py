import os

def loginCheck(user_id, password):
	if(user_id == 'Shashankh' and password == '41c41a5db0fd0e9bbcdd3ae4b30d23bddcbc4d42f4bbd89d6e8a2c9a6c2bc986'):
		e_code = 0
		e_msg = "Login Successful"
	else:
		e_code = 1
		e_msg = "User ID and Password pair are incorrect"
	return e_code,e_msg

