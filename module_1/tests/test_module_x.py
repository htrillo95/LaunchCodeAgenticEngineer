import pytest

from module_x import (
    calculate_discount,
    classify_priority,
    is_valid_project_code,
    normalize_name,
    summarize_order,
)


class TestNormalizeName:
    def test_collapses_internal_whitespace(self):
        assert normalize_name("john   doe") == "John Doe"

    def test_strips_leading_and_trailing_whitespace(self):
        assert normalize_name("  jane smith  ") == "Jane Smith"

    def test_title_cases_each_word(self):
        assert normalize_name("MARY ANN jones") == "Mary Ann Jones"

    def test_single_word(self):
        assert normalize_name("cher") == "Cher"

    def test_raises_type_error_for_non_string(self):
        with pytest.raises(TypeError):
            normalize_name(123)

    def test_raises_value_error_for_empty_string(self):
        with pytest.raises(ValueError):
            normalize_name("")

    def test_raises_value_error_for_whitespace_only(self):
        with pytest.raises(ValueError):
            normalize_name("   ")


class TestCalculateDiscount:
    def test_standard_tier_no_discount(self):
        assert calculate_discount(100.0, "standard") == 100.0

    def test_silver_tier_discount(self):
        assert calculate_discount(100.0, "silver") == 95.0

    def test_gold_tier_discount(self):
        assert calculate_discount(100.0, "gold") == 90.0

    def test_platinum_tier_discount(self):
        assert calculate_discount(100.0, "platinum") == 85.0

    def test_tier_is_case_insensitive_and_trimmed(self):
        assert calculate_discount(100.0, "  GOLD  ") == 90.0

    def test_rounds_to_two_decimal_places(self):
        assert calculate_discount(19.99, "silver") == 18.99

    def test_zero_price(self):
        assert calculate_discount(0.0, "gold") == 0.0

    def test_raises_value_error_for_negative_price(self):
        with pytest.raises(ValueError):
            calculate_discount(-10.0, "gold")

    def test_raises_value_error_for_unknown_tier(self):
        with pytest.raises(ValueError):
            calculate_discount(100.0, "diamond")


class TestClassifyPriority:
    def test_zero_is_low(self):
        assert classify_priority(0) == "low"

    def test_boundary_below_medium_is_low(self):
        assert classify_priority(39) == "low"

    def test_boundary_medium(self):
        assert classify_priority(40) == "medium"

    def test_boundary_below_high_is_medium(self):
        assert classify_priority(69) == "medium"

    def test_boundary_high(self):
        assert classify_priority(70) == "high"

    def test_boundary_below_urgent_is_high(self):
        assert classify_priority(89) == "high"

    def test_boundary_urgent(self):
        assert classify_priority(90) == "urgent"

    def test_max_score_is_urgent(self):
        assert classify_priority(100) == "urgent"

    def test_raises_type_error_for_non_int(self):
        with pytest.raises(TypeError):
            classify_priority(85.5)

    def test_raises_type_error_for_bool_is_allowed_as_int(self):
        # bool is a subclass of int in Python, so this should not raise TypeError
        assert classify_priority(True) == "low"

    def test_raises_value_error_below_range(self):
        with pytest.raises(ValueError):
            classify_priority(-1)

    def test_raises_value_error_above_range(self):
        with pytest.raises(ValueError):
            classify_priority(101)


class TestSummarizeOrder:
    def test_empty_list_returns_zeros(self):
        assert summarize_order([]) == {"item_count": 0, "subtotal": 0.0}

    def test_single_item(self):
        result = summarize_order([{"quantity": 2, "unit_price": 5.0}])
        assert result == {"item_count": 2, "subtotal": 10.0}

    def test_multiple_items(self):
        items = [
            {"quantity": 2, "unit_price": 5.0},
            {"quantity": 1, "unit_price": 3.5},
        ]
        result = summarize_order(items)
        assert result == {"item_count": 3, "subtotal": 13.5}

    def test_rounds_subtotal_to_two_decimal_places(self):
        items = [{"quantity": 3, "unit_price": 0.1}]
        result = summarize_order(items)
        assert result["subtotal"] == 0.3

    def test_missing_quantity_defaults_to_zero(self):
        result = summarize_order([{"unit_price": 10.0}])
        assert result == {"item_count": 0, "subtotal": 0.0}

    def test_missing_unit_price_defaults_to_zero(self):
        result = summarize_order([{"quantity": 5}])
        assert result == {"item_count": 5, "subtotal": 0.0}

    def test_raises_value_error_for_negative_quantity(self):
        with pytest.raises(ValueError):
            summarize_order([{"quantity": -1, "unit_price": 5.0}])

    def test_raises_value_error_for_non_int_quantity(self):
        with pytest.raises(ValueError):
            summarize_order([{"quantity": 1.5, "unit_price": 5.0}])

    def test_raises_value_error_for_negative_unit_price(self):
        with pytest.raises(ValueError):
            summarize_order([{"quantity": 1, "unit_price": -5.0}])

    def test_raises_value_error_for_non_numeric_unit_price(self):
        with pytest.raises(ValueError):
            summarize_order([{"quantity": 1, "unit_price": "five"}])


class TestIsValidProjectCode:
    def test_valid_code(self):
        assert is_valid_project_code("AB-1234") is True

    def test_invalid_lowercase_prefix(self):
        assert is_valid_project_code("ab-1234") is False

    def test_invalid_prefix_length(self):
        assert is_valid_project_code("ABC-1234") is False

    def test_invalid_number_length(self):
        assert is_valid_project_code("AB-123") is False

    def test_invalid_number_not_digits(self):
        assert is_valid_project_code("AB-12A4") is False

    def test_invalid_missing_separator(self):
        assert is_valid_project_code("AB1234") is False

    def test_invalid_too_many_separators(self):
        assert is_valid_project_code("AB-12-34") is False

    def test_invalid_non_string_input(self):
        assert is_valid_project_code(1234) is False

    def test_invalid_prefix_with_non_alpha(self):
        assert is_valid_project_code("A1-1234") is False
