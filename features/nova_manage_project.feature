Feature: Create project
    Try to create project via nova-manage

    Scenario: Check creation of project via nova-manage
	Create project "vskproject" for user "vsk"
	Check project "vskproject" exist for user "vsk"
	Delete project "vskproject" for user "vsk"
	Check project "vskproject" does not exist for user "vsk"
