from dao.base_dao import BaseDAO
from dao.models.user import User


class UserDAO(BaseDAO[User]):
    __model__ = User

    def get_one_by_email(self, email: str) -> User | None:
        users = self.session.query(User) \
            .filter(User.email == email).all()
        # тк электронная почта уникальна то дб только 1 пользователь
        if len(users) == 1:
            return users[0]
        else:
            return None
