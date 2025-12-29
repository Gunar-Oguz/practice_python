-- @block
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

-- @block
SELECT
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table,
    ccu.column_name AS foreign_column
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu
    ON tc.constraint_name = ccu.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
ORDER BY tc.table_name;

-- @block
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public'
ORDER BY table_name, ordinal_position;


-- @block
SELECT *
FROM film_actor;

-- @block
SELECT *
FROM actor
LIMIT 10;

-- @block
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public';

-- @block
SELECT *
FROM address
LIMIT 10;


-- @block
SELECT *
FROM rental
LIMIT 10;

-- @block
SELECT *
FROM staff
LIMIT 10;

-- @block
SELECT 
    c.first_name,
    c.last_name,
    f.title,
    r.rental_date
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
LIMIT 10;

-- @block
SELECT first_name, last_name
FROM actor
WHERE first_name = 'PENELOPE';

-- @block
SELECT *
FROM film
WHERE rental_rate > 2.99
LIMIT 10;

-- @block
SELECT title, length
FROM film
WHERE length >= 120
LIMIT 10;


-- @block
SELECT title, rental_rate, length
FROM film
WHERE rental_rate > 2.99 AND length >= 120;


-- @block
SELECT first_name, last_name
FROM actor
WHERE first_name = 'PENELOPE' OR first_name = 'NICK';

-- @block
SELECT title, rating
FROM film
WHERE NOT rating = 'G'


-- @block
SELECT title, length
FROM film
WHERE length BETWEEN 90 AND 120;

-- @block
SELECT first_name, last_name
FROM actor
WHERE last_name LIKE '%S%S%'

-- @block
SELECT DISTINCT rating
FROM film;

-- @block
SELECT DISTINCT rating, rental_rate
FROM film;


-- @block
SELECT title, length, rating
FROM film
WHERE rating = 'R'
ORDER BY length ASC
LIMIT 10;

-- @block
SELECT COUNT(*)
FROM film;


-- @block
SELECT COUNT(*)
FROM actor;


-- @block
SELECT COUNT(*)
FROM customer;


-- @block
SELECT COUNT(*)
FROM customer
WHERE activebool = true;


-- @block
SELECT original_language_id
FROM film
WHERE original_language_id is not NULL;

-- @block
SELECT 
    COUNT(*) AS total_films,
    AVG(rental_rate) AS avg_price,
    MIN(rental_rate) AS cheapest,
    MAX(rental_rate) AS most_expensive
FROM film;

-- @block
SELECT release_year, COUNT(release_year) AS total
FROM film
GROUP BY release_year
ORDER BY release_year;

-- @block
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
ORDER BY film_count DESC;

-- @block
SELECT customer_id, SUM(amount) AS total_spent
FROM payment
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;


-- @block
-- WHERE: filters rows BEFORE grouping
SELECT rating, COUNT(*) AS film_count
FROM film
WHERE length > 100
GROUP BY rating;

-- HAVING: filters groups AFTER counting
-- @block
SELECT rating, COUNT(*) AS film_count
FROM film
GROUP BY rating
HAVING COUNT(*) > 190;


-- @block
SELECT rating, COUNT(*)
FROM film
GROUP BY rating;

-- @block
SELECT *
FROM rental;


-- @block
SELECT customer_id, COUNT(*) AS rental_count
FROM rental
GROUP BY customer_id
HAVING COUNT(*) > 30;

-- @block
SELECT staff_id, SUM(amount) 
FROM payment
GROUP BY staff_id
HAVING SUM(amount) > 30000;

-- @block
SELECT *
FROM film;


-- @block
SELECT rating, AVG(replacement_cost) AS avg_replacement_cost
FROM film
GROUP BY rating
HAVING AVG(replacement_cost) > 20
ORDER BY avg_replacement_cost DESC;

-- @block
SELECT *
FROM rental;

-- @block
SELECT inventory_id, COUNT(inventory_id) AS total_inventory_id
FROM rental
GROUP BY inventory_id
HAVING COUNT(inventory_id) > 4
ORDER BY total_inventory_id DESC
LIMIT 10;


-- @block
SELECT inventory_id, COUNT(*) AS rental_count
FROM rental
GROUP BY inventory_id
ORDER BY rental_count DESC
LIMIT 10;


-- @block
SELECT *
FROM customer;

-- @block
SELECT store_id, COUNT(customer_id) AS total_customer_by_store
FROM customer
GROUP BY store_id;

-- @block
SELECT *
FROM payment;

-- @block
SELECT customer_id, AVG(amount) AS average_amount
FROM payment
WHERE amount > 5 
GROUP BY customer_id
HAVING AVG(amount) > 7;


-- @block
SELECT *
FROM film;

-- @block
SELECT rental_duration, COUNT(*)
FROM film
WHERE rental_rate > 2.99
GROUP BY rental_duration
HAVING COUNT(*) > 100;


-- @block
SELECT *
FROM customer;

-- @block
SELECT EXTRACT(YEAR FROM create_date) as year, COUNT(*) AS total_customers
FROM customer
GROUP BY EXTRACT(YEAR FROM create_date)
HAVING COUNT(*) > 100;

-- @block
SELECT *
FROM film;


-- @block
SELECT rating, MIN(length) AS shorter, MAX(length) AS longer
FROM film
WHERE replacement_cost BETWEEN 10 AND 25
GROUP BY rating
HAVING MAX(length) > 180
ORDER BY MAX(length) DESC;

-- @block
SELECT c.first_name, c.last_name, r.rental_date
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
LIMIT 10;

-- @block
SELECT c.first_name, c.last_name, f.title, r.rental_date
FROM rental r
JOIN customer c ON r.customer_id = c.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id
LIMIT 10;

-- @block
SELECT *
FROM film;

-- @block
SELECT *
FROM language;

-- @block
SELECT f.title, l.name
FROM film AS f
JOIN language AS l
ON f.language_id = l.language_id
LIMIT 10;

-- @block
SELECT *
FROM customer; 

-- @block
SELECT *
FROM address;


-- @block
SELECT c.first_name, c.last_name, a.address
FROM customer AS c
JOIN address AS a
ON c.address_id = a.address_id;

-- @block
SELECT *
FROM customer; 

-- @block
SELECT *
FROM address;

-- @block
SELECT *
FROM city;

-- @block 
SELECT *
FROM country;


-- @block
SELECT c.first_name, c.last_name, ci.city, co.country
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city ci ON a.city_id = ci.city_id
JOIN country co ON ci.country_id = co.country_id
LIMIT 10;


-- @block
SELECT *
FROM rental
LIMIT 3;

-- @block
SELECT *
FROM staff
LIMIT 3;

-- @block
SELECT *
FROM customer
LIMIT 3;


-- @block
SELECT tc.table_name, kcu.column_name, ccu.table_name AS foreign_table
FROM information_schema.table_constraints tc
JOIN information_schema.key_column_usage kcu ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage ccu ON tc.constraint_name = ccu.constraint_name
WHERE tc.constraint_type = 'FOREIGN KEY'
AND tc.table_name IN ('rental', 'staff', 'customer');


-- @block
SELECT s.first_name, c.first_name, rental_date
FROM staff as s
JOIN rental as r 
ON s.staff_id = r.staff_id
JOIN customer as c
ON c.customer_id = r.customer_id;


-- @block
SELECT *
FROM film
LIMIT 2;


-- @block
SELECT *
FROM film_category
LIMIT 2;

-- @block
SELECT *
FROM category
LIMIT 2;


-- @block
SELECT f.title, l.name AS language
FROM film f
LEFT JOIN language l ON f.original_language_id = l.language_id
LIMIT 10;

-- @block
SELECT c.first_name, p.amount
FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id;

-- @block
SELECT c.first_name, c.last_name, p.amount
FROM customer c
LEFT JOIN payment p ON c.customer_id = p.customer_id
WHERE p.amount IS NULL;

-- @block
SELECT title, rental_rate
FROM film
WHERE rental_rate > 2.98;

-- @block
SELECT AVG(rental_rate)
FROM film;

-- @block
SELECT title, rental_rate
FROM film
WHERE rental_rate > (
    SELECT AVG(rental_rate)
    FROM film
)



-- @block
SELECT *
FROM customer;
-- @block
SELECT *
FROM rental;


-- @block
SELECT c.first_name, c.last_name, c.customer_id
FROM customer AS c
WHERE c.customer_id in (
    SELECT rental.customer_id FROM rental);


-- @block
S










