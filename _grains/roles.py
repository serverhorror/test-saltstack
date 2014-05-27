import random

def is_():
	return random.choice((True, False))

def is_nginx():
	return {u'is_nginx': is_()}
def is_httpd():
	return {u'is_httpd': is_()}
def is_slapd():
	return {u'is_slapd': is_()}
def is_production():
	return {u'is_production': is_()}
def is_qa():
	return {u'is_qa': is_()}
def is_dev():
	return {u'is_dev': is_()}
