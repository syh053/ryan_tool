from sqlalchemy.orm import DeclarativeBase

class BaseModel(DeclarativeBase):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        server_default=text("gen_random_uuid()"),
        primary_key=True,
        comment="ID"
    )