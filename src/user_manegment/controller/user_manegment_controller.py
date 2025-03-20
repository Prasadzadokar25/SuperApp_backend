from src.user_manegment.dao.get_user_info_dao import UserManegmentDao


class UserManegmentController :
    
    @staticmethod
    def getUserInfo(user_id): 
        return UserManegmentDao().getUserInfo(user_id)

  