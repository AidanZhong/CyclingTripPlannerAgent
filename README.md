# How to run locally
Step 1: cd into the project folder

Step 2: install the dependencies
```bash
python -m pip install --no-cache-dir --force-reinstall -r requirements.txt
```
step 3: run the FASTAPI server
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8080
```

step4: Run the local CLI or directly call the API endpoint

to run the CLI execute:
```bash
python src/chat_cli.py
```

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
6. Typo correction (e.g. typo of city names)