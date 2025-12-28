import pytest
import os

def test_word_count_output():
    output_path = "/app/output.txt"
    input_path = "/app/input.txt"

    # Fail if output.txt is missing
    assert os.path.exists(output_path), "Output file /app/output.txt is missing"

    # Read input to calculate expected values
    with open(input_path, "r") as f:
        content = f.read()
        lines = content.strip().splitlines()
        expected_line_count = len(lines)
        # Using split() handles multiple spaces correctly as per wc -w
        expected_word_count = len(content.split()) 

    # Read output validation
    with open(output_path, "r") as f:
        output_data = {}
        for line in f:
            if ":" in line:
                key, value = line.split(":", 1)
                output_data[key.strip()] = value.strip()
            else:
                pytest.fail(f"Malformed line in output: {line.strip()}")

    # Validate output format
    assert "lines" in output_data, "Output missing 'lines' key"
    assert "words" in output_data, "Output missing 'words' key"

    # Validate values match input
    try:
        actual_lines = int(output_data["lines"])
        actual_words = int(output_data["words"])
    except ValueError:
        pytest.fail("Output values must be integers")

    assert actual_lines == expected_line_count, f"Line count mismatch: expected {expected_line_count}, got {actual_lines}"
    assert actual_words == expected_word_count, f"Word count mismatch: expected {expected_word_count}, got {actual_words}"

    # Ensure output.txt is not empty (implicit in format check but good to be explicit)
    assert os.path.getsize(output_path) > 0, "Output file is empty"
