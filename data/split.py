import numpy as np
from sklearn.model_selection import train_test_split
from typing import Tuple

def split_dataset(
    images: np.ndarray,
    labels: np.ndarray,
    train_size: float = 0.8,
    val_size: float = 0.1,
    test_size: float = 0.1,
    random_state: int = 42
) -> Tuple[np.ndarray, ...]:

    assert train_size + val_size + test_size == 1.0, \
        "train, val and test sizes must add up to 1.0"

    # Train vs Temp (Val + Test)
    X_train, X_temp, y_train, y_temp = train_test_split(
        images,
        labels,
        test_size=(1.0 - train_size),
        random_state=random_state
    )

    # adjust val & test
    val_ratio = val_size / (val_size + test_size)

    # Validation vs Test
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp,
        y_temp,
        test_size=(1.0 - val_ratio),
        random_state=random_state
    )

    return X_train, X_val, X_test, y_train, y_val, y_test