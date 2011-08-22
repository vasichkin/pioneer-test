Feature: Check nova returns correct credentials
    Try to create project, user and get credentials. Verify them

    Scenario: Check zipfile
        Create admin user "osthtestuser"
        Create project "osthtestproject" for user "osthtestuser"
        Check novarc function for project "osthtestproject", user "osthtestuser"
        Delete project "osthtestproject" for user "osthtestuser"
        Delete user "osthtestuser"
