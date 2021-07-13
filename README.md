# expo

## About the app

    - This application will utilize websockets to handle the fast communication between stations.
    - An order will be entered in, the corresponding menu items will be sent to their respective stations
        - times attributed to menu items will be updated based on current business levels to effectively handle
          the common situation of multiple dishes on the same station
    - A user can create a kitchen profile
        - within this profile a service type can be created to adjust speed time to change fire times
        - stations can be created
        - menu items can be created and associated with a specific station to know where to send the item to
            - there will also be a fire time added to count adjust the times for all items on the same order
            - within a given fire time when other items will be ready, an item will be marked as fired
            - there will be alerts for time
        - menu items can be sold from the station to clear when it is ready
        - orders can be cleared when all dishes are ready and sent out
