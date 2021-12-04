CREATE TABLE frame
(
    id           SERIAL NOT NULL PRIMARY KEY,
    protocol     varchar(10),
    s_mac        macaddr,
    d_mac        macaddr,
    s_ip         inet,
    d_ip         inet,
    s_port       int,
    d_port       int,
    data         text,
    arrival_time timestamp
);

CREATE TABLE ip_location
(
    id           SERIAL NOT NULL PRIMARY KEY,
    ip           inet,
    country      varchar(100),
    country_code varchar(5),
    latitude     real,
    longitude    real,
    region       varchar(100),
    city         varchar(100)
);

ALTER TABLE frame
    ADD FOREIGN KEY (s_ip) REFERENCES ip_location (id);

ALTER TABLE frame
    ADD FOREIGN KEY (d_ip) REFERENCES ip_location (id);
