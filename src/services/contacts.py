from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactRepository
from src.schemas import ContactModel


class ContactService:
    def __init__(self, db: AsyncSession):
        self.repository = ContactRepository(db)

    async def create_contact(self, body: ContactModel):
        if await self.repository.is_contact_exists(body.email, body.phone_number):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Contact with '{body.email}' email or '{body.phone_number}' phone number already exists."
            )
        return await self.repository.create_contact(body)

    async def get_contacts(self, first_name: str, last_name: str, email: str, skip: int, limit: int):
        return await self.repository.get_contacts(first_name, last_name, email, skip, limit)

    async def get_contact(self, contact_id: int):
        return await self.repository.get_contact_by_id(contact_id)

    async def update_contact(self, contact_id: int, body: ContactModel):
        return await self.repository.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int):
        return await self.repository.remove_contact(contact_id)

    async def get_upcoming_birthdays(self, days: int):
        return await self.repository.get_upcoming_birthdays(days)