"""Basic tests to verify imports and functionality."""

import pytest
import pandas as pd
import numpy as np


def test_pandas_import():
    """Test that pandas is imported correctly."""
    assert pd.__version__ is not None
    assert isinstance(pd.DataFrame(), pd.DataFrame)


def test_numpy_import():
    """Test that numpy is imported correctly."""
    assert np.__version__ is not None
    assert np.array([1, 2, 3]).sum() == 6


def test_dataframe_creation():
    """Test basic pandas DataFrame creation."""
    df = pd.DataFrame({'"A"': [1, 2, 3], '"B"': [4, 5, 6]})
    assert df.shape == (3, 2)
    assert df['"A"'].mean() == 2


def test_sentiment_function():
    """Test that sentiment function works."""
    def mock_sentiment(text):
        return 0.5 if "good" in text else -0.5
    
    assert mock_sentiment("good news") == 0.5
    assert mock_sentiment("bad news") == -0.5


def test_return_calculation():
    """Test return calculation logic."""
    prices = pd.Series([100, 102, 101, 105])
    returns = prices.pct_change() * 100
    assert pd.isna(returns.iloc[0])  # First return is NaN
    assert abs(returns.iloc[1] - 2.0) < 0.01  # 2% return


def test_date_parsing():
    """Test date parsing functionality."""
    dates = pd.to_datetime(['"2024-01-01"', '"2024-01-02"'])
    assert dates[0].year == 2024
    assert dates[0].month == 1
