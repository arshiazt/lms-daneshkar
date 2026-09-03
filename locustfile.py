from locust import HttpUser,task,between

class BookApiUser(HttpUser):
    wait_time = between(1,3)

    @task
    def list_books(self):
        self.client.get('/blog/api/books/')

    @task
    def viewset_book_list(self):
        self.client.get('/blog/viewset/book/')

    @task
    def create_book(self):
        payload = {
            'title':'world war',
            'author':1
        }
        headers = {
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzg4NDU1NDQyLCJpYXQiOjE3ODg0NTUxNDIsImp0aSI6IjQyMjU0YzBjOTU1YTRlMjY4NWVhYTMzYTEwMTE0NDhlIiwidXNlcl9pZCI6IjEiLCJpZCI6MSwiZmlyc3RfbmFtZSI6ImFyc2hpYSIsImxhc3RfbmFtZSI6InRlaHJhbmkiLCJpc19zdGFmZiI6dHJ1ZSwicGhvbmUiOiIwOTkyMjgwMDMwMSJ9.-ElAH-J5RhzUQyRotSfSx1zRM0elPaNzY5K3VLNXLA8'
        }
        self.client.post('/blog/viewset/book/',json=payload,headers=headers)