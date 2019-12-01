import cx_Oracle

def connector():
	ip = '192.168.1.42'
	port = 1521
	SID = 'system'
	dsn_tns_con = cx_Oracle.makedsn(ip, port, SID)
	user_name = 'system'
	password = 'system'
	con = cx_Oracle.connect(user_name, password, dsn_tns_con)
	return con
