SELECT * FROM wall.users;
SELECT * FROM wall.messages;
SELECT * FROM wall.comments;
INSERT INTO messages (user_id, message, created_at, updated_at) VALUES (17, 'Argggg', NOW(), NOW());
INSERT INTO `wall`.`messages` (`id`, `user_id`, `message`, `created_at`, `updated_at`) VALUES (8, 18, 'fjdkals', '2018-01-14 16:25:51', '2018-01-14 16:25:51');

Select users.id As User_id, first_name, last_name, email, messages.id As message_id, message, messages.created_at As message_created_at, comments.id As comment_id, comment, comments.created_at As comment_created_at 
From users 
Join messages On users.id = messages.user_id
Left Join comments On messages.id = comments.message_id
Order By user_id Desc, message_id, comment_id;

# messages w/o date_function in methond returnDashboard()
Select concat(users.id,'-', messages.id) As message_key, email, group_concat(' ' ,message, ' - ') AS messages, concat(first_name, ' ', last_name, ' - ',  date_format(messages.created_at,'%M %e, %Y')) As label, date_format(messages.created_at,'%B%d%Y-%H%M%S') As new_id 
From users 
Join messages On users.id = messages.user_id 
Group By users.id, concat(day(messages.created_at), month(messages.created_at), year(messages.created_at)) 
Order By users.id Desc, messages.id, messages.created_at;

# comments w/o date_functions in methond returnDashboard()
Select comments.message_id As message_id, group_concat(' ' ,comment,' - ') As comments, concat(first_name, ' ', last_name, ' - ',  date_format(comments.created_at,'%M %e, %Y')) As label 
From messages 
Join comments On message_id = comments.message_id 
Join users on comments.user_id = users.id 
where comments.message_id=messages.id
Group By comments.user_id, comments.user_id, concat(day(messages.created_at), month(messages.created_at), year(messages.created_at)) 
Order By comments.user_id Desc, messages.id, comments.id;
