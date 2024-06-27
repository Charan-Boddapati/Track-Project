- Clone repository and download files to a required folder.
- Open command prompt and change directory to that folder.
  - Use the following command:
    ```bash
    cd C:\Users\chara\Documents\Python  # replace directory with your directory
    ```
- Create a virtual environment using the following command:
    ```bash
    py -m venv env_name
    ```
- Activate environment:
    ```bash
    env_name\scripts\activate.bat
    ```
- Install all the dependencies:
    ```bash
    pip install django
    pip install folium
    pip install six
    ```
- Create an outlook mail and enable POP and IMAP section of sync mail in settings. Use credentials of your mail in info.py file by replacing sample@outlook.com and password
- Run the following command to run the website:
    ```bash
    python manage.py runserver
    ```
- A link will be displayed in the command prompt. Copy the given link and paste it into your browser.
- The home page will be opened. Three login options will be there:
  - User login (Get started button)
  - Admin login
  - Service Provider Login (Bus conductors and rickshaw drivers)
- Open the user login and you will see a signup button. Click that and you will be redirected to the signup page.
- Use your IITG mail to register. A mail will be sent to your IITG email address. A link for activation will be sent to you.
- Copy that link and paste it into your browser. You will be redirected to the home page. You are successfully logged in. Now again click on the get started button.
- You will see two options: Bus and AutoRickshaw. Select on BUS.
- All the bus details will be displayed. All the bus statuses are displayed as Halted because no conductor has logged in for the coordinates to update.
- Now open a new tab using the link from STEP 7. Click on the service provider login.
- Select Bus. Credentials are as follows (I have hardcoded credentials of bus workers):
  - Bus_id: bus_service
  - Password: bus_1234
- Now you should enter to which vehicle you are responsible. Use the following credentials:
  - Bus Number: AP1234
  - Enter any two places as start and end
- A page will open displaying Bus Number and a box to update the number of vacancies. Give location access and wait for some time (approximately 5-10s) to fetch coordinates. These coordinates will be updated to the bus database.
- Now open the page containing bus information in a table in STEP 13. Refresh the page to see updated coordinates and the status of the bus changed to running. Click on generate map and then click on view map. A map will pop up having two markers. The red marker is your location and the blue marker is the bus location. But in this case, as the project is not deployed, both markers will be at the same location.
- Do similar steps for E-rickshaw.
- E-Rickshaw credentials:
  - Rickshaw_number: AR1234
  - Vehicle_key: AR1234pass
- ADMIN login credentials:
  - Username: admin
  - Password: admin12345

