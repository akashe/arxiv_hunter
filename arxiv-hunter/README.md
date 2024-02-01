# Project Structure (without comments)

```bash
arxiv-hunter
├── README.md
├── requirements.txt
├── template.yaml
├── src
│   ├── app
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── services.py
│   │   ├── utils.py
│   │   ├── auth
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── user.py
│   │   ├── search
│   │   │   ├── __init__.py
│   │   │   ├── search.py
│   │   │   └── index.py
│   │   └── recommend
│   │       ├── __init__.py
│   │       ├── recommend.py
│   │       └── preference.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   └── test_app.py
│   └── lambda_handler.py
└── frontend
    ├── package.json
    ├── public
    │   └── index.html
    └── src
        ├── index.js
        ├── App.js
        ├── components
        │   ├── Header.js
        │   ├── Content.js
        │   └── Footer.js
        └── styles
            ├── index.css
            ├── App.css
            ├── Header.css
            ├── Content.css
            └── Footer.css

```

# Project Structure (with comments)

```bash
arxiv-hunter
├── README.md # project documentation
├── requirements.txt # project dependencies
├── template.yaml # aws serverless application model template
├── src # folder that contains source code for the backend application
│   ├── app # folder that contains the FastAPI app
│   │   ├── __init__.py # initializes the FastAPI app instance and imports the dependencies
│   │   ├── main.py # defines the routes and endpoints for your API to handle the requests and responses
│   │   ├── config.py # configuration settings for the app - database URL, secret key, and logging level
│   │   ├── models.py # defines the database models for the app
│   │   ├── schemas.py # defines the Pydantic schemas for the app for data validation and serialization
│   │   ├── services.py # contains the business logic and service layer for the app - functions to interact with the database and perform the core functionality of the app
│   │   ├── utils.py # contains the utility functions and helpers for the app - functions to generate and verify tokens, handle errors, and send emails
│   │   ├── auth # folder that contains source code related to user registration and authentication
│   │   │   ├── __init__.py
│   │   │   ├── auth.py # it defines the authentication routes and dependencies
│   │   │   └── user.py # it defines the user model and schema
│   │   ├── search # folder that contains source code related to the search feature for the users
│   │   │   ├── __init__.py
│   │   │   ├── search.py # define the search routes and dependencies
│   │   │   └── index.py # create and update TFIDF index
│   │   └── recommend # folder that contains source code related to the recommendation feature
│   │       ├── __init__.py
│   │       ├── recommend.py # define the recommendation routes and dependencies (import user & index)
│   │       └── preference.py # define the preference model and schema
│   ├── tests # folder that contains the unit tests for the app
│   │   ├── __init__.py
│   │   ├── conftest.py # sets up fixtures and mocks for the tests - test client, test database, and test data
│   │   └── test_app.py # contains the test cases for the app
│   └── lambda_handler.py # defines the Lambda handler function for the application, using the mangum library (adapter between the Lambda event and the FastAPI app)
└── frontend # folder that contains the source code for the frontend app (React app that uses the create-react-app tool to bootstrap the project)
    ├── package.json # define JavaScript dependencies and scripts (use npm or yarn to install them with the command npm install or yarn install)
    ├── public # folder that contains the static assets for the project - the HTML template, the favicon, and the manifest
    │   └── index.html # defines the HTML template for the project, has a root element where the React app is rendered
    └── src # folder that contains the JavaScript and CSS code for the project
        ├── index.js # renders the React app to the root element in the HTML template
        ├── App.js # defines the main component for the app, it uses the react-router-dom library to handle the routing and navigation, it also renders the header, the content, and the footer components
        ├── components # folder that contains the reusable components for the app
        │   ├── Header.js # defines the header component for the app, it displays the logo and the navigation links
        │   ├── Content.js # defines the content component for the app, it displays the main content of the app, such as the forms, the tables, the charts, and the messages
        │   └── Footer.js # defines the footer component for the app, it displays some information and links about the project and the company
        └── styles # folder that contains the CSS styles for the app
            ├── index.css # defines the global styles for the app - the font, the color scheme, and the layout
            ├── App.css # defines the styles for the main component of the app - the background and the margin
            ├── Header.css # defines the styles for the header component of the app - the logo, the font size, and the alignment
            ├── Content.css # defines the styles for the content component of the app - the forms, the tables, the charts, and the messages
            └── Footer.css # defines the styles for the footer component of the app, such as the font size, the color, and the links
```
