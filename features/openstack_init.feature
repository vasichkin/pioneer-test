Feature: Initialize test enviroment to run tests
    Try to admin user, project, network and get credentials


#    Scenario: Create nova enviroment test
#	Do all to set up nova
#	Do all checks to verify nova enviroment
#	Do all to clean nova

    Scenario: Create nova enviroment
	Create admin user "osth-user-admin"
	Create project "osth-project" for user "osth-user-admin"
	Create network "10.222.0.0/24" with "1" nets, "256" ips per network

    Scenario: Check nova enviroment
	Check user "osth-user-admin" exist
	Check project "osth-project" exist for user "osth-user-admin"
	Check network "10.222.0.0/24" exist
	Check novarc function for project "osth-project", user "osth-user-admin"

    Scenario: Clean nova enviroment
	Delete network "10.222.0.0/24"
	Delete project "osth-project" for user "osth-user-admin"
	Delete user "osth-user-admin"

    Scenario: Check nova enviroment cleared
	Check user "osth-user-admin" does not exist
	Check project "osth-project" does not exist for user "osth-user-admin"
	Check network "10.222.0.0/24" does not exist

