
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# 1. Load dataset
data = pd.read_csv("Crop_recommendation.csv")

print("Dataset loaded successfully!")
print("Dataset shape:", data.shape)

# 2. Separate input and output
X = data.drop("label", axis=1)
y = data["label"]

# 3. Encode crop names
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 4. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

# 5. Create model
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42
)

# 6. Train model
print("Training started...")
model.fit(X_train, y_train)

# 7. Check accuracy
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("Training completed!")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# 8. Save model
joblib.dump(model, "crop_model.pkl")
joblib.dump(encoder, "label_encoder.pkl")
joblib.dump(list(X.columns), "feature_names.pkl")

print("All model files saved successfully!")
