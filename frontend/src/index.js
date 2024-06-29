/**
 * This file is the entry point of the Firebase application.
 * It imports necessary modules, initializes Firebase app,
 * and defines functions for handling login with email and password,
 * creating a new account, monitoring the authentication state,
 * and logging out.
*/

import './styles.css';
import { config } from 'dotenv';
config(); // Load environment variables from a .env file into process.env
import process from 'process/browser'; // polyfill for process.browser
import {
  hideLoginError,
  showLoginState,
  showLoginForm,
  showApp,
  showLoginError,
  btnLogin,
  btnSignup,
  btnLogout,
  // btnGetStarted,
  lblAuthState,
} from './ui';

import { initializeApp } from 'firebase/app';
import {
  getAuth,
  onAuthStateChanged,
  signOut,
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  connectAuthEmulator,
  sendEmailVerification,
} from 'firebase/auth';

const firebaseApp = initializeApp({
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: process.env.FIREBASE_AUTH_DOMAIN,
  projectId: process.env.FIREBASE_PROJECT_ID,
  storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
  messagingSenderId: process.env.FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.FIREBASE_APP_ID,
  measurementId: process.env.FIREBASE_MEASUREMENT_ID,
});

const auth = getAuth(firebaseApp); // initialize Firebase Auth
// use connectAuthEmulator when testing user authentication
// in which case we run `firebase emulators:start --only --project echoes-of-time`
// to start the Auth Emulator. And we connect to it using the port provided in the terminal.
// every signup and login done will only reflect in the emulator and not in the Firebase console.
// connectAuthEmulator(auth, 'http://localhost:9099'); // connect to the Auth Emulator

/**
 * Function to handle login with email and password.
 * It retrieves the email and password from the input fields,
 * attempts to sign in using Firebase Auth,
 * and handles any errors that occur during the process.
 */
const loginEmailPassword = async () => {
  const loginEmail = txtEmail.value;
  const loginPassword = txtPassword.value;

  if (!loginEmail || !loginPassword) {
    showLoginError({ message: 'Please fill out both fields.' });
    return;
  }
  // error handling
  try {
    await signInWithEmailAndPassword(auth, loginEmail, loginPassword);
  } catch (error) {
    console.log(`There was an error: ${error}`);
    showLoginError(error);
  }
};

/**
 * Function to create a new account using email and password.
 * It retrieves the email and password from the input fields,
 * attempts to create a new user using Firebase Auth,
 * and handles any errors that occur during the process.
 *
 * @async
 * @function createAccount
 * @returns {Promise<void>} A promise that resolves when the account is successfully created.
 * @throws {Error} If there is an error during the account creation process.
 */
const createAccount = async () => {
  const email = txtEmail.value;
  const password = txtPassword.value;

  try {
    const userCred = await createUserWithEmailAndPassword(
      auth,
      email,
      password
    );
    console.log(`User created: ${userCred.user.email}`);

    // send email verification
    await sendEmailVerification(auth.currentUser);
    console.log('Verification email sent.');
    alert('Verification email sent. Please verify your email.');

    // format last_login to match the backend format
    const lastLogin = new Date().toISOString().split('.')[0] + 'Z';
    // hardcode username to be the first part of the email before the @ symbol
    const userName = email.split('@')[0];
    // env variable for the API key
    const xApiKey = process.env.X_API_KEY;

    // prepare the POST data request to the backend
    const postData = {
      id: userCred.user.uid,
      username: userName,
      email: email,
      last_login: lastLogin,
    };

    console.log('Sending POST request to backend with data:', postData);

    // Send a POST request to the backend
    const response = await fetch('http://127.0.0.1:5000/api/v1/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-API-KEY': xApiKey,
      },
      body: JSON.stringify(postData),
    });

    if (response.ok) {
      const result = await response.json();
      console.log('User saved to backend:', result);
    } else {
      const error = await response.json();
      console.error('Error saving user to backend:', error);
    }
  } catch (error) {
    console.log(`There was an error: ${error}`);
    showLoginError(error);
  }
};

/**
 * Function to monitor the authentication state of the user
 * and update the UI accordingly.
 */
const monitorAuthState = async () => {
  onAuthStateChanged(auth, (user) => {
    if (user) {
      console.log(user);
      showApp();
      showLoginState(user);

      hideLoginError();
    } else {
      showLoginForm();
      lblAuthState.innerHTML = 'You are not logged in.';
    }
  });
};

/**
 * Function to handle the logout process.
 * It signs out the current user using Firebase Auth.
 */
const logout = async () => {
  const loggedOut = await signOut(auth);
  console.log(loggedOut);
};

btnLogin.addEventListener('click', loginEmailPassword);
btnSignup.addEventListener('click', createAccount);
btnLogout.addEventListener('click', logout);

const btnGetStarted = document.querySelector('#btnGetStarted');
// Redirect to login/signup page when Get Started button is clicked
if (btnGetStarted) {
  btnGetStarted.addEventListener('click', () => {
    window.location.href = 'login_signup.html';
  });
}

monitorAuthState();
