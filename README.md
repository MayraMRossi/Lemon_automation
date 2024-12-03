# Automation Challenge

This project aims to automate the processing of customer emails, classify user intents, and provide a system for querying a help center using Retrieval-Augmented Generation (RAG). The project is structured using SOLID principles, Clean Code, Domain-Driven Design (DDD), Test-Driven Development (TDD), and Hexagonal Architecture.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Design Decisions](#design-decisions)

## Project Structure

The project is structured as follows:
automation-challenge/
│
├── app/
│ ├── adapters/
│ │ ├── input/
│ │ │ ├── email_input_adapter.py
│ │ │ ├── intent_input_adapter.py
│ │ │ └── rag_input_adapter.py
│ │ └── output/
│ │ ├── email_output_adapter.py
│ │ ├── intent_output_adapter.py
│ │ └── rag_output_adapter.py
│ ├── domain/
│ │ ├── models/
│ │ │ ├── email_model.py
│ │ │ ├── intent_model.py
│ │ │ └── rag_model.py
│ │ ├── services/
│ │ │ ├── email_service.py
│ │ │ ├── intent_service.py
│ │ │ └── rag_service.py
│ │ └── repositories/
│ │ ├── email_repository.py
│ │ ├── intent_repository.py
│ │ └── rag_repository.py
│ ├── infrastructure/
│ │ ├── messaging/
│ │ │ ├── task_producer.py
│ │ │ └── task_consumer.py
│ │ ├── nlp/
│ │ │ ├── classifier.py
│ │ │ └── summarizer.py
│ │ ├── persistence/
│ │ │ ├── db_connection.py
│ │ │ ├── email_repository_impl.py
│ │ │ ├── intent_repository_impl.py
│ │ │ └── rag_repository_impl.py
│ │ └── vector_store/
│ │ └── vector_manager.py
│ ├── api/
│ │ ├── email_controller.py
│ │ ├── intent_controller.py
│ │ └── rag_controller.py
│ └── main.py
│
├── tests/
│ ├── test_email_service.py
│ ├── test_intent_service.py
│ └── test_rag_service.py
│
├── data/
│ ├── emails.csv
│ ├── intents.csv
│ └── rag_data.json
│
├── docker-compose.yml
├── requirements.txt
└── README.md

Copy

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/automation-challenge.git
   cd automation-challenge
Install the dependencies:

bash
Copy
pip install -r requirements.txt
Set up the database (if using a local PostgreSQL instance):

bash
Copy
export DATABASE_URL=postgresql://user:password@localhost/dbname
Run the application:

bash
Copy
python app/main.py
Usage
Processing Emails
To process emails, send a POST request to the /emails/process endpoint:

bash
Copy
curl -X POST http://localhost:8080/emails/process
Classifying Intents
To classify intents, send a POST request to the /intents/classify endpoint:

bash
Copy
curl -X POST http://localhost:8080/intents/classify
Querying RAG
To query the RAG system, send a POST request to the /rag/query endpoint:

bash
Copy
curl -X POST http://localhost:8080/rag/query
Testing
To run the tests, use the following command:

bash
Copy
pytest tests/

Design Decisions
SOLID Principles
Single Responsibility Principle (SRP): Each class has a single responsibility, such as EmailService for processing emails.

Open/Closed Principle (OCP): The system is designed to be easily extendable without modifying existing code.

Liskov Substitution Principle (LSP): The repository interfaces (EmailRepository, IntentRepository, RAGRepository) can be substituted with their implementations.

Interface Segregation Principle (ISP): The interfaces are small and specific to the needs of the client.

Dependency Inversion Principle (DIP): High-level modules depend on abstractions rather than concrete implementations.

Clean Code
Meaningful Names: Variables, functions, and classes are named descriptively.

Small Functions: Functions are kept small and focused on a single task.

Comments: Comments are used sparingly and only when necessary to explain complex logic.

Domain-Driven Design (DDD)
Domain Models: The domain package contains the core business logic and models.

Services: The services package contains the application services that orchestrate the use cases.

Repositories: The repositories package contains the interfaces for data access.

Test-Driven Development (TDD)
Unit Tests: Each service has corresponding unit tests in the tests package.

Mocking: Mock objects are used to isolate the unit under test.

Hexagonal Architecture
Adapters: The adapters package contains input and output adapters for reading and writing data.

Infrastructure: The infrastructure package contains the implementation details, such as persistence and messaging.

This structure ensures that the application is modular, maintainable, and scalable.

