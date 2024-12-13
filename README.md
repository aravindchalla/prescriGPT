# PrescriGPT
The PrescriGPT project harnesses the capabilities of Generative AI (GenAI) to revolutionize healthcare by providing personalized medicine recommendations. Leveraging datasets like MIMIC-III and PresData, the system processes user inputs, including symptoms and medical history, to deliver actionable and accurate healthcare advice. The architecture integrates a user-friendly front-end, robust back-end processing powered by ChatGPT APIs, and an iterative feedback mechanism to ensure continuous improvement. By prioritizing data privacy, regulatory compliance, and scalability, the project bridges critical gaps in healthcare accessibility, paving the way for smarter and more reliable medical solutions.

# Dependencies
1. Python (>= 3.6)
2. Textbase library (Install using pip install textbase)
3. OpenAI API Key

### Installation : 

Clone the repository
``` git clone <repository_link> ```

Install Virtual Environment 
``` python -m venv your_virtual_name ```

Activate Virtual Environment 
```your_virtual_name\scripts\activate```

Please change the api-key in the main.py file: 

We chose not to include the API key in the code to avoid potential security risks. Since our GitHub repository will be public, exposing the API key could allow others to misuse it, leading to unauthorized usage. This could result in overutilization of the OpenAI API, which would incur charges on our credit card, posing a financial risk. 

Use the following command to run
``` poetry run python3 -W ignore textbase/textbase_cli.py test main.py```