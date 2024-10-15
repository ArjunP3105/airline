from django.test import TestCase , Client
from .models import airport,Flights 

# we created a class where we use this test case feature and in tnat a function that creates airport and flights based on the models

# Create your tests here.
class FlightTestCase(TestCase):
    def setUp(self):
        #create airport
        a1 = airport.objects.create(code = "AAA" , city = "City A")
        a2 = airport.objects.create(code = "BBB" , city = "City B")
        
        #create flight
        Flights.objects.create(origin = a1 , destination = a2 , duration = 100 )
        Flights.objects.create(origin = a1 , destination = a1 , duration = 200 )
        Flights.objects.create(origin = a1 , destination = a2 , duration = -100 )

    def test_flight_departure_count(self):
        a = airport.objects.get(code = "AAA")
        self.assertEqual(a.origin.count(),3)
    
    def test_flight_arrival_count(self):
        a = airport.objects.get(code = "AAA")
        self.assertEqual(a.destination.count(),1)
    
    def test_flights_isvalid(self):
        a1 = airport.objects.get(code = "AAA")
        a2 = airport.objects.get(code = "BBB")
        f = Flights.objects.get(origin = a1 , destination = a2 , duration = -100 )
        self.assertTrue(f.is_valid_flight())

    def test_flights_invalid(self):
        a1 = airport.objects.get(code = "AAA")
        f = Flights.objects.get(origin = a1 , destination  = a1)
        self.assertFalse(f.is_valid_flight())
    
    def test_index(self):
        c = Client()
        response = c.get("/flights/") # client().get is like fetch in js
        self.assertEqual(response.status_code,200) 
        self.assertEqual(response.context["flights"].count(),3) # here response.context["flights"] is like documment.queryselector()
        #200 means no error
        #here the we acces the client side using Client() and we get the client().get(url) the values of the url
        #like previously we can use the self.assertequal(response.status_code)
    #to check if a particular page of flight works 

    def test_particular_pages(self):
        a1 = airport.objects.get(code = "AAA")
        f = Flights.objects.get(origin = a1, destination = a1)
        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code,200)










#here we create a class test(testcases) where testcases is the code and now in here to signfy each function in the class as a test case we use prefic test_