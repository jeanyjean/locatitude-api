Locatitude API Server
===============
Locatitude API for getting information from your location

## How to run your tests.<br />
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
3. Generate code from the OAS (type them all in one line, For Windows’ command prompt, use the ^ character instead of \ to continue on the second line)
    ```bash
    java -jar openapi-generator-cli-X.Y.Z.jar generate \
    -i openapi/locatitude-api.yaml -o autogen -g python-flask
    ```
4. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement.txt
    ```bash
    pip install -r requirements.txt
    ```
5. Start the REST API server 
    ```bash
    python app.py
    ```
6. Optionally test the API at http://localhost:8080//locatitude/ui

7. In another terminal, run openapi-to-graphql with CORS
(Cross-Origin Resource Sharing) enabled.
    ```bash
    openapi-to-graphql --cors -u http://localhost:8080/locatitude openapi/locatitude-api.yaml
    ```

8. Open the page http://localhost:3000/graphql <br />
 The browser should display GraphQL window

9. Open the file html/index.html with your web browser
![alt text](https://sv1.picz.in.th/images/2021/11/28/6Zt3vI.jpg)