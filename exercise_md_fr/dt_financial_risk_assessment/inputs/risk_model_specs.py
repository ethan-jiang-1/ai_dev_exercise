"""
FinSecure Risk Assessment Platform - Risk Models Specification
=============================================================

This module defines the specifications for the machine learning models used
in the FinSecure Risk Assessment Platform. It includes feature definitions,
model architectures, hyperparameters, and evaluation criteria.

Models included:
- Transaction Fraud Detection
- Credit Risk Assessment
- Anti-Money Laundering Detection
- Behavioral Analysis

Author: FinSecure Data Science Team
Last Updated: 2025-01-20
Version: 0.8.5
"""

import enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union


class ModelType(enum.Enum):
    """Enumeration of supported model types"""
    CLASSIFICATION = "classification"
    REGRESSION = "regression"
    ANOMALY_DETECTION = "anomaly_detection"
    CLUSTERING = "clustering"
    TIME_SERIES = "time_series"


class DataType(enum.Enum):
    """Enumeration of supported data types"""
    NUMERIC = "numeric"
    CATEGORICAL = "categorical"
    TEXT = "text"
    DATETIME = "datetime"
    GEOSPATIAL = "geospatial"
    GRAPH = "graph"


@dataclass
class FeatureDefinition:
    """Definition of a feature used in risk models"""
    name: str
    data_type: DataType
    description: str
    required: bool = True
    nullable: bool = False
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    categorical_values: Optional[List[str]] = None
    derived: bool = False
    derivation_formula: Optional[str] = None
    pii: bool = False  # Personally Identifiable Information
    transformer: Optional[str] = None
    importance_score: Optional[float] = None  # Feature importance (0-1)


@dataclass
class ModelPerformance:
    """Performance metrics for a risk model"""
    accuracy: Optional[float] = None
    precision: Optional[float] = None
    recall: Optional[float] = None
    f1_score: Optional[float] = None
    auc_roc: Optional[float] = None
    false_positive_rate: Optional[float] = None
    false_negative_rate: Optional[float] = None
    mean_squared_error: Optional[float] = None
    mean_absolute_error: Optional[float] = None
    r_squared: Optional[float] = None
    latency_ms: Optional[int] = None  # Inference latency in milliseconds
    throughput_tps: Optional[int] = None  # Transactions per second


@dataclass
class ModelSpecification:
    """Complete specification for a risk model"""
    model_id: str
    name: str
    version: str
    description: str
    model_type: ModelType
    features: List[FeatureDefinition]
    target_variable: str
    architecture: str  # e.g., "RandomForest", "LSTM", "XGBoost"
    hyperparameters: Dict[str, Union[str, int, float, bool]]
    training_dataset: str  # Reference to training dataset
    validation_dataset: str  # Reference to validation dataset
    performance: ModelPerformance
    explainability_method: str  # e.g., "SHAP", "LIME", "IntegratedGradients"
    regulatory_approval: bool = False
    approval_date: Optional[str] = None
    refresh_frequency: str = "quarterly"  # How often model should be retrained
    dependencies: List[str] = None  # Other models this model depends on


# ===========================================================================
# Fraud Detection Model
# ===========================================================================

FRAUD_DETECTION_FEATURES = [
    FeatureDefinition(
        name="transaction_amount",
        data_type=DataType.NUMERIC,
        description="Amount of the transaction in base currency",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.85
    ),
    FeatureDefinition(
        name="merchant_category_code",
        data_type=DataType.CATEGORICAL,
        description="MCC indicating the merchant type",
        categorical_values=["1000", "1001", ..., "9999"],
        transformer="OneHotEncoder",
        importance_score=0.72
    ),
    FeatureDefinition(
        name="transaction_country",
        data_type=DataType.CATEGORICAL,
        description="Country where transaction occurred",
        transformer="OneHotEncoder",
        importance_score=0.68
    ),
    FeatureDefinition(
        name="transaction_time",
        data_type=DataType.DATETIME,
        description="Timestamp of the transaction",
        transformer="TimeFeatureExtractor",
        importance_score=0.65
    ),
    FeatureDefinition(
        name="cardholder_country",
        data_type=DataType.CATEGORICAL,
        description="Country of the cardholder",
        transformer="OneHotEncoder",
        importance_score=0.63
    ),
    FeatureDefinition(
        name="transaction_ip",
        data_type=DataType.TEXT,
        description="IP address used for transaction",
        transformer="IPAddressTransformer",
        importance_score=0.61
    ),
    FeatureDefinition(
        name="distance_from_home",
        data_type=DataType.NUMERIC,
        description="Distance from cardholder's home address in km",
        derived=True,
        derivation_formula="haversine(home_location, transaction_location)",
        transformer="StandardScaler",
        importance_score=0.78
    ),
    FeatureDefinition(
        name="time_since_last_transaction",
        data_type=DataType.NUMERIC,
        description="Minutes since the last transaction by this cardholder",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.75
    ),
    FeatureDefinition(
        name="transaction_velocity_1h",
        data_type=DataType.NUMERIC,
        description="Number of transactions in the last hour",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.82
    ),
    FeatureDefinition(
        name="average_transaction_amount_30d",
        data_type=DataType.NUMERIC,
        description="Average transaction amount over the last 30 days",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.70
    ),
    FeatureDefinition(
        name="transaction_amount_vs_average",
        data_type=DataType.NUMERIC,
        description="Ratio of current transaction to average amount",
        derived=True,
        derivation_formula="transaction_amount / average_transaction_amount_30d",
        transformer="StandardScaler",
        importance_score=0.79
    ),
    FeatureDefinition(
        name="merchant_risk_score",
        data_type=DataType.NUMERIC,
        description="Risk score associated with the merchant",
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.73
    ),
    FeatureDefinition(
        name="card_present",
        data_type=DataType.CATEGORICAL,
        description="Whether the card was physically present",
        categorical_values=["true", "false"],
        transformer="OneHotEncoder",
        importance_score=0.69
    ),
    FeatureDefinition(
        name="device_fingerprint",
        data_type=DataType.TEXT,
        description="Fingerprint of the device used",
        required=False,
        transformer="HashingEncoder",
        importance_score=0.58
    ),
    FeatureDefinition(
        name="previously_seen_device",
        data_type=DataType.CATEGORICAL,
        description="Whether this device has been seen before",
        categorical_values=["true", "false"],
        derived=True,
        transformer="OneHotEncoder",
        importance_score=0.67
    ),
]

FRAUD_DETECTION_MODEL = ModelSpecification(
    model_id="FDM-001",
    name="Transaction Fraud Detection Model",
    version="1.2.3",
    description="Real-time fraud detection model for payment card transactions",
    model_type=ModelType.CLASSIFICATION,
    features=FRAUD_DETECTION_FEATURES,
    target_variable="is_fraudulent",
    architecture="XGBoost",
    hyperparameters={
        "max_depth": 8,
        "learning_rate": 0.1,
        "n_estimators": 200,
        "objective": "binary:logistic",
        "subsample": 0.8,
        "colsample_bytree": 0.8,
        "scale_pos_weight": 10,  # Adjusted for imbalanced data
        "eval_metric": "auc",
        "early_stopping_rounds": 10
    },
    training_dataset="fraud_detection_training_2024Q4",
    validation_dataset="fraud_detection_validation_2024Q4",
    performance=ModelPerformance(
        accuracy=0.996,
        precision=0.923,
        recall=0.875,
        f1_score=0.898,
        auc_roc=0.985,
        false_positive_rate=0.0008,
        false_negative_rate=0.042,
        latency_ms=12,
        throughput_tps=10000
    ),
    explainability_method="SHAP",
    regulatory_approval=True,
    approval_date="2024-12-15",
    refresh_frequency="monthly",
    dependencies=[]
)


# ===========================================================================
# Credit Risk Assessment Model
# ===========================================================================

CREDIT_RISK_FEATURES = [
    FeatureDefinition(
        name="credit_score",
        data_type=DataType.NUMERIC,
        description="Credit bureau score (FICO/VantageScore)",
        min_value=300,
        max_value=850,
        transformer="StandardScaler",
        importance_score=0.91
    ),
    FeatureDefinition(
        name="debt_to_income_ratio",
        data_type=DataType.NUMERIC,
        description="Total debt payments divided by income",
        min_value=0.0,
        max_value=None,
        transformer="StandardScaler",
        importance_score=0.85
    ),
    FeatureDefinition(
        name="income",
        data_type=DataType.NUMERIC,
        description="Annual income in base currency",
        min_value=0.0,
        transformer="LogTransformer",
        importance_score=0.78,
        pii=True
    ),
    FeatureDefinition(
        name="employment_length",
        data_type=DataType.NUMERIC,
        description="Years at current employer",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.65
    ),
    FeatureDefinition(
        name="housing_status",
        data_type=DataType.CATEGORICAL,
        description="Housing ownership status",
        categorical_values=["own", "mortgage", "rent", "other"],
        transformer="OneHotEncoder",
        importance_score=0.62
    ),
    FeatureDefinition(
        name="loan_amount",
        data_type=DataType.NUMERIC,
        description="Requested loan amount",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.75
    ),
    FeatureDefinition(
        name="loan_term",
        data_type=DataType.NUMERIC,
        description="Loan term in months",
        transformer="StandardScaler",
        importance_score=0.58
    ),
    FeatureDefinition(
        name="loan_purpose",
        data_type=DataType.CATEGORICAL,
        description="Purpose of the loan",
        categorical_values=["home", "auto", "education", "medical", "debt_consolidation", "business", "other"],
        transformer="OneHotEncoder",
        importance_score=0.66
    ),
    FeatureDefinition(
        name="number_of_open_accounts",
        data_type=DataType.NUMERIC,
        description="Number of open credit accounts",
        min_value=0,
        transformer="StandardScaler",
        importance_score=0.61
    ),
    FeatureDefinition(
        name="credit_utilization",
        data_type=DataType.NUMERIC,
        description="Percentage of available credit used",
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.82
    ),
    FeatureDefinition(
        name="delinquencies_last_2_years",
        data_type=DataType.NUMERIC,
        description="Number of delinquencies in the last 2 years",
        min_value=0,
        transformer="StandardScaler",
        importance_score=0.83
    ),
    FeatureDefinition(
        name="months_since_last_delinquency",
        data_type=DataType.NUMERIC,
        description="Months since most recent delinquency",
        nullable=True,
        transformer="CustomDelinquencyTransformer",
        importance_score=0.70
    ),
    FeatureDefinition(
        name="public_records",
        data_type=DataType.NUMERIC,
        description="Number of derogatory public records",
        min_value=0,
        transformer="StandardScaler",
        importance_score=0.73
    ),
    FeatureDefinition(
        name="application_age",
        data_type=DataType.NUMERIC,
        description="Years since first credit application",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.59
    ),
    FeatureDefinition(
        name="address_stability",
        data_type=DataType.NUMERIC,
        description="Years at current address",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.55
    ),
]

CREDIT_RISK_MODEL = ModelSpecification(
    model_id="CRM-001",
    name="Credit Risk Assessment Model",
    version="2.1.0",
    description="Credit risk model for loan approval decisions",
    model_type=ModelType.CLASSIFICATION,
    features=CREDIT_RISK_FEATURES,
    target_variable="default_risk",
    architecture="LightGBM",
    hyperparameters={
        "objective": "binary",
        "boosting_type": "gbdt",
        "num_leaves": 31,
        "learning_rate": 0.05,
        "feature_fraction": 0.9,
        "bagging_fraction": 0.8,
        "bagging_freq": 5,
        "max_depth": -1,
        "min_data_in_leaf": 20,
        "num_iterations": 500
    },
    training_dataset="credit_risk_training_2024Q4",
    validation_dataset="credit_risk_validation_2024Q4",
    performance=ModelPerformance(
        accuracy=0.938,
        precision=0.856,
        recall=0.823,
        f1_score=0.839,
        auc_roc=0.942,
        false_positive_rate=0.032,
        false_negative_rate=0.047,
        latency_ms=25,
        throughput_tps=5000
    ),
    explainability_method="SHAP",
    regulatory_approval=True,
    approval_date="2024-11-30",
    refresh_frequency="quarterly",
    dependencies=[]
)


# ===========================================================================
# Anti-Money Laundering (AML) Detection Model
# ===========================================================================

AML_DETECTION_FEATURES = [
    FeatureDefinition(
        name="transaction_amount",
        data_type=DataType.NUMERIC,
        description="Amount of the transaction in base currency",
        min_value=0.0,
        transformer="StandardScaler",
        importance_score=0.79
    ),
    FeatureDefinition(
        name="transaction_type",
        data_type=DataType.CATEGORICAL,
        description="Type of transaction",
        categorical_values=["deposit", "withdrawal", "transfer", "payment", "forex", "other"],
        transformer="OneHotEncoder",
        importance_score=0.75
    ),
    FeatureDefinition(
        name="customer_risk_score",
        data_type=DataType.NUMERIC,
        description="Risk score associated with the customer",
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.87
    ),
    FeatureDefinition(
        name="sender_account_age",
        data_type=DataType.NUMERIC,
        description="Age of sender account in days",
        min_value=0,
        transformer="LogTransformer",
        importance_score=0.68
    ),
    FeatureDefinition(
        name="receiver_account_age",
        data_type=DataType.NUMERIC,
        description="Age of receiver account in days",
        min_value=0,
        transformer="LogTransformer",
        importance_score=0.63
    ),
    FeatureDefinition(
        name="sender_country",
        data_type=DataType.CATEGORICAL,
        description="Country of the sender",
        transformer="OneHotEncoder",
        importance_score=0.71
    ),
    FeatureDefinition(
        name="receiver_country",
        data_type=DataType.CATEGORICAL,
        description="Country of the receiver",
        transformer="OneHotEncoder",
        importance_score=0.73
    ),
    FeatureDefinition(
        name="high_risk_country_involved",
        data_type=DataType.CATEGORICAL,
        description="Whether transaction involves a high-risk country",
        categorical_values=["true", "false"],
        derived=True,
        transformer="OneHotEncoder",
        importance_score=0.85
    ),
    FeatureDefinition(
        name="transaction_frequency_1d",
        data_type=DataType.NUMERIC,
        description="Number of transactions in last day",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.82
    ),
    FeatureDefinition(
        name="transaction_frequency_7d",
        data_type=DataType.NUMERIC,
        description="Number of transactions in last 7 days",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.76
    ),
    FeatureDefinition(
        name="transaction_frequency_30d",
        data_type=DataType.NUMERIC,
        description="Number of transactions in last 30 days",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.70
    ),
    FeatureDefinition(
        name="transaction_amount_7d",
        data_type=DataType.NUMERIC,
        description="Total transaction amount in last 7 days",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.78
    ),
    FeatureDefinition(
        name="transaction_amount_30d",
        data_type=DataType.NUMERIC,
        description="Total transaction amount in last 30 days",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.75
    ),
    FeatureDefinition(
        name="transaction_pattern_score",
        data_type=DataType.NUMERIC,
        description="Score representing unusual patterns",
        derived=True,
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.88
    ),
    FeatureDefinition(
        name="structuring_indicator",
        data_type=DataType.NUMERIC,
        description="Indicator of potential structuring behavior",
        derived=True,
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.90
    ),
    FeatureDefinition(
        name="network_risk_score",
        data_type=DataType.NUMERIC,
        description="Risk score based on transaction network analysis",
        derived=True,
        min_value=0.0,
        max_value=1.0,
        transformer="StandardScaler",
        importance_score=0.84
    ),
]

AML_DETECTION_MODEL = ModelSpecification(
    model_id="AML-001",
    name="Anti-Money Laundering Detection Model",
    version="1.5.2",
    description="Model to detect potential money laundering activities",
    model_type=ModelType.CLASSIFICATION,
    features=AML_DETECTION_FEATURES,
    target_variable="aml_risk",
    architecture="Neural Network",
    hyperparameters={
        "hidden_layers": [128, 64, 32],
        "activation": "relu",
        "dropout": 0.3,
        "learning_rate": 0.001,
        "batch_size": 256,
        "epochs": 100,
        "early_stopping": True,
        "patience": 10,
        "class_weight": {"0": 1, "1": 15}  # Heavily weighted for rare positives
    },
    training_dataset="aml_detection_training_2025Q1",
    validation_dataset="aml_detection_validation_2025Q1",
    performance=ModelPerformance(
        accuracy=0.991,
        precision=0.821,
        recall=0.773,
        f1_score=0.796,
        auc_roc=0.952,
        false_positive_rate=0.0012,
        false_negative_rate=0.039,
        latency_ms=35,
        throughput_tps=3000
    ),
    explainability_method="IntegratedGradients",
    regulatory_approval=True,
    approval_date="2025-01-10",
    refresh_frequency="monthly",
    dependencies=[]
)


# ===========================================================================
# Behavioral Analysis Model
# ===========================================================================

BEHAVIORAL_ANALYSIS_FEATURES = [
    FeatureDefinition(
        name="user_id",
        data_type=DataType.TEXT,
        description="Unique identifier for the user",
        transformer="EntityEmbedding",
        importance_score=None  # Not directly used for prediction
    ),
    FeatureDefinition(
        name="session_features",
        data_type=DataType.TEXT,
        description="JSON of session-related features",
        transformer="SessionFeatureExtractor",
        importance_score=0.75
    ),
    FeatureDefinition(
        name="device_type",
        data_type=DataType.CATEGORICAL,
        description="Type of device used",
        categorical_values=["mobile", "tablet", "desktop", "other"],
        transformer="OneHotEncoder",
        importance_score=0.58
    ),
    FeatureDefinition(
        name="browser_fingerprint",
        data_type=DataType.TEXT,
        description="Browser fingerprint hash",
        transformer="HashingEncoder",
        importance_score=0.62
    ),
    FeatureDefinition(
        name="ip_address",
        data_type=DataType.TEXT,
        description="IP address of the user",
        transformer="IPAddressTransformer",
        importance_score=0.67
    ),
    FeatureDefinition(
        name="login_time",
        data_type=DataType.DATETIME,
        description="Time of login",
        transformer="TimeFeatureExtractor",
        importance_score=0.72
    ),
    FeatureDefinition(
        name="typical_login_times",
        data_type=DataType.TEXT,
        description="JSON array of typical login times",
        derived=True,
        transformer="TimePatternExtractor",
        importance_score=0.79
    ),
    FeatureDefinition(
        name="login_location",
        data_type=DataType.GEOSPATIAL,
        description="Geolocation of login",
        transformer="GeoFeatureExtractor",
        importance_score=0.74
    ),
    FeatureDefinition(
        name="location_variance",
        data_type=DataType.NUMERIC,
        description="Variance from typical locations",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.81
    ),
    FeatureDefinition(
        name="typing_pattern",
        data_type=DataType.TEXT,
        description="Typing rhythm pattern",
        required=False,
        transformer="BiometricFeatureExtractor",
        importance_score=0.63
    ),
    FeatureDefinition(
        name="navigation_pattern",
        data_type=DataType.TEXT,
        description="User navigation pattern",
        transformer="SequenceEncoder",
        importance_score=0.70
    ),
    FeatureDefinition(
        name="transaction_pattern",
        data_type=DataType.TEXT,
        description="Transaction behavior pattern",
        transformer="SequenceEncoder",
        importance_score=0.78
    ),
    FeatureDefinition(
        name="behavioral_biometrics",
        data_type=DataType.TEXT,
        description="JSON of behavioral biometric data",
        required=False,
        transformer="BiometricFeatureExtractor",
        importance_score=0.65
    ),
    FeatureDefinition(
        name="activity_speed",
        data_type=DataType.NUMERIC,
        description="Speed of user activity (actions per minute)",
        derived=True,
        transformer="StandardScaler",
        importance_score=0.69
    ),
    FeatureDefinition(
        name="session_duration",
        data_type=DataType.NUMERIC,
        description="Duration of user session in seconds",
        transformer="StandardScaler",
        importance_score=0.60
    ),
]

BEHAVIORAL_ANALYSIS_MODEL = ModelSpecification(
    model_id="BAM-001",
    name="User Behavioral Analysis Model",
    version="1.1.0",
    description="Model to detect anomalous user behavior indicating potential account takeover",
    model_type=ModelType.ANOMALY_DETECTION,
    features=BEHAVIORAL_ANALYSIS_FEATURES,
    target_variable="anomaly_score",
    architecture="Isolation Forest + LSTM",
    hyperparameters={
        "isolation_forest": {
            "n_estimators": 100,
            "contamination": "auto",
            "max_samples": "auto"
        },
        "lstm": {
            "units": 64,
            "recurrent_dropout": 0.2,
            "return_sequences": True,
            "activation": "tanh"
        },
        "ensemble_weights": {
            "isolation_forest": 0.5,
            "lstm": 0.5
        }
    },
    training_dataset="behavioral_analysis_training_2024Q4",
    validation_dataset="behavioral_analysis_validation_2024Q4",
    performance=ModelPerformance(
        accuracy=0.972,
        precision=0.843,
        recall=0.815,
        f1_score=0.829,
        auc_roc=0.934,
        false_positive_rate=0.012,
        false_negative_rate=0.031,
        latency_ms=48,
        throughput_tps=2500
    ),
    explainability_method="LIME",
    regulatory_approval=True,
    approval_date="2024-12-20",
    refresh_frequency="monthly",
    dependencies=[]
)


# Model registry
RISK_MODELS = {
    "fraud_detection": FRAUD_DETECTION_MODEL,
    "credit_risk": CREDIT_RISK_MODEL,
    "aml_detection": AML_DETECTION_MODEL,
    "behavioral_analysis": BEHAVIORAL_ANALYSIS_MODEL
}


def get_model_spec(model_name: str) -> ModelSpecification:
    """
    Retrieve the specification for a named model.
    
    Args:
        model_name: Name of the model to retrieve
        
    Returns:
        ModelSpecification for the requested model
        
    Raises:
        KeyError: If the requested model does not exist
    """
    if model_name not in RISK_MODELS:
        raise KeyError(f"Model '{model_name}' not found in risk model registry")
    return RISK_MODELS[model_name]


def get_model_performance_summary() -> Dict[str, Dict]:
    """
    Get a summary of performance metrics for all models.
    
    Returns:
        Dictionary of model performance summaries
    """
    return {
        name: {
            "auc_roc": model.performance.auc_roc,
            "f1_score": model.performance.f1_score,
            "latency_ms": model.performance.latency_ms,
            "throughput_tps": model.performance.throughput_tps,
            "approval_date": model.approval_date
        }
        for name, model in RISK_MODELS.items()
    }


# Example usage
if __name__ == "__main__":
    # Print summary of all models
    print("Risk Model Performance Summary:")
    for model_name, metrics in get_model_performance_summary().items():
        print(f"\n{model_name.upper()}:")
        for metric, value in metrics.items():
            print(f"  - {metric}: {value}")
    
    # Get complete spec for a specific model
    fraud_model = get_model_spec("fraud_detection")
    print(f"\nDetails for {fraud_model.name} (v{fraud_model.version}):")
    print(f"  - Architecture: {fraud_model.architecture}")
    print(f"  - Features: {len(fraud_model.features)}")
    print(f"  - Top 5 features by importance:")
    
    top_features = sorted(
        [f for f in fraud_model.features if f.importance_score is not None],
        key=lambda x: x.importance_score or 0,
        reverse=True
    )[:5]
    
    for feature in top_features:
        print(f"    * {feature.name} (importance: {feature.importance_score:.3f})") 