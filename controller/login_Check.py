import os
import sys
import connector

def loginCheck(user_id, password):
	con = connector.connector()
	cursor = con.cursor()
	query = """select user_type from tbl_users where user_id = \'""" + user_id + """\' and user_pass = \'""" + password + """\'"""
	cursor.execute(query)
	chk = False
	for row in cursor:
		chk = True
	err = {}
	if(chk):
		err['er_no'] = row[0]
		err['er_msg'] = 'Login Successful'
	else:
		err['er_no'] = -1;
		err['er_msg'] = 'Login Failed. Due to invalid user_id or password';
	return err
