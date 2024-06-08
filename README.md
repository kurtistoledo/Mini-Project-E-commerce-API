# E-commerce Application

This is a robust and feature-rich e-commerce application built with Flask and Flask-SQLAlchemy. It includes functionalities for managing customers, products, and orders, with JWT authentication for security.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Database Models](#database-models)
- [Testing](#testing)
- [Docker](#docker)
- [License](#license)

## Features

- **Customer Management**: Create, Read, Update, Delete (CRUD) operations for customers.
- **Customer Account Management**: CRUD operations for customer accounts with secure password handling.
- **Product Management**: CRUD operations for products, including listing and stock level management.
- **Order Processing**: Place, retrieve, and manage orders, including calculating total order price and tracking order status.
- **Authentication**: JWT-based authentication for securing endpoints.
- **Data Validation**: Input validation using Flask-Marshmallow.
- **Error Handling**: Comprehensive error handling and logging.
- **Docker Support**: Dockerized application for consistent development and deployment environments.

## Installation

### Prerequisites

- Python 3.8+
- MySQL
- Node.js and npm (for running Postman collections)
