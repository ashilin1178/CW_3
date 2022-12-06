from dao.model.user import User

class UserDAO():
    def __init__(self, session):
        self.session = session


    def get_all_users(self):
        return self.session.query(User).all()


    def get_user_by_id(self, uid):
        return self.session.query(User).filter(User.id == uid).one()

    def get_user_by_email(self, email):
        return self.session.query(User).filter(User.email == email).one()


    def create_user(self, **kwargs):
        try:
            self.session.add(User(**kwargs))
            self.session.commit()
            return True
        except Exception as e:
            print(e)
            self.session.rollback()
            return False


    def edit_user_by_id(self, uid, **user_data):
        try:
            self.session.query(User).filter(User.id == uid).update(user_data)
            self.session.commit()
            return True
        except Exception as e:
            print('ошибка DAO.edit_user_by_id', e)
            self.session.rollback()
            return False


    def delete_user_by_id(self, uid):
        try:
            self.session.query(User).filter(User.id == uid).delete()
            self.session.commit()
            return True

        except Exception as e:
            print(e)
            self.session.rollback()
            return False
