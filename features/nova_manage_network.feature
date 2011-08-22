Feature: Create network
    Try to create network via nova-manage

    Scenario: Check creation of network via nova-manage
        Create network "10.123.0.0/24" with "1" nets, "256" ips per network
        Check network "10.123.0.0/24" exist
        Delete network "10.123.0.0/24"
        Check network "10.123.0.0/24" does not exist

        Create network "10.123.0.0/24" with "2" nets, "128" ips per network
        Check network "10.123.0.0/25" exist
        Check network "10.123.0.128/25" exist
        Delete network "10.123.0.0/25"
        Delete network "10.123.0.128/25"
        Check network "10.123.0.0/25" does not exist
        Check network "10.123.0.128/25" does not exist


        Create network "10.123.0.0/24" with "4" nets, "4" ips per network
        Check network "10.123.0.0/30" exist
        Check network "10.123.0.4/30" exist
        Check network "10.123.0.8/30" exist
        Check network "10.123.0.12/30" exist
        Delete network "10.123.0.0/30"
        Delete network "10.123.0.4/30"
        Delete network "10.123.0.8/30"
        Delete network "10.123.0.12/30"
        Check network "10.123.0.0/30" does not exist
        Check network "10.123.0.4/30" does not exist
        Check network "10.123.0.8/30" does not exist
        Check network "10.123.0.12/30" does not exist
