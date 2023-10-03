CREATE TABLE abn_user (
  id serial PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  registered_at TIMESTAMP
);

CREATE TABLE host (
  id serial PRIMARY KEY,
  abn_user_id int NOT NULL,
  FOREIGN KEY (abn_user_id) REFERENCES abn_user (id)
);

CREATE TABLE guest (
  id serial PRIMARY KEY,
  abn_user_id int NOT NULL,
  FOREIGN KEY (abn_user_id) REFERENCES abn_user (id)
);

CREATE TABLE room (
  id serial PRIMARY KEY,
  host_id int NOT NULL,
  price_night float NOT NULL,
  amount_of_residents int NOT NULL,
  n_of_rooms int NOT NULL,
  n_of_beds int NOT NULL,
  air_conditioning bool NOT NULL,
  refrigerator bool NOT NULL,
  kitchen bool NOT NULL,
  FOREIGN KEY (host_id) REFERENCES host (id)
);

CREATE TABLE reservation (
  id serial PRIMARY KEY,
  reservation_time timestamp NOT NULL,
  check_in date NOT NULL,
  check_out date NOT NULL,
  room_id int NOT NULL,
  guest_id int,
  FOREIGN KEY (room_id) REFERENCES room (id),
  FOREIGN KEY (guest_id) REFERENCES guest (id)
);

CREATE TABLE availability (
  room_id int NOT NULL,
  checking_date date NOT NULL,
  available bool NOT NULL,
  FOREIGN KEY (room_id) REFERENCES room (id)
);

CREATE TABLE payment (
  id serial PRIMARY KEY,
  paid_at timestamp NOT NULL,
  room_id int NOT NULL,
  guest_id int NOT NULL,
  payment_method varchar(50) NOT NULL,
  FOREIGN KEY (room_id) REFERENCES room (id),
  FOREIGN KEY (guest_id) REFERENCES guest (id)
);

CREATE TABLE review (
  id serial PRIMARY KEY,
  review_date timestamp NOT NULL,
  room_id int NOT NULL,
  guest_id int NOT NULL,
  review varchar NOT NULL,
  rate int NOT NULL
  FOREIGN KEY (room_id) REFERENCES room (id),
  FOREIGN KEY (guest_id) REFERENCES guest (id)
);


INSERT INTO abn_user (username, email, phone) VALUES
                                                    ('Nick', 'nick23@mail', '12345678901'),
                                                    ('Paola', 'paolasmith@mail', '34567892034'),
                                                    ('Bob', 'bobbybrown@mail', '480985123545'),
                                                    ('Max', 'max@mail', '345766885543'),
                                                    ('Katrin', 'kate@mail', '23785490345');

INSERT INTO host (abn_user_id) VALUES (1), (2), (3);

INSERT INTO guest (abn_user_id) VALUES (3), (4), (5);

INSERT INTO room (host_id,
                price_night,
                amount_of_residents,
                n_of_rooms,
                n_of_beds,
                air_conditioning,
                refrigerator,
                kitchen) VALUES
                (1, 75.5, 2, 1, 2, TRUE, TRUE, TRUE),
                (2, 90.0, 3, 2, 2, TRUE, TRUE, TRUE),
                (3, 80, 2, 2, 2, FALSE, TRUE, TRUE);

INSERT INTO reservation (
                reservation_time,
                check_in,
                check_out,
                room_id,
                guest_id
                ) VALUES
                (NOW(), '2023-10-10', '2023-10-15', 1, 1),
                (NOW(), '2023-10-10', '2023-10-15', 2, 2),
                (NOW(), '2023-10-16', '2023-10-25', 1, 2);

INSERT INTO availability (
    room_id,
    checking_date,
    available) VALUES
    (1, '2023-10-25', FALSE),
    (1, '2023-10-26', TRUE),
    (1, '2023-10-27', TRUE);

INSERT INTO payment (
    paid_at,
    room_id,
    guest_id,
    payment_method
    ) VALUES
    (NOW(), 1, 1, 'card'),
    (NOW(), 2, 2, 'cash'),
    (NOW(), 1, 2, 'cash');

INSERT INTO review (
    review_date,
    room_id,
    guest_id,
    review,
    rate) VALUES
    (NOW(), 1, 1, 'great', 5),
    (NOW(), 2, 2, 'Everything is ok', 5),
    (NOW(), 1, 2, 'recommend this room', 5);

 
SELECT u.username, u.id, COUNT(r.guest_id) AS biggest_traveler
FROM reservation r
LEFT JOIN guest g ON g.id = r.guest_id
LEFT JOIN abn_user u ON u.id = g.abn_user_id
GROUP BY u.username, u.id
ORDER BY biggest_traveler DESC
LIMIT 1;

