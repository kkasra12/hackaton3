# Overall idea
The overall idea was to save some of the information in the blockchain (the data that should be transparent and immutable) and the remaining data which contains sensitive information should be saved in the local database. 

# How to run the project
well normally we couldn't finish the project completely but we have these things:
- The smart contract is deployed on the SmaprtPy (named `template_contract_for_resources.py`) and then it will be compiled using online IDE and then we have the TZ file (named `resource_contract.tz`)
- and then we have the `contract_managers.py` which contains a class to create and call the entry points of the smart contract, simply we can deploy a contract with:
```python
contract_manager("resource_contract.tz").send_contract(
        {
            "availability": 2,
            "carbon_footprint": 200,
            "technical_compliance": str(
                {"certification": "ISO 9001", "compliance": "EU"}
            ),
            "price": 1000,
        },
        verbose=1,
    )
```
- We have the database structure in the `database.sql` file (we need to add more SQL functions to the database to make it more useful)

- We have the `database_manager.py` which contains a class to connect to the database and make some operations on it, and have the outputs as a simple `dict` object.

> NOTE: I made these things to have a structral project and to make it easy to continue the project in the future. and also, we can convert it to an API very easily.

- finally, we have the `__init__.py` file which is a simple flask call to other codes.

> ALSO we have very static front-end design [here](https://greenmarketsol.000webhostapp.com/)

