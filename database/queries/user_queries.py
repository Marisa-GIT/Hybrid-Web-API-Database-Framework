

GET_ALL_USERS = """
SELECT *
FROM users;
"""

GET_USER_BY_ID = """
SELECT *
FROM users
WHERE id = %s;
"""

USER_EXISTS = """
SELECT COUNT(*) 
AS count 
FROM users 
WHERE id = %s;"""