from pydantic import BaseModel, ConfigDict


class FinnyBase(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        from_attributes=True,
        validate_assignment=True,
        arbitrary_types_allowed=True,
        extra="forbid",
    )
