def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity_name = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity_name in payload

    activity = payload[expected_activity_name]
    assert "description" in activity
    assert "schedule" in activity
    assert "max_participants" in activity
    assert "participants" in activity
    assert isinstance(activity["participants"], list)
