# Echoes of Time Frontend

Welcome to the frontend of the Echoes of Time project! This README provides detailed information on the structure, functionality, and setup of the frontend folder.

## Project Structure

```bash
frontend
│   ├── dist/                    # Compiled output from webpack
│   ├── src/
│   │   ├── index.js             # Entry point of the Firebase application
│   │   ├── ui.js                # UI manipulation functions and element references
│   │   ├── styles.css           # Application styles
│   │   ├── index.html           # Main HTML file
│   │   ├── login_signup.html    # HTML file for login and signup
│   ├── package.json             # Project dependencies and scripts
│   ├── webpack.config.js        # Webpack configuration
│   ├── firebase.json            # Firebase emulator configuration
│   └── .env                     # Environment variables
```

## Installation

- **Clone the repository:**

```bash
git clone https://github.com/your-repo/echoes-of-time.git
cd echoes-of-time/frontend
```

- **Install dependencies:**

```bash
npm install
```

- **Setup environment variables:**

  - Create a .env file in the frontend directory and add the following:

    ```env
    FIREBASE_API_KEY=your_firebase_api_key
    FIREBASE_AUTH_DOMAIN=your_firebase_auth_domain
    FIREBASE_PROJECT_ID=your_firebase_project_id
    FIREBASE_STORAGE_BUCKET=your_firebase_storage_bucket
    FIREBASE_MESSAGING_SENDER_ID=your_firebase_messaging_sender_id
    FIREBASE_APP_ID=your_firebase_app_id
    FIREBASE_MEASUREMENT_ID=your_firebase_measurement_id
    X_API_KEY=your_backend_api_key
    ```

- **Run the project:**

  - Terminal 1:
  
    ```bash
    npx webpack
    ```

  - Terminal 2:

    ```bash
    firebase serve --only hosting --project echoes-of-time
    ```

## Detailed File Descriptions

### `frontend/src/index.js`

This file serves as the entry point of the Firebase application. It initializes the Firebase app, handles user authentication, and updates the UI accordingly.

- Key Functions:

  - `saveUserToBackend`: Helper function that handles formatting the user data and sending it to the backend.
  - `loginEmailPassword`: Handles login with email and password.
  - `createAccount`: Creates a new user account and sends a verification email.
  - `monitorAuthState`: Monitors the authentication state and updates the UI.
  - `logout`: Handles user logout.
  - `loginWithGoogle`: Handles Google Sign-In for users who prefer to use their Google accounts.

- Event Listeners:

  - `btnLogin`: Triggers the loginEmailPassword function.
  - `btnSignup`: Triggers the createAccount function.
  - `btnGoogle`: Triggers the loginWithGoogle funtion.
  - `btnLogout`: Triggers the logout function.
  - `btnGetStarted`: Redirects to the login/signup page.

### `frontend/src/ui.js`

This file contains functions for manipulating the UI and references to HTML elements.

- Key Functions:

  - `showLoginForm`: Displays the login form and hides the main app.
  - `showApp`: Displays the main app and hides the login form.
  - `hideLoginError`: Hides any login error messages.
  - `showLoginError`: Displays login error messages.
  - `showLoginState`: Displays the current authentication state.

- HTML Element References:

  - `txtEmail`: Input field for email.
  - `txtPassword`: Input field for password.
  - `btnLogin`: Login button.
  - `btnSignup`: Signup button.
  - `btnLogout`: Logout button.
  - `divAuthState`: Div displaying authentication state.
  - `lblAuthState`: Label displaying authentication state.
  - `divLoginError`: Div displaying login errors.
  - `lblLoginErrorMessage`: Label displaying login error messages.

### `frontend/webpack.config.js`

This is the configuration file for webpack, which bundles the JavaScript files for usage in the browser.

- Key Points:

  - Entry Point: `src/index.js`
  - Output Directory: `dist/`
  - Plugins:
    - `HtmlWebpackPlugin` for generating HTML files.
    - `Dotenv` for loading environment variables.

### `frontend/package.json`

This file lists the project's dependencies and scripts.

- Scripts:

  - `build`: Runs webpack to bundle the application.

- Dependencies:

  - `dotenv`: For loading environment variables.
  - `firebase`: For Firebase functionalities.
  - `dotenv-webpack`: For using environment variables with webpack.

- DevDependencies:

  - `buffer`, `crypto-browserify`, `css-loader`, `html-webpack-plugin`, `os-browserify`, `path-browserify`, `stream-browserify`,
  - `style-loader`, `vm-browserify`, `webpack`, `webpack-cli`: Various tools and loaders required for webpack and polyfills for browser compatibility.

### `frontend/firebase.json`

This file contains configuration for Firebase emulators.

- Key Points:

  - `Auth Emulator`: Runs on port 9099.
  - `Hosting Emulator`: Runs on port 5001.
  - `UI Emulator`: Enabled.
  - `Single Project Mode`: Enabled.
  - `Public Directory`: dist/

### HTML and CSS Files

- `index.html`: Main HTML file for the application.
- `login_signup.html`: HTML file for login and signup pages.
- `styles.css`: Contains styles for the application.

## Running the Firebase Emulator

To start the Firebase emulator, run the following command:

```bash
firebase emulators:start --only auth hosting --project echoes-of-time
```

This will start the Auth and Hosting emulators for local development.

### Additional Information

The project uses Firebase for authentication and a backend server for managing user data. The environment variables need to be correctly set up for the application to work properly.

For any issues or questions, feel free to open an issue in the GitHub repository or contact the project maintainers.
