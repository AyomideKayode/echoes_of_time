import { AuthErrorCodes } from 'firebase/auth';

export const txtEmail = document.querySelector('#txtEmail');
export const txtPassword = document.querySelector('#txtPassword');

export const btnLogin = document.querySelector('#btnLogin');
export const btnSignup = document.querySelector('#btnSignup');

export const btnLogout = document.querySelector('#btnLogout');

export const divAuthState = document.querySelector('#divAuthState');
export const lblAuthState = document.querySelector('#lblAuthState');

export const divLoginError = document.querySelector('#divLoginError');
export const lblLoginErrorMessage = document.querySelector(
  '#lblLoginErrorMessage'
);
export const btnGetStarted = document.querySelector('#btnGetStarted');

export const showLoginForm = () => {
  document.querySelector('#login').classList.remove('hidden');
  document.querySelector('#app').classList.add('hidden');
};

export const showApp = () => {
  document.querySelector('#login').classList.add('hidden');
  document.querySelector('#app').classList.remove('hidden');
};

export const hideLoginError = () => {
  divLoginError.classList.add('hidden');
  lblLoginErrorMessage.innerHTML = '';
};

export const showLoginError = (error) => {
  divLoginError.classList.remove('hidden');
  if (error.code == AuthErrorCodes.INVALID_PASSWORD) {
    lblLoginErrorMessage.innerHTML = `Wrong password. Try again.`;
  } else {
    lblLoginErrorMessage.innerHTML = `Error: ${error.message}`;
  }
};

export const showLoginState = (user) => {
  lblAuthState.innerHTML = `You're logged in as ${user.displayName} (uid: ${user.uid}, email: ${user.email}) `;
};

hideLoginError();
