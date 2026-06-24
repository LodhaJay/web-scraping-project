# Web Scraping & Data Collection Internship Project

## Overview

This repository contains all assignments and projects completed during my Data Collection, Data Cleaning, and Web Scraping Internship.

The primary goal of this internship is to understand how real-world datasets are collected, cleaned, structured, and prepared for future AI/ML applications.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Technologies Used

- Python
- Requests
- BeautifulSoup
- Pandas
- Selenium
- Playwright
- JSON
- CSV
- Excel
- Logging
- Git & GitHub

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Project Roadmap

## Phase 1: HTML & Requests Fundamentals

### Objective
Understand website structure and basic scraping concepts.

### Concepts Learned
- HTML Page Structure
- Requests
- BeautifulSoup
- HTML Tags
- CSS Selectors
- CSV Handling

### Project
Scraped quotes from QuotesToScrape.

### Data Collected
- Quote Text
- Author
- Tags

### Output
- CSV Dataset
- JSON Dataset

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 2: Pagination Scraping

### Objective
Learn multi-page scraping.

### Concepts Learned
- Loops
- URL Generation
- Error Handling

### Project
Scraped all pages from QuotesToScrape.

### Data Collected
- Every Quote
- Every Author

### Output
- Single Merged Dataset

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 3: Real Dataset Collection

### Objective
Build large-scale structured datasets.

### Website
- books.toscrape.com

### Data Collected

- Title
- Category
- Price
- Availability
- Stock Count
- UPC
- Product Type
- Reviews
- Star Rating
- Description
- Product URL
- Image URL

### Additional Work
- Downloaded book cover images
- Generated complete dataset with detailed metadata

### Output
- Excel Dataset
- Product Images

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 4: Data Cleaning

### Objective
Learn real-world data preparation techniques.

### Tasks Performed

- Removed Duplicates
- Handled Missing Values
- Normalized Columns
- Validated Records
- Standardized Data Formats

### Tools Used

- Pandas

### Output

- Raw Dataset
- Cleaned Dataset
- Data Cleaning Report

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 5: Advanced Web Scraping

### Objective
Handle production-style scraping scenarios.

### Concepts Learned

- Request Headers
- User-Agent Rotation
- Session Management
- Cookies
- Retry Mechanisms
- Rate Limiting
- Robots.txt
- Logging

### Projects

#### The Hindu E-Paper Scraper

Not scraped data as robot.txt disallowed scraping

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 6: Dynamic Website Scraping

### Objective
Scrape JavaScript-rendered websites.

### Concepts Learned

- Selenium
- Playwright
- Browser Automation
- Waiting Strategies
- Infinite Scroll
- Lazy Loading

### Projects

#### Data Scientist Job Scraper

Collected:

- Job Titles
- Company Names
- Job Descriptions
- upload time
- company rating 
- location
- salary
- job type

### Output

- Structured Datasets

#### Bambu Lab Product Collection

Collected product information from multiple distributors:

- 3idea
- Ideal3D
- Wol3D

### Data Collected

- Product Title
- Price
- Description
- Features
- Ratings(if available)
- review counts(if availabile)
- Product Images

### Output

- Product Datasets
- Image Collections

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Phase 7: NSE India Data Discovery (In Progress)

### Objective

Perform reconnaissance and source cataloging of NSE India resources.

### Scope

- Website Discovery
- Sitemap Discovery
- URL Discovery
- API Discovery
- Dataset Cataloging
- Metadata Extraction
- Data Lineage
- Source Mapping

### Deliverables

- Source Registry
- Dataset Registry
- API Registry
- Documentation

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Repository Structure

web-scraping-project/
│
├── src/
│   ├── phase_1_quotes_scraping.ipynb
│   ├── phase_2_quotes_scraping.ipynb
│   ├── phase_3_books_dataset.ipynb
│   ├── phase_4_data_cleaning.ipynb
│   ├── phase_6_ideal3d_bambu.py
│   ├── phase_6_3idea_bambu.py
│   └── phase_6_wol3d_bambu.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── README.md
├── requirements.txt
└── .gitignore
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Key Skills Developed

### Data Collection
- Dataset Building
- Web Data Extraction
- Image Collection

### Data Engineering
- Data Validation
- Data Cleaning
- Data Transformation

### Web Scraping
- Requests
- BeautifulSoup
- Selenium
- Playwright

### Software Engineering
- Error Handling
- Logging
- File Management
- Git Version Control

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
