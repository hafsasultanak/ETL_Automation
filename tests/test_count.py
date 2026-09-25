def test_source_target_count():
    source_count = 100
    target_count = 100

    assert source_count == target_count

def test_data_validation():
    source_cust_id = [1,2,3,4,5,5]
    target_cust_id = [1,2,3,4,5]

    assert set (source_cust_id) == set(target_cust_id)

