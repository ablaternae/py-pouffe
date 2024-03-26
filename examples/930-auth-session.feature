
@skip
Feature: https://github.com/behave-restful/behave-restful/issues/42
	As authorized client
	
	@skip
	Scenario: пропустить
		Given a request url http://127.0.59.84:5984
		When the request sends GET
			And request header "Accept-Encoding" equal "gzip, deflate, br"

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
			And the response json at $.vendor contains "pouffe"

