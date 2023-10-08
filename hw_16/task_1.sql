CREATE TABLE abn_user (
  id serial PRIMARY KEY,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(50) NOT NULL,
  phone VARCHAR(20) NOT NULL,
  registered_at TIMESTAMP,
  user_type VARCHAR(5) NOT NULL
);


CREATE TABLE room (
  id serial PRIMARY KEY,
  abn_user_id int NOT NULL,
  price_night float NOT NULL,
  amount_of_residents int NOT NULL,
  n_of_rooms int NOT NULL,
  n_of_beds int NOT NULL,
  air_conditioning bool NOT NULL,
  refrigerator bool NOT NULL,
  kitchen bool NOT NULL,
  FOREIGN KEY (abn_user_id) REFERENCES abn_user (id)
);

CREATE TABLE reservation (
  id serial PRIMARY KEY,
  reservation_time timestamp NOT NULL,
  check_in date NOT NULL,
  check_out date NOT NULL,
  room_id int NOT NULL,
  abn_user_id int,
  FOREIGN KEY (room_id) REFERENCES room (id),
  FOREIGN KEY (abn_user_id) REFERENCES abn_user (id)
);

CREATE TABLE payment (
  id serial PRIMARY KEY,
  paid_at timestamp NOT NULL,
  reservation_id int NOT NULL,
  payment_method varchar(50) NOT NULL,
  amount decimal(7,2) NOT NULL,
  FOREIGN KEY (reservation_id) REFERENCES reservation (id)
);

CREATE TABLE review (
  id serial PRIMARY KEY,
  review_date timestamp NOT NULL,
  reservation_id int NOT NULL,
  review varchar NOT NULL,
  rate int NOT NULL,
  FOREIGN KEY (reservation_id) REFERENCES reservation (id)
);


INSERT INTO abn_user (username, email, phone, user_type) VALUES
                                                    ('Nick', 'nick23@mail', '12345678901', 'host'),
                                                    ('Paola', 'paolasmith@mail', '34567892034', 'host'),
                                                    ('Bob', 'bobbybrown@mail', '480985123545', 'host'),
                                                    ('Max', 'max@mail', '345766885543', 'guest'),
                                                    ('Katrin', 'kate@mail', '23785490345', 'guest');

INSERT INTO room (abn_user_id,
                price_night,
                amount_of_residents,
                n_of_rooms,
                n_of_beds,
                air_conditioning,
                refrigerator,
                kitchen
                ) 
                VALUES
                (1, 75.5, 2, 1, 2, TRUE, TRUE, TRUE),
                (2, 90.0, 3, 2, 2, TRUE, TRUE, TRUE),
                (3, 80, 2, 2, 2, FALSE, TRUE, TRUE);

INSERT INTO reservation (
                reservation_time,
                check_in,
                check_out,
                room_id,
                abn_user_id
                ) 
                VALUES
                (NOW(), '2023-10-10', '2023-10-15', 1, 3),
                (NOW(), '2023-10-10', '2023-10-15', 2, 4),
                (NOW(), '2023-10-16', '2023-10-25', 1, 4);

INSERT INTO payment (
    paid_at,
    reservation_id,
    payment_method,
    amount
    ) 
    VALUES
    (NOW(), 1, 'card', 453.00),
    (NOW(), 2, 'card', 540.00),
    (NOW(), 1, 'cash', 900.00);

INSERT INTO review (
    review_date,
    reservation_id,
    review,
    rate
    ) 
    VALUES
    (NOW(), 1, 'great', 5),
    (NOW(), 2, 'Everything is ok', 5),
    (NOW(), 3, 'recommend this room', 5);
 
SELECT u.username, u.id, COUNT(r.abn_user_id) AS biggest_traveler
FROM reservation r
LEFT JOIN abn_user u ON u.id = r.abn_user_id
GROUP BY u.username, u.id
ORDER BY biggest_traveler DESC
LIMIT 1;

