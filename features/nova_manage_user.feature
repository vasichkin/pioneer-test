Feature: Create user and admin user
    Try to create user via nova-manage

    Scenario: Check creation of user via nova-manage
	Create admin user "adminosthtestuser"
	Create user "osthtestuser"
	Check user "osthtestuser" exist
	Check user "adminosthtestuser" exist
	Delete user "osthtestuser"
	Delete user "adminosthtestuser"
	Check user "osthtestuser" does not exist
	Check user "adminosthtestuser" does not exist
