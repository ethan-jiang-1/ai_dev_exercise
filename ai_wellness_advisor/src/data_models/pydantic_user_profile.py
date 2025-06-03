# Pydantic model for User Profile
# Path: /Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/src/data_models/pydantic_user_profile.py

from typing import List, Optional, Literal
from uuid import UUID, uuid4
from datetime import datetime, timezone # Ensure timezone is imported
from pydantic import BaseModel, Field, validator, root_validator, field_validator # Import field_validator for Pydantic V2 style

class UserProfile(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    age: int = Field(..., gt=0, lt=120, description="User's age in years")
    gender: Literal['male', 'female', 'other'] = Field(..., description="User's gender")
    height_cm: float = Field(..., gt=0, description="User's height in centimeters")
    weight_kg: float = Field(..., gt=0, description="User's weight in kilograms")
    health_goals: List[str] = Field(..., min_length=1, description="List of user's health goals") # Pydantic V1: min_items, V2: min_length
    allergies: Optional[List[str]] = Field(default=None, description="List of user's allergies")
    medical_conditions: Optional[List[str]] = Field(default=None, description="List of user's medical conditions")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of profile creation")
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), description="Timestamp of last profile update")

    @root_validator(skip_on_failure=True)
    def _update_timestamp_on_any_validation(cls, values):
        """Sets updated_at to current UTC time whenever the model is validated."""
        # This ensures updated_at reflects the time of the last validation/modification.
        # This root_validator runs after default_factories and individual field validators.
        values['updated_at'] = datetime.now(timezone.utc)
        return values

    # Pydantic V2 uses model_config as a dictionary, not a class
    # For Pydantic V1, Config class is used.
    class Config:
        validate_assignment = True # Allows re-validation when an attribute is assigned a new value.
        json_encoders = {
            UUID: lambda v: str(v), # Serializes UUID to string for JSON output.
            datetime: lambda v: v.isoformat() # Serializes datetime to ISO 8601 string.
        }
        # Pydantic V1 anystr_strip_whitespace = True # Strips whitespace from strings (char, byte, str)
        # This is no longer a config option in Pydantic V2. Whitespace stripping needs to be handled by @validator or @field_validator.

        # Example for Pydantic V2 model_config (if migrating):
        # model_config = {
        #     "validate_assignment": True,
        #     "json_encoders": {
        #         UUID: lambda v: str(v),
        #         datetime: lambda v: v.isoformat()
        #     },
        #     "title": "User Health Profile",
        #     "json_schema_extra": {
        #         "examples": [
        #             {
        #                 "user_id": "123e4567-e89b-12d3-a456-426614174000",
        #                 "age": 30,
        #                 "gender": "female",
        #                 "height_cm": 165.5,
        #                 "weight_kg": 60.2,
        #                 "health_goals": ["Lose weight", "Improve stamina"],
        #                 "allergies": ["Pollen", "Dust mites"],
        #                 "medical_conditions": ["Asthma"],
        #                 # created_at and updated_at are usually set by the model
        #             }
        #         ]
        #     }
        # }

# Example Usage (can be run directly for quick testing):
if __name__ == "__main__":
    try:
        # Valid data
        user_data = {
            "age": 30,
            "gender": "female",
            "height_cm": 165.5,
            "weight_kg": 60.2,
            "health_goals": ["Lose weight", "Improve stamina"],
            "allergies": ["Pollen", "Dust mites"],
            "medical_conditions": ["Asthma"]
        }
        profile1 = UserProfile(**user_data)
        print("Profile 1 (valid):")
        print(profile1.model_dump_json(indent=2))
        print(f"User ID: {profile1.user_id} (Type: {type(profile1.user_id)})")
        print(f"Created At: {profile1.created_at} (Type: {type(profile1.created_at)})")
        print(f"Updated At: {profile1.updated_at} (Type: {type(profile1.updated_at)})")

        # Minimal valid data (optional fields will be None)
        minimal_data = {
            "age": 25,
            "gender": "male",
            "height_cm": 180.0,
            "weight_kg": 75.0,
            "health_goals": ["Build muscle"]
        }
        profile2 = UserProfile(**minimal_data)
        print("\nProfile 2 (minimal valid):")
        print(profile2.model_dump_json(indent=2))
        assert profile2.allergies is None
        assert profile2.medical_conditions is None

        # Test assignment validation
        print("\nTesting assignment validation:")
        old_updated_at = profile1.updated_at
        import time
        time.sleep(0.01) # Ensure time moves forward for updated_at check
        profile1.age = 31 # This should trigger validation and update 'updated_at'
        print(f"Age updated to: {profile1.age}")
        print(f"Updated At after age modification: {profile1.updated_at}")
        assert profile1.updated_at > old_updated_at

        # Invalid data examples
        print("\nTesting invalid data:")
        invalid_data_age = minimal_data.copy()
        invalid_data_age["age"] = -5
        try:
            UserProfile(**invalid_data_age)
        except ValidationError as e:
            print(f"Validation error for age < 0: Caught successfully!\n{e}")

        invalid_data_gender = minimal_data.copy()
        invalid_data_gender["gender"] = "other_gender"
        try:
            UserProfile(**invalid_data_gender)
        except ValidationError as e:
            print(f"Validation error for invalid gender: Caught successfully!\n{e}")

        invalid_data_goals = minimal_data.copy()
        invalid_data_goals["health_goals"] = [] # Empty list, should fail min_length=1
        try:
            UserProfile(**invalid_data_goals)
        except ValidationError as e:
            print(f"Validation error for empty health_goals: Caught successfully!\n{e}")

    except ValidationError as e:
        print("An unexpected validation error occurred during example usage:")
        print(e)