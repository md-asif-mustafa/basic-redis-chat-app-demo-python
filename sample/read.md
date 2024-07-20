docker compose exec redis redis-cli -a secret
127.0.0.1:6379> keys user:*
127.0.0.1:6379> 

Manually Set User Data:

Use hset to manually add "Fisa" to Redis:

bash

127.0.0.1:6379> hset user:5 username Fisa
127.0.0.1:6379> hset user:5 password <hashed_password>


