INSERT INTO `friendship`.`users` (`id`, `first_name`, `last_name`, `created_at`, `updated_at`) VALUES ('4', 'Diana', 'Smith', now(), Now());
SELECT * FROM friendship.users;
INSERT INTO `friendship`.`friendships` (`id`, `user_id`, `friend_id`, `created_at`, `updated_at`) VALUES (6, 3, 1, now(), Now());
SELECT * FROM friendship.friendships;
SELECT users.first_name as first_name, users.last_name as last_name, user2.first_name as friend_first_name, user2.last_name as friend_last_name FROM friendship.users
LEFT JOIN friendships ON users.id = friendships.user_id 
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
ORDER BY friendships.id;
