docker run -it --rm --link pcns-scrape-db-1:pcns-scrape-db-1 --network pcns-scrape_default postgres psql -h pcns-scrape-db-1 -U postgres