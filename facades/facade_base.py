from api.dal import GenericDAL 

class FacadeBase:

    def __init__(self):
        self.dal = GenericDAL()
        pass
    

    def get_all_flights(self):
        pass


    def get_flight_by_id(self, id):
        pass
    

    def get_flights_by_parameters(self, origin_country_id, destination_country_id, date):
        pass
    

    def get_all_airlines(self):
        pass
    
    
    def get_airline_by_id(self, id):
        pass
    
    
    def get_airline_by_parameters(self):
        pass
    
    
    def get_all_countries(self):
        pass
    
    
    def get_country_by_id(self, id):
        pass
    
    
    def create_new_user (self, user):
        pass
