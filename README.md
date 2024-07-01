

## ALTEN Website testing

### Description:

This project was created as an example of my work on a framework of automated website testing. 

Used:
* Python
* Selenium
* Behave (Gherkin/BDD)

### Estructure:

project/  
├drivers/  
├features/       
│  ├── busca_empleo.feature  
│  ├── ver_detalles_oferta.feature  
├steps/           
│   ├── busca_empleo_steps.py  
│   ├── detalle_empleo_steps.py  
├pages/           
│   ├── base_page.py  
│   ├── resultados_empleo_page.py  
├utils/          
│   ├── utils.py  
├reports/    
├environment.py  
└README.md        


### Prerequisites:

Python installed is required. [Tutorial here](https://www.freecodecamp.org/news/how-to-install-python-in-windows-operating-system/)

* Install Selenium on terminal
```
pip install selenium
```
* Install Behave on terminal
```
pip install behave
```

### How to run it:
After downloading the repository on your local machine, run the test in the terminal as it follows:
```
behave
```
A **reports** folder will be created.
It will create a **test_results.csv** file into the **reports** folder. The results will be added with each execution. 
A **screenshots** file will be created into the **reports** folder as well, where the evidence will be stored by date/scenario as screenshots.

### Author:
Mercedes Pérez [MerPC](https://github.com/MerPC)

[mmcomesana@proton.me](mailto:mmcomesana@proton.me)

### License:
Distributed under the [MIT License](https://license.md/licenses/mit-license/)


