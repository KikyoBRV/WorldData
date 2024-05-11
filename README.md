# WorldData
  WorldData is a Python-based app with a GUI interface. This app provides general data on 195 countries worldwide, allowing users to view statistics on various attributes through visualization, including various types of graphs.

## Data Source
This project using [Global Country Information Dataset 2023](https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023/data) as a data source.
(This data has some errors, such as errors in country names, but I have already fixed them. Additionally, I have added the region of each country to the data.)

## Running the Application
### Requirements
The program needs to be run with the following packages installed (that are in requirements.txt):

* customtkinter==5.2.2
* matplotlib==3.8.4
* pandas==2.2.2
* pillow==10.3.0
* numpy==1.26.4
* networkx==3.3
### How to run the program
1. Clone the repository
```
git clone https://github.com/KikyoBRV/WorldData.git
```
2. Change your directory to WorldData
```
cd WorldData
```
3. Create virtual environment
```
py -m virtualenv env
```
4. Activate the virtual environment
```
# On Linux or MacOS
source env/bin/activate

# On MS Windows
env\Scripts\activate
```
5. Installing requirement library
```
pip install -r requirements.txt
```
6. Run the application
```
# On MacOS
python3 main.py

# On MS Windows
python main.py
```

## Functions currently available
* User can use all function in "Statistic Data" page. 
* Other feature will be updated as soon as possible