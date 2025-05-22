## Getting an Access Token

1. **Register your application in Asana**
   - Go to [Asana's Developer Console](https://app.asana.com/0/developer-console)
   - Click "Create new app"
   - Provide a name and agree to API terms

2. **Configure OAuth Settings**
   - In your app settings, navigate to "OAuth"
   - Add a Redirect URL: `urn:ietf:wg:oauth:2.0:oob` (for CLI applications) or `localhost_etc.com` for web app.
   - Note your Client ID and Client Secret

3. **Get Authorization Code**
   - Open this URL in your browser (replace YOUR_CLIENT_ID):
     ```
     https://app.asana.com/-/oauth_authorize?client_id=YOUR_CLIENT_ID&redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=code&state=random_state
     ```
   - After authorization, you'll receive a code

4. **Exchange Code for Access Token**
   - Run this command (replace placeholders):
     ```bash
     curl -X POST https://app.asana.com/-/oauth_token \
       -H "Content-Type: application/x-www-form-urlencoded" \
       -d "grant_type=authorization_code" \
       -d "client_id=YOUR_CLIENT_ID" \
       -d "client_secret=YOUR_CLIENT_SECRET" \
       -d "redirect_uri=urn:ietf:wg:oauth:2.0:oob" \
       -d "code=AUTHORIZATION_CODE"
     ```
   - Save the returned `access_token`

5. **Use the token in the client.py script**
   - Replace `YOUR_ACCESS_TOKEN` with your actual token

