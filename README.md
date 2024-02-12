# PCNS-scrape
## Intro
This project scrapes the pcns.co.za sites /Search/Verify endpoint for practice details.
## Scrape site analysis
The pcns site search page allows a user to fill in a search number, which is submitted in a form (along with a __RequestVerificationToken) via a post request to the `/Search/Verify` endpoint.
The endpoint doesn't seem to care about the token validity though - making scraping easier.
The server is also very slow (roughly 7.5 seconds RTT - tested empirically), so using a mock server with configurable latency seems practical.
## Services
The project is made up of several services

### Mock server (mock-server)
This is a simple FastAPI server (previously bun & express) used for dev and testing to avoid bombarding the actual site server and adjusting latency for dev.
It accepts a post request with a `SearchValue` form field just like the site (it ignores `__RequestVerificationToken` though, as the site doesn't seem to care about this field either). 
The mock server can return a hit (valid number search with data) or miss (invalid number, no data) response, which is the same HTML structure as the pcns site returns in each case. A hit returns some dummy data (in the same kind of fomat as the pcns site ofcourse), and a miss returns the no results page, both embed the `SearchValue` in the html - this is important as on hits we extract the data, including the id, and we want it to be unique (although we do already have the number we searched at hand, this ensures the data extracted from the page could be directly inserted in the db without violating the unique constraint on the primary key `id` column).  
The server implements three routes:
- / - returns hits for even `SearchValue`, misses for odd
- /hit - returns a hit
- /miss - returns a miss


### Postgres Database (db)
A database server with a `PCNS` database to store scraped results.
The database runs a SQL script to create the schema on container creation.
The database includes two tables
- practices - for storing the details associated with a valid practice number 
- scrape_results - for storing the result of a scrape for a particular practice number

### Scraper (scraper)
A python script that spawns multiple processes and divides the practice number range between them.
Each worker process gets the practice search page html, extracts data if available, parses and validates it, and saves it to the db 
(for every number in it's assigned range that is not already in the scrape_results table)

*Note: services with dependencies use relevant health checks to ensure race-conditions are avoided.*

**Optimisations**
- multi-process
- async (requests, db interactions)
- chunking of scrapes 
- db scrape_results log table to avoid re-scraping if scraper is started again   

## Instructions
The project is dockerized so to run, adjust env options in compose file:

WORKERS - number of worker processes
CHUNK_SIZE - number of scrapes to process in one go
START_ID - start of pcns number range
END_ID - end of pcns number range

RES_LATENCY (in dev file) - mock server response latency

Run relevant docker-compose.yml file:
**Real server**

```bash
docker compose up --build
```

**Mock server**
```bash
docker compose -f docker-compose.dev.yml up --build
```


