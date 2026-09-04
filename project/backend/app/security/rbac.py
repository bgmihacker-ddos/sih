from fastapi import Depends, HTTPException, status
from app.models.user import Role
from app.api.auth import get_current_user

class RoleChecker:
    def __init__(self, allowed_roles: list[Role]):
        self.allowed_roles = allowed_roles

    def __call__(self, user: dict = Depends(get_current_user)):
        # user here would need to be the full user object loaded from DB
        # To keep it simple for now, assume user includes role in token payload
        if user.get("role") not in [role.value for role in self.allowed_roles]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return user
