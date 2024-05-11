// LoginPage.js

import React, { useState } from 'react';
import './LoginPage.css'; // Import CSS file
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';

const LoginPage = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [showPassword, setShowPassword] = useState(false);

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  };

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleEmailLogin = () => {
    // Add your email login API call here
    // Example:
    // fetch('YOUR_EMAIL_LOGIN_API_URL', {
    //   method: 'POST',
    //   body: JSON.stringify({ email, password }),
    //   headers: {
    //     'Content-Type': 'application/json',
    //   },
    // })
    // .then(response => response.json())
    // .then(data => {
    //   // Handle login response
    // })
    setError(''); // Clear any previous error
    console.log('Logging in with email:', email, password);
  };

  const handleGoogleLogin = () => {
    // Add your Google login API call here
    // Example:
    // window.location.href = 'YOUR_GOOGLE_LOGIN_REDIRECT_URL';
    console.log('Logging in with Google');
  };

  const handleFacebookLogin = () => {
    // Add your Facebook login API call here
    // Example:
    // window.location.href = 'YOUR_FACEBOOK_LOGIN_REDIRECT_URL';
    console.log('Logging in with Facebook');
  };

  return (
    <div className="login-container">
      <h1>Login</h1>
      {error && <div className="error">{error}</div>}
      <form>
        <label>Email:</label>
        <input type="email" value={email} onChange={handleEmailChange} />
        <label>Password:</label>
        <div className="input-group">
          <input type={showPassword ? "text" : "password"} value={password} onChange={handlePasswordChange} />
          <FontAwesomeIcon icon={showPassword ? faEyeSlash : faEye} className="password-toggle" onClick={togglePasswordVisibility} />
        </div>
        <button type="button" onClick={handleEmailLogin}>Login </button>
      </form>
      <div>
        <button type="button" onClick={handleGoogleLogin}>Continue with Google</button>
        <button type="button" onClick={handleFacebookLogin}>Continue with Facebook</button>
      </div>
    </div>
  );
};

export default LoginPage;
