# 2FA broken logic

### Link to the lab: https://portswigger.net/web-security/authentication/multi-factor/lab-2fa-bypass-using-a-brute-force-attack

in this problem, we have to brute-force the security code.

  - at first, login to to provided account, you'll be required to enter a security code.
  - next, click **Email client** button to get your code.
  - modify the *GET /login2* request (change cookie). this action will make server send a security code to carlos's real email
  - send the POST request with cookie verify is carlos and data mfa-code is brute-forced