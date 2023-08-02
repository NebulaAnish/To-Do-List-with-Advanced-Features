# To Do List API with Advanced Features
This is a to do list api with some advanced features. The API isn't protected as of now and can be accessed without using access token. The API has following features:

- Basic CRUD operations.
- CSV File Upload to bulk update database contents.
- Export database table as CSV.
- Pagination with page and count query paramters.
- Case in-sensitive search.
- Filter items based on paramters.
- Order items in either ascending or descending order with respect to one of it's properties.


Below are the steps to clone this project and get the server running. Refer to `documentation.md` file for information about the accessible endpoints

## Steps
- Setup the virtual environment:

    `$ python -m venv .venv`
- Activate virtual environment
    Run the following commands by heading to the location where .venv is created.
    - Windows:  `$.venv/scripts/activate`
    - Linux: `$ source .venv/bin/activate`
- Clone the repository.

    `$git clone https_link`
- Install the required dependencies.

    `$pip install -r requirements.txt`
- Start the server.

    `$python manage.py runserver `

- Now visit the appropriate endpoint through browser, postman, curl or other tools. Refer documentation for information about the available endpoints.