def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, \
       print (f"expected {expected_result}, got {actual_result}")

    #print (f"expected {expected_result} got {actual_result}")
    # ваша реализация, напишите assert и сообщение об ошибке

a=int(input())
b=int(input())
test_input_text(a,b)