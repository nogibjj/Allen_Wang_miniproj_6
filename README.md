# Allen_Wang_miniproj_6

[![CI](https://github.com/nogibjj/Allen_Wang_miniproj_6/actions/workflows/CICD.yml/badge.svg)](https://github.com/nogibjj/Allen_Wang_miniproj_6/actions/workflows/CICD.yml)

## Overview

This project demonstrates connecting to a external MySQL database, performing a complex SQL query involving joins, aggregation, and sorting. The project is implemented in Python, with RDS datbase connection and CI/CD setup for testing and validation.

## Project Structure

- **.devcontainer/**: Configuration for the development container.
- **Makefile**: Provides commands for setup, formatting, linting, testing, and running SQL queries:
  - `make install`: Installs dependencies.
  - `make format`: Formats Python files.
  - `make lint`: Lints Python files.
  - `make test`: Runs tests.
  - `make all`: Runs all tasks (install, format, lint, and test).
  - `make transform`: Transforms data and stores it in the `drink.db` database.
  - `make query3`: Run the complex SQL query

- **.github/workflows/ci.yml**: CI/CD pipeline configuration.
- **main.py**: Python script to handle data transformation, and database queries.
- **README.md**: Setup, usage instructions, and project description.

## Complex SQL Query

```sql
SELECT 
    tc.country,
    tc.total_beer_servings,
    u.age_group,
    u.alcohol_use,
    u.alcohol_frequency
FROM 
    (SELECT country, SUM(beer_servings) AS total_beer_servings 
     FROM drink 
     GROUP BY country 
     ORDER BY total_beer_servings DESC 
     LIMIT 5) AS tc
JOIN 
    drug_use u 
ON 
    u.alcohol_use = (SELECT MAX(alcohol_use) FROM drug_use) 
ORDER BY 
    tc.total_beer_servings DESC, u.alcohol_use DESC;
```

### Explanation
This query is designed to find the top 5 countries with the highest total beer servings and the corresponding age group with the maximum alcohol use.

- First, the subquery calculates the total beer servings per country by summing `beer_servings` from the `drink` table and selecting only the top 5 countries with the highest values, sorted in descending order.
- Next, this subquery result (`tc`) is joined with the `drug_use` table, where the age group is selected based on the highest recorded alcohol use (`MAX(alcohol_use)`).
- The final output shows the country, total beer servings, age group with the maximum alcohol use, and the median alcohol usage frequency for each of these countries. The results are sorted by the total beer servings in descending order, followed by the alcohol use in descending order.

### Expected Result

| Country         | Total Beer Servings | Age Group | Alcohol Use (%) | Alcohol Frequency |
|-----------------|--------------------|-----------|-----------------|-------------------|
| Namibia         | 376                | 22-23     | 84.2            | 52.0              |
| Czech Republic  | 361                | 22-23     | 84.2            | 52.0              |
| Gabon           | 347                | 22-23     | 84.2            | 52.0              |
| Germany         | 346                | 22-23     | 84.2            | 52.0              |
| Lithuania       | 343                | 22-23     | 84.2            | 52.0              |

This result shows the top 5 countries with the highest beer servings and the age group `22-23`, which has the maximum alcohol use across all countries at `84.2%`, with a median usage frequency of `52` times in the last 12 months.



## Setup

1. **Clone the repository**:

    ```bash
    git clone https://github.com/nogibjj/Allen_Wang_miniproj_6.git
    cd Allen_Wang_miniproj_6
    ```

2. **Install dependencies**:

    ```bash
    make install
    ```

3. **Format code**:

    ```bash
    make format
    ```

4. **Lint code**:

    ```bash
    make lint
    ```

5. **Test code**:

    ```bash
    make test
    ```
