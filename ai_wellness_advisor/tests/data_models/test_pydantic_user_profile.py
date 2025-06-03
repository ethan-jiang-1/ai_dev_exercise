# Test cases for Pydantic UserProfile model
# Path: /Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/tests/data_models/test_pydantic_user_profile.py

import pytest
from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from uuid import UUID
import time

from ai_wellness_advisor.src.data_models.pydantic_user_profile import UserProfile

# --- Test Data ---
VALID_USER_PROFILE_DATA = {
    "age": 30,
    "gender": "female",
    "height_cm": 165.5,
    "weight_kg": 60.2,
    "health_goals": ["Lose weight", "Improve stamina"],
    "allergies": ["Pollen", "Dust mites"],
    "medical_conditions": ["Asthma"]
}

MINIMAL_USER_PROFILE_DATA = {
    "age": 25,
    "gender": "male",
    "height_cm": 180.0,
    "weight_kg": 75.0,
    "health_goals": ["Build muscle"]
}

# --- Test Cases ---

@pytest.fixture
def user_profile_model():
    """Fixture to provide the UserProfile model."""
    return UserProfile


class TestUserProfileCreation:
    def test_create_user_profile_success(self, user_profile_model):
        """Test successful creation of UserProfile with all valid data."""


        profile = user_profile_model(**VALID_USER_PROFILE_DATA)
        assert profile.age == VALID_USER_PROFILE_DATA["age"]
        assert profile.gender == VALID_USER_PROFILE_DATA["gender"]
        assert profile.height_cm == VALID_USER_PROFILE_DATA["height_cm"]
        assert profile.weight_kg == VALID_USER_PROFILE_DATA["weight_kg"]
        assert profile.health_goals == VALID_USER_PROFILE_DATA["health_goals"]
        assert profile.allergies == VALID_USER_PROFILE_DATA["allergies"]
        assert profile.medical_conditions == VALID_USER_PROFILE_DATA["medical_conditions"]

        assert isinstance(profile.user_id, UUID)
        assert isinstance(profile.created_at, datetime)
        assert isinstance(profile.updated_at, datetime)
        # Check if timestamps are recent (e.g., within the last few seconds)
        assert datetime.now(timezone.utc) - profile.created_at < timedelta(seconds=5)
        assert datetime.now(timezone.utc) - profile.updated_at < timedelta(seconds=5)

    def test_create_user_profile_minimal_data_success(self, user_profile_model):
        """Test successful creation with only minimal required data."""


        profile = user_profile_model(**MINIMAL_USER_PROFILE_DATA)
        assert profile.age == MINIMAL_USER_PROFILE_DATA["age"]
        assert profile.gender == MINIMAL_USER_PROFILE_DATA["gender"]
        assert profile.health_goals == MINIMAL_USER_PROFILE_DATA["health_goals"]
        assert profile.allergies is None # Default
        assert profile.medical_conditions is None # Default

    def test_optional_fields_default_to_none(self, user_profile_model):
        """Test that optional fields default to None if not provided."""

        
        profile = user_profile_model(**MINIMAL_USER_PROFILE_DATA)
        assert profile.allergies is None
        assert profile.medical_conditions is None

    def test_optional_fields_can_be_set_to_empty_list(self, user_profile_model):
        """Test that optional fields can be explicitly set to an empty list."""


        data = {**MINIMAL_USER_PROFILE_DATA, "allergies": [], "medical_conditions": []}
        profile = user_profile_model(**data)
        assert profile.allergies == []
        assert profile.medical_conditions == []

class TestUserProfileValidations:
    @pytest.mark.parametrize("invalid_age", [-1, 0, 120, 150, "invalid"])
    def test_age_invalid(self, user_profile_model, invalid_age):
        """Test age validation for out-of-range and invalid type."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "age": invalid_age}
            user_profile_model(**data)

    @pytest.mark.parametrize("invalid_gender", ["unknown", "malee", 123])
    def test_gender_invalid(self, user_profile_model, invalid_gender):
        """Test gender validation for invalid values."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "gender": invalid_gender}
            user_profile_model(**data)

    @pytest.mark.parametrize("invalid_height", [-10.0, 0.0, "invalid"])
    def test_height_cm_invalid(self, user_profile_model, invalid_height):
        """Test height_cm validation for non-positive values and invalid type."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "height_cm": invalid_height}
            user_profile_model(**data)

    @pytest.mark.parametrize("invalid_weight", [-5.0, 0.0, "invalid"])
    def test_weight_kg_invalid(self, user_profile_model, invalid_weight):
        """Test weight_kg validation for non-positive values and invalid type."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "weight_kg": invalid_weight}
            user_profile_model(**data)

    def test_health_goals_empty_list_invalid(self, user_profile_model):
        """Test health_goals validation for empty list (should fail due to min_length=1)."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "health_goals": []}
            user_profile_model(**data)

    @pytest.mark.parametrize("invalid_goals", ["not a list", [1, 2, 3]])
    def test_health_goals_invalid_type(self, user_profile_model, invalid_goals):
        """Test health_goals validation for invalid type or item type."""


        with pytest.raises(ValidationError):
            data = {**MINIMAL_USER_PROFILE_DATA, "health_goals": invalid_goals}
            user_profile_model(**data)

    @pytest.mark.parametrize("missing_field", ["age", "gender", "height_cm", "weight_kg", "health_goals"])
    def test_missing_required_fields(self, user_profile_model, missing_field):
        """Test that missing required fields raise ValidationError."""


        data = MINIMAL_USER_PROFILE_DATA.copy()
        del data[missing_field]
        with pytest.raises(ValidationError):
            user_profile_model(**data)

class TestUserProfileTimestamps:
    def test_timestamps_auto_generated_and_type(self, user_profile_model):
        """Test created_at and updated_at are auto-generated and are datetime objects."""


        profile = user_profile_model(**MINIMAL_USER_PROFILE_DATA)
        assert isinstance(profile.created_at, datetime)
        assert isinstance(profile.updated_at, datetime)
        assert profile.created_at.tzinfo is not None and profile.created_at.tzinfo == timezone.utc
        assert profile.updated_at.tzinfo is not None and profile.updated_at.tzinfo == timezone.utc

    def test_updated_at_updates_on_modification(self, user_profile_model):
        """Test that updated_at timestamp updates when the model is modified (if validate_assignment=True)."""


        profile = user_profile_model(**MINIMAL_USER_PROFILE_DATA)
        initial_updated_at = profile.updated_at
        time.sleep(0.1) # Wait a bit longer to ensure timestamp difference
        
        profile.age = profile.age + 1 # Trigger re-validation if validate_assignment is True
        
        assert profile.updated_at > initial_updated_at

class TestUserProfileSerialization:
    def test_user_profile_serialization_to_json(self, user_profile_model):
        """Test serialization to JSON string."""

        
        import json
        profile = user_profile_model(**VALID_USER_PROFILE_DATA)
        json_output = profile.model_dump_json()
        data_from_json = json.loads(json_output)

        assert str(profile.user_id) == data_from_json["user_id"]
        assert profile.age == data_from_json["age"]
        assert profile.gender == data_from_json["gender"]
        assert profile.created_at.isoformat().startswith(data_from_json["created_at"])