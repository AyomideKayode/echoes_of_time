/**
 * This file is the entry point of the Firebase application.
 * It imports necessary modules, initializes Firebase app,
 * and defines functions for handling login with email and password.
*/

import './styles.css';
import {
  hideLoginError,
  showLoginState,
  showLoginForm,
  showApp,
  showLoginError,
  btnLogin,
  btnSignup,
  btnLogout,
  btnGetStarted,
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
} from 'firebase/auth';

// import 'dotenv/config'; // Load environment variables from a .env file into process.env

const firebaseApp = initializeApp({
  apiKey: 'AIzaSyDtV79_VTs8QrdXfYz5ksicOVg3I54S6LQ',
  authDomain: 'echoes-of-time.firebaseapp.com',
  projectId: 'echoes-of-time',
  storageBucket: 'echoes-of-time.appspot.com',
  messagingSenderId: '976641569266',
  appId: '1:976641569266:web:90e6ea36c23a82b4c7fb6b',
  measurementId: 'G-0FJR017M90',
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

btnLogin.addEventListener('click', loginEmailPassword);

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
  } catch (error) {
    console.log(`There was an error: ${error}`);
    showLoginError(error);
  }
};

btnSignup.addEventListener('click', createAccount);

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

monitorAuthState();

/**
 * Function to handle the logout process.
 * It signs out the current user using Firebase Auth.
 */
const logout = async () => {
  const loggedOut = await signOut(auth);
  console.log(loggedOut);
};

btnLogout.addEventListener('click', logout);

btnGetStarted.addEventListener('click', () => {
  document.querySelector('section.intro').classList.add('hidden');
  document.querySelector('section.features').classList.add('hidden');
  document.querySelector('section.how-it-works').classList.add('hidden');
  document.querySelector('section.testimonials').classList.add('hidden');
  document.querySelector('footer').classList.add('hidden');
  document.querySelector('#login').classList.remove('hidden');
});