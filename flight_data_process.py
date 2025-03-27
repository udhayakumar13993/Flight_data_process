from status_value import FlightStatus
from datetime import datetime

class FlightDataProcess:

    def __init__(self):
        self.json_flight_data = [
            {"flight_number": "AZ001", 
            "departure_time": "2025-02-19 15:30",
            "arrival_time": "2025-02-20 03:45", 
            "status": FlightStatus.ON_TIME.value
            },
            {"flight_number": "AZ002",
            "departure_time": "2025-02-21 11:00",
            "arrival_time": "2025-02-21 16:00", 
            "status": FlightStatus.DELAYED.value
            },
        ]

    # Add the new flight to flight_data
    def add_flight(self,flight_details:dict)->None:

        flight_number = flight_details['flight_number']
        for flight in self.json_flight_data:
            if flight_number==flight['flight_number']:
                print(f"Flight already exists{flight_number}")
                return
        self.json_flight_data.append(flight_details)
        print(f"flight details added successfully")

    
    
    # remove the flight details
    def remove_flight(self,flight_number:str)->None:
        flight_found = False
        for flight in self.json_flight_data:
            if flight['flight_number']==flight_number:
                self.json_flight_data.remove(flight)
                flight_found=True
        if not flight_found:
            print(f"Flight number not found {flight_number}")
    
    # returns flights by status
    def flights_by_status(self, status: str) -> list[dict]:
        flights = []
        for flight in self.json_flight_data:
            
            if flight['status'] == status:
                flights.append(flight)
        
        return flights

    # get longest flight
    def get_longest_path(self)->dict:
        max_duration =0
        longest_flight = None
        
        for flight in self.json_flight_data:
            total_minutes = (datetime.strptime(flight['arrival_time'], "%Y-%m-%d %H:%M") - 
                 datetime.strptime(flight['departure_time'], "%Y-%m-%d %H:%M")).total_seconds() / 60

            if total_minutes>max_duration:
                max_duration=total_minutes
                longest_flight=flight

        return longest_flight

    # update status by flight number
    def update_status_by_number(self,flight_number:str,status:str)->None:
        flight_number_found = False
        for flight in self.json_flight_data:
            if flight['flight_number']==flight_number:
                flight['status']=status
                flight_number_found=True
                print(f"flight status for flight number:{flight_number} has been updated")
        if not flight_number_found:
            print(f"flight number {flight_number} Not found in list")
    
    # get all the flight details
    def process_all_flights(self):
        ''' Wrapper function to call all the methods'''
        self.add_flight({
            "flight_number": "AZ003",
            "departure_time": "2025-03-22 13:00",
            "arrival_time": "2025-03-22 16:00", 
            "status": FlightStatus.ON_TIME.value
            })
        self.remove_flight("AZ003")
        self.flights_by_status("DELAYED")
        self.get_longest_path()
        self.update_status_by_number("AZ001","CANCELLED")
        return self.json_flight_data

flight_data_process = FlightDataProcess()
flight_data_process.process_all_flights()













