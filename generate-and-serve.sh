#!/bin/bash

# Generate the Allure report
allure generate /app/allure-results --clean -o /app/default-reports

# Serve the Allure report
allure serve /app/default-reports --port 5051
