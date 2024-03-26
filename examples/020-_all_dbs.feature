
Feature: welcome to the jungle
	As a anonimous client
	Scenario: Посмотреть все базы
		Given a request url http://127.0.59.84:5984/_all_dbs
		When the request sends GET
		Then the response status is 501
