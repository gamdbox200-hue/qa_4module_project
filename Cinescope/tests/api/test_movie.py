import pytest

class TestMoviesAPI:
    def test_get_movies_success(self, api_manager,admin_session):
        response = api_manager.movies_api.get_movies()
        assert response.status_code == 200
        movies = response.json()["movies"]
        assert isinstance(movies, list)

