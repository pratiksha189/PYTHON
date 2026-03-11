import calc
if __name__ == "__main__":
    print("--- Running Internal Tests ---")
    test_result = calc.add(10, 5)
    print(f"Test 10 + 5: {test_result}")
    if test_result == 15:
        print("Test Passed!")
