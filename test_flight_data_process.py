import unittest
from datetime import datetime
from flight_data_process import FlightDataProcess
from status_value import FlightStatus

class TestFlightDataProcess(unittest.TestCase):
    
    def setUp(self):
        #setting up the fixtures for all the methods under Flight data process class
        self.flight_process = FlightDataProcess()
        self.test_add_flight_data = {
            "flight_number": "AZ003",
            "departure_time": "2025-03-22 13:00",
            "arrival_time": "2025-03-22 16:00", 
            "status": FlightStatus.ON_TIME.value
            }

    def test_add_flight(self):
        '''Test for adding new flight details'''
        
        add_flight = self.flight_process.add_flight(self.test_add_flight_data)

        self.assertIn(self.test_add_flight_data,self.flight_process.json_flight_data)
    
    def test_remove_flight(self):
        ''' Test for Remove flight details'''
        add_flight = self.flight_process.add_flight(self.test_add_flight_data)
        
        self.flight_process.remove_flight("AZ003")

        self.assertNotIn(self.test_add_flight,self.flight_process.json_flight_data)
    
    def test_flights_by_status(self):
        ''' Test for getting flights by status'''
        self.flight_process.add_flight(self.test_add_flight_data)

        on_time_flight = self.flight_process.flights_by_status(FlightStatus.ON_TIME.value)
        self.assertTrue(all(flight['status']==FlightStatus.ON_TIME.value for flight in on_time_flight))

        delayed_flight = self.flight_process.flights_by_status(FlightStatus.DELAYED.value)
        self.assertTrue(all(flight['status']==FlightStatus.DELAYED.value for flight in delayed_flight))
    
    def test_longest_duration(self):
        ''' Test longest flight'''
        
        longest_flight = self.flight_process.get_longest_path()
        
        excepted_flight = {"flight_number": "AZ001", 
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45", 
            "status": FlightStatus.ON_TIME.value
            }
        
        self.assertEqual(longest_flight,excepted_flight)

    def test_update_flight_by_status(self):
        
        ''' Test Update flight by status'''

        update_flight_value = self.flight_process.update_status_by_number("AZ001","CANCELLED")
        
        self.assertEqual(self.flight_process.json_flight_data[0]['status'],FlightStatus.CANCELLED.value)

        
        
