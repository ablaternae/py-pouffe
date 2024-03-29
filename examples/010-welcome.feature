
Feature: welcome to the jungle
	As a anonymous client
	Scenario: Первое подключение к серверу
		Given a request url http://127.0.59.84:5984
			#And request header "Accept-Encoding" "gzip, deflate, br"
		When the request sends GET

		Then the response status is OK
			And the response json matches
				"""
				{
					"poufdb": {"type": "string"},
					"id": {"type": ["number", "string"]},
					"uuid": {"type": "uuid"},
					"vendor": {"type": "string"},
					"version": {"type": ["number", "string"]}
				}
				"""
			And the response json at $.poufdb contains "PoufDB"
			And the response json at $.vendor contains "ablaternae"

