from fitapi.server import app
    
def test_page_exists_at_desired_location():
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200

def test_page_uses_correct_template():
    with app.test_client() as test_client:
        response = test_client.get("/")
        assert response.status_code == 200
        
        # assertTemplateUsed(response, "home.html")

def test_html():
        pass
    
