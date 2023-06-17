# DSE-webScraping
Using BeautifulSoup to scrape certain data from the website and put them in csv files. Next put those data in PostgreSQL using python. Then visualize the data in PowerBI.

<strong>Installations:</strong> <br>
```pip install pandas``` <br>
```pip install python``` <br>
```pip install beautifulsoup4```<br>
```pip install requests```<br>

<strong>For API:</strong> <br>
```pip install djangorestframework```

<strong>For Database: </strong><br>
```Install PostgreSQL```

<strong>For visualization:</strong><br>
```Install PowerBI Desktop```

<h1>Web Scraping</h1>

<ol>
  
  <li>DSE's website was inspected</li>
  <li>The class where the data we want was noted</li>
  <li>BeautifulSoup was used to get response from the website</li>
  <li>Dataframe was created to create the table</li>
  <li>Data was inserted by scraping for each column of the dataframe </li>
  <li>Dataframe was converted into two csv files: companies and holdings </li>
  
</ol>
<br>

<h1>From csv files to PostgreSQL Database</h1>

<ol>
  
  <li>A database was created in PostgreSQL</li>
  <li>Psycopg2 library was used to connect to the database</li>
  <li>Table was created in the database according to the parameters of the csv file data using python</li>
  <li>A loop was used to enter all the data from the csv file to the table in the database</li>
  
</ol>
<br>

<h1>Data Visualization</h1>

<ol>
  
  <li>Microsoft PowerBI was used to visualize the data</li>
  <li>The extracted data of the csv file was transformed and loaded into PowerBI</li>
  <li>Different cards, charts, filters, slicers and tables were used to show the data and comparison we needed to see</li>
  
</ol>
