# Chatting with multiple PDF files

## Introduction
This project is all about retrieving information from multiple PDF files at the same time. In the process of integrating the ChatPDF API into the GitHub project for managing multiple large PDF files, several observations emerged regarding its functionality and suitability for our requirements.

## Experience with ChatPDF API
### Integration Efforts
Upon attempting to incorporate the ChatPDF API into our project workflow, it became evident that certain limitations existed.
### Limitations Identified
- **Inadequate Support for Multiple Files**: The API's inability to handle multiple PDF files concurrently poses a significant challenge. ChatPDF can only handle one API call to one PDF at a time, which would lead to a workflow like this:
Question 1:
- query to PDF1
- query to PDF2
Question 2:
- query to PDF1
- query to PDF2
etc.
- **Logic Errors and Inaccurate Retrievals**: Notably, the API demonstrated instances of logic errors and inaccuracies in retrieving information from PDF documents. Despite tailored queries, the API occasionally yielded incorrect or irrelevant results.
  <img width="695" alt="chatpdf mixed results" src="https://github.com/BartCzech/ChatPDF/assets/81484379/35ed3a13-827d-4439-bc2d-604df579f2dc">
  <img width="647" alt="actual info" src="https://github.com/BartCzech/ChatPDF/assets/81484379/cd757866-207b-4818-bc86-b35491062879">


