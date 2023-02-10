from loguru import logger
from sqlalchemy.exc import IntegrityError

from app.schemas.users import CreateUser
from .base_crud import BaseCRUD
from ..models.users import User


class UserDAL(BaseCRUD):
    async def create_user(self, new_user: CreateUser):
        user = User(
            user_id=new_user.user_id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            username=new_user.username,
            is_admin=new_user.is_admin
        )
        try:
            self.session.add(user)
            await self.session.commit()
        except IntegrityError as ex:
            logger.warning(ex)
