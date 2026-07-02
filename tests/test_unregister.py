def test_unregister_success_removes_student(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": existing_email}
    )
    get_response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from {activity_name}"
    participants = get_response.json()[activity_name]["participants"]
    assert existing_email not in participants


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    unknown_activity = "Gardening Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(f"/activities/{unknown_activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_not_signed_up_student_returns_404(client):
    # Arrange
    activity_name = "Programming Class"
    absent_email = "notasigned@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": absent_email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"


def test_unregister_missing_email_returns_422(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/unregister")

    # Assert
    assert response.status_code == 422
