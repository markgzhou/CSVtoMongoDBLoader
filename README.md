# CSV to MongoDB Loader
The tool loads a CSV file and insert each row as a document to MongoDB

Python version required v3.5.X+


Required Python packages:
- Install pymongo with [pip](https://pypi.python.org/pypi/pip/): `pip install pymongo`
- Install csv with [pip](https://pypi.python.org/pypi/pip/): `pip install csv`

Default configuration at the beginning of the script:
- FILE_LOCATION='data/zipcode-database-Primary.csv'
- MONGODB_CONNECTION='localhost'
- MONGODB_PORT=27017