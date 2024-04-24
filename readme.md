# Chatting with multiple PDF files

## Introduction
This project is all about retrieving information from multiple PDF files at the same time. In the process of integrating the ChatPDF API into the GitHub project for managing multiple large PDF files, several observations emerged regarding its functionality and suitability for our requirements.

## Experience with ChatPDF API
### Integration Efforts
Upon attempting to incorporate the ChatPDF API into our project workflow, it became evident that certain limitations existed.
### Limitations Identified
- **Inadequate Support for Multiple Files**: The API's inability to handle multiple PDF files concurrently poses a significant challenge. ChatPDF can only handle one API call to one PDF at a time, which would lead to a workflow like this:
- Question 1:
-- query to PDF1
-- query to PDF2
- Question 2:
-- query to PDF1
-- query to PDF2
etc.
- **Logic Errors and Inaccurate Retrievals**: The API demonstrated instances of logic errors and inaccuracies in retrieving information from table-like structures. Despite tailored queries, the API occasionally yielded incorrect or irrelevant results.
  <img width="695" alt="chatpdf mixed results" src="https://github.com/BartCzech/ChatPDF/assets/81484379/35ed3a13-827d-4439-bc2d-604df579f2dc">
  <img width="647" alt="actual info" src="https://github.com/BartCzech/ChatPDF/assets/81484379/cd757866-207b-4818-bc86-b35491062879">

### TAM structure
The biggest problem encountered seems to be the specification of the TAM document, as the model, having successfully extracted main client requirements, doesn't seem to retrieve relevant information from the TAM document.
1. **Successful Identification of Client Requirements:**
   ![Client Requirements](https://github.com/BartCzech/ChatPDF/assets/81484379/af8bed6d-ee84-4c1a-a83a-fad7506a5d8a)
   The model successfully identified the main client requirements, indicating the effectiveness of the extraction process.
2. **Challenges in Identifying TAM Equivalents:**
   ![TAM Output](https://github.com/BartCzech/ChatPDF/assets/81484379/6d2d40e5-568f-41e7-bd38-71b05edb6693)
