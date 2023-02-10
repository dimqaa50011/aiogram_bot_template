from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.users import CreateUser
from ..models.users import User
from .base_crud import BaseCRUD


class UserDAL(BaseCRUD):
    
    async def create_user(self, new_user: CreateUser):
        user = User(
            user_id=new_user.user_id,
            first_name=new_user.first_name,
            last_name=new_user.last_name,
            username=new_user.username,
            is_admin=new_user.is_admin
        )
        self.session.add(user)
        await self.session.commit()
        return user
