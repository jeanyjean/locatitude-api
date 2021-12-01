Locatitude API
===============
**Locatitude API** is an API for getting various information regarding your visited location.

This API provides the following :
* Latitude and Longitude of the visited location
* PM 2.5 of the visited location
* Population in the visited location
* Number of Covid 19 cases near the visited location
* Covid19 trend for each province
* PM2.5 trend for each province
* Infection rate of 1 million people per day for visited province

Access [Locatitude Swagger UI](loca-titude.herokuapp.com/locatitude/ui) or run locally(with graphs) below

## How to run the API locally.<br />
1. Access to a command-line/terminal window and clone/download code from github.
    ```bash
    git clone https://github.com/jeanyjean/locatitude-api.git
    ```
2. Access to a command-line/terminal window and change directory to the directory that contain `locatitude-api` folder, create and activate a virtual environment.
    ```bash
    python3.9 -m venv env
    env/bin/activate # macOS and Linux
    env\Scripts\activate.bat # Windows
    ```
3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement.txt
    ```bash
    pip install -r requirements.txt
    ```
4. Start the REST API server 
    ```bash
    python app.py
    ```
5. Test the API at http://localhost:8080//locatitude/ui

7. In another terminal, run openapi-to-graphql with CORS
(Cross-Origin Resource Sharing) enabled.
    ```bash
    openapi-to-graphql --cors -u http://localhost:8080/locatitude openapi/locatitude-api.yaml
    ```

8. Open the page http://localhost:3000/graphql <br />
 The browser should display GraphQL window

9. Open the file `html/index.html` with your web browser <br />

    ![alt text](https://sv1.picz.in.th/images/2021/11/30/6g5vs9.jpg)

10. Click on the button to view each data visualization

## Group member
1. Panida Ounnaitham 6210545513
2. Purich Trainorapong 6210545581
3. Phakarat Khongphaisan 6210546412
