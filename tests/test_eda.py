"""Tests for EDA functionality."""

import pytest
import pandas as pd
import numpy as np


def test_headline_length_calculation():
    """Test headline length calculation."""
    headlines = pd.Series(['"Short"', '"A longer headline here"'])
    lengths = headlines.str.len()
    assert lengths.iloc[0] == 7
    assert lengths.iloc[1] == 23


def test_date_range_calculation():
    """Test date range calculation."""
    dates = pd.date_range('"2024-01-01"', periods=5, freq='"D"')
    assert len(dates) == 5
    assert dates[0] < dates[-1]


def test_sample_dataframe():
    """Test sample DataFrame creation."""
    sample_df = pd.DataFrame({
        '"headline"': ['"Test 1"', '"Test 2"'],
        '"publisher"': ['"Pub A"', '"Pub B"'],
        '"date"': ['"2024-01-01"', '"2024-01-02"']
    })
    assert len(sample_df) == 2
    assert '"headline"' in sample_df.columns


def test_percentage_calculation():
    """Test percentage calculations."""
    total = 1000
    part = 250
    percentage = (part / total) * 100
    assert percentage == 25.0


def test_moving_average():
    """Test simple moving average calculation."""
    data = pd.Series([10, 20, 30, 40, 50])
    ma = data.rolling(window=3).mean()
    assert pd.isna(ma.iloc[0])
    assert pd.isna(ma.iloc[1])
    assert ma.iloc[2] == 20.0
