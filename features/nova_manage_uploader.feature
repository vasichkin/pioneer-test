Feature: TODO Image manipuation using nova-manage
    Upload and delete images

    Scenario: Upload image
#	Do all to set up nova
	Register image "images/RS_ubu-SSH-key.tar.gz" using project "osth-project", user "osth-user-admin"
	Deregister image "ere"