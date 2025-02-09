For Windows:
1. VS code
2. Create virtual environment by python -m venv <name>
3. Activate environment .\<name>\Scripts\activate
4. If not possible go to windows start menu - type powershell and run it as administrator
5. type pip  -  and then  A (all)
6. GO to 3 again - check terminal has (venv) in command 
7. pip install selenium
8. pip install behave
9. pip install webdriver_manager
10. pip install selenium webdriver_manager
11. on bottom right corner select interpritour if needed
12. check venv path in settings - search for venv and add path

Remarks:
if in powershell behave is not working then run it in debug mode first
disable pylance

How to run a test:
1. one test: behave -n 'name'
2. all tests at once: behave

For MAC/Linux
1. sudo apt update && sudo apt install -y python3 python3-pip python3-venv
2. python3 -m venv <name>
3. source <name>/bin/activate 
4. pip install selenium
5. pip install behave
6. sudo apt install -y google-chrome-stable
7. pip install chromedriver-autoinstaller 

