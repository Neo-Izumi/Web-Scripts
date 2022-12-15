# Brute-forcing a stay-logged-in cookie

### Link to the lab: https://portswigger.net/web-security/authentication/other-mechanisms/lab-brute-forcing-a-stay-logged-in-cookie

1. open **Burp Suite**
2. log in to the given account in the lab description and keep in your mind that you have to check the 'remember me' checkbox
3. in **Burp Suite** - **Proxy** - **HTTP history**, take a closer look at the *GET /my-account*, you'll see a *stay-logged-in* cookie was generated
4. select that cookie value and notice the **Inspector** bar, you'll see:
    - **Select text**: the text you've just selected
    - **Decoded from**: the decoded form (from detected encode function) of the *Select text* 
5. from the string you received in **Decoded from**, notice that it was created from username and ':' and md5 encoded form of password
6. log out from your account
7. run the **Stay-Logged_in Cookie.py** file with your new url    