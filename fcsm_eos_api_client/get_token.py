# coding: utf-8

"""
    Combined FCSM EOS API

    See test_auth.py - sso login to create cookies.json file
"""

from __future__ import absolute_import
import os.path
import json
import time
from urllib.parse import urlsplit


JWT_TOKENS = {}


def set_api_token(api):
	host = api.api_client.configuration.host
	token = load_token_from_cookies(host)
	#api.api_client.default_headers["Authorization"] = "Bearer %s" % token
	# From AnalyticsApi.md:
	#configuration = fcsm_eos_api_client.Configuration()
	# Configure Bearer authorization (JWT): bearerAuth
	#configuration.access_token = 'YOUR_BEARER_TOKEN'
	# Defining host is optional and default to https://emeia-eos.fcsm.io
	#configuration.host = "https://emeia-eos.fcsm.io"
	# Create an instance of the API class
	#api_instance = fcsm_eos_api_client.AnalyticsApi(fcsm_eos_api_client.ApiClient(configuration))
	api.api_client.configuration.access_token = token


def load_token_from_cookies(host):
	u = urlsplit(host)
	domain = u.netloc
	print(domain)
	if domain in JWT_TOKENS:
		return JWT_TOKENS[domain]
	path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'cookies.json')
	print(path)
	assert os.path.isfile(path)
	#if not os.path.isfile(path):
	#	return
	with open(path, 'r') as fp:
		cookies = json.load(fp)
	jwt_token = None
	for info in cookies:
		if info['domain'] != domain:
			continue
		if info['name'] == 'jwt_token':
			print('Found jwt_token', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(info['expires'])))
			assert info['expires'] > time.time()
			#if info['expires'] <= time.time():
			#	print('jwt_token expired', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(info['expires'])))
			#	break
			jwt_token = info['value']
			#print('Found jwt_token', time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(info['expires'])))
			break
	JWT_TOKENS[domain] = jwt_token
	return jwt_token


if __name__ == '__main__':
	host = 'https://emeia-eos.fcsm.io'
	print(load_token_from_cookies(host))
