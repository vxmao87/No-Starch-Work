create database eventful;

use eventful;

create table event_message
	(
	message  varchar(100)
	);
    
-- 13-1
-- Create an event that runs every minute for 5 minutes
-- that sends a message to your timestamp table
DROP EVENT IF EXISTS e_write_timestamp;

DELIMITER //

CREATE EVENT e_write_timestamp
	ON SCHEDULE EVERY 1 MINUTE
    STARTS current_timestamp()
    ENDS current_timestamp() + INTERVAL 5 MINUTE
    DO BEGIN
		INSERT INTO event_message (message)
        VALUES (current_timestamp());
	END //
    
DELIMITER ;

-- 13-2
-- Check for errors in the event you just made
SELECT * 
FROM performance_schema.error_log
WHERE data like '%e_write_timestamp%';

-- 13-3
-- Use the command below to check that your event is working as it should
SELECT * FROM event_message;

DROP EVENT IF EXISTS e_write_timestamp;