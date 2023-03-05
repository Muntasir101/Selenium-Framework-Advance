# Selenium-Framework-Advance
Selenium Framework using POM

# Activate the virtual environment
source venv/bin/activate

# Install the dependencies
pip install -r requirements.txt

# Run the tests and generate an Allure report
pytest --alluredir=./allure-results
allure serve allure-results/

