# How to run locally


# Architecture decisions
I made an adjustment of the code structure which is folder "agent", "tools", "schemas" will be inside of the src instead
of root folder.

- Schemas are used to define the data structure of the database.

- tools are used to help with the development process(i.e. service to do the algorithms).

- agent is the main part of the project. such as planners, controllers, etc.

- api is the entry point of the project.

# What would be developed with more time
1. add CI/CD pipeline
2. add logging and tracking system
3. build frontend
4. build database to replace the current in memory database
5. add more functions like get_point_of_interest/ check_visa_requirements/ estimate_budgets