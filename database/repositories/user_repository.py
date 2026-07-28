from database.queries.user_queries import GET_ALL_USERS, GET_USER_BY_ID, USER_EXISTS
from database.base_repository import BaseRepository
from core.logger import Logger

logger = Logger.get_logger(__name__)

class UserRepository(BaseRepository):

    def get_all_users(self):
        cursor = self.get_cursor()

        try:
            
            cursor.execute(GET_ALL_USERS)

            
            users = cursor.fetchall()

            logger.info(f"{len(users)} users were obtained from the database.")

            
            return users
        except Exception as e:
            logger.error(f"Error executing GET_ALL_USERS: {e}")
            raise


    def get_user_by_id(self, user_id):
        cursor = self.get_cursor()

        try:
            
            cursor.execute(GET_USER_BY_ID, (user_id,))
            user = cursor.fetchone()  
            
            if user:
                self.logger.info(f"User with ID {user_id} found in DB.")
            else:
                self.logger.warning(f"User with ID {user_id} not found in DB.")
                
            return user
        except Exception as e:
            logger.error(f"Error executing GET_USER_BY_ID for ID {user_id}: {e}")
            raise
     

    def user_exists(self, user_id):
        cursor = self.get_cursor()

        try:
            cursor.execute(USER_EXISTS, (user_id,))
            result = cursor.fetchone()
            exists = result["count"] > 0 if result else False

            logger.info(f"¿Does the user with ID exist {user_id}?: {exists}")
            return exists

        except Exception as e:
            logger.error(f"Error executing EXISTS_USER_BY_ID for ID {user_id}: {e}")
            raise

       