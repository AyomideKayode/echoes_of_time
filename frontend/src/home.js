import './styles.css';
import { getAuth, signOut, onAuthStateChanged } from 'firebase/auth';
import { showLoginState, btnLogout, hideLoginError, showApp } from './ui';

document.addEventListener('DOMContentLoaded', (event) => {
  console.log('DOM fully loaded and parsed');

  const auth = getAuth(); // initialize Firebase Auth

  const monitorAuthState = async () => {
    onAuthStateChanged(auth, (user) => {
      if (user) {
        console.log('User logged in:', user);
        showLoginState(user);
        // showApp();
        // hideLoginError();
      } else {
        console.log('No user logged in, redirecting to login page');
        window.location.href = 'login_signup.html';
      }
    });
  };

  const logout = async () => {
    console.log('Logout function called');
    try {
      await signOut(auth);
      console.log('User signed out successfully, redirecting to login page');
      window.location.href = 'login_signup.html'; // Redirect to login page after logout
    } catch (error) {
      console.error('Logout failed:', error);
    }
  };

  console.log('btnLogout:', btnLogout);
  if (btnLogout) {
    btnLogout.addEventListener('click', logout);
    console.log('Logout button event listener attached');
  } else {
    console.error('Logout button not found');
  }

  monitorAuthState();
});
