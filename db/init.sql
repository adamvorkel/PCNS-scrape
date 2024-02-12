CREATE TABLE scrape_results (
    id INTEGER PRIMARY KEY,
    success BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE practices (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    registered_date DATE,
    status VARCHAR(50),
    dispensing_license BOOLEAN
);

INSERT INTO scrape_results (id, success) VALUES (1000001, TRUE);
INSERT INTO scrape_results (id, success) VALUES (1000011, TRUE);
INSERT INTO scrape_results (id, success) VALUES (1000081, TRUE);