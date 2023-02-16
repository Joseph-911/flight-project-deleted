'''
Generic DAL methods uses model-specific to perform CRUD operations on any model.
Methods would take as input both the model and the data to be processed, and use the model-specific parameters to perform the necessary database operations.

C - Create (create_object)
R - Read (get_object, get_all_objects)
U - Update (update object)
D - Delete (delete object)
'''

class GenericDAL:
    # ---------------------------------------- #
    # ----------------- CRUD ----------------- #
    # ---------------------------------------- #
    def create_object(self, model, data):
        obj = model(**data)
        obj.save()
        return obj


    def get_object(self, model, id):
        try:
            return model.objects.get(id=id)
        except model.DoesNotExist:
            return None


    def get_all_objects(self, model):
        return model.objects.all()


    def update_object(self, obj, data):
        for field, value in data.items():
            setattr(obj, field, value)
        obj.save()


    def delete_object(self, obj):
        obj.delete()

    # ---------------------------------------- #
    # ---------------------------------------- #
    # ---------------------------------------- #
    def getAirlinesByCountry(country_id):
        pass


    def getFlightsByOriginCountryId(country_id):
        pass


    def getFlightsByDestinationCountryId(country_id):
        pass


    def getFlightsByDepartureDate(date):
        pass


    def getFlightsByLandingDate(date):
        pass

    
    def getFlightsByCustomer(customer):
        pass

    # ---------------------------------------- #
    # ---------------------------------------- #
    # ---------------------------------------- #
    def get_airline_by_username(username):
        pass
    
    
    def get_customer_by_username(username):
        pass
    
    
    def get_user_by_username(username):
        pass
    
    
    def get_flights_by_parameters(origin_counry_id, detination_country_id, date):
        pass
    
    
    def get_flights_by_airline_id(airline_id):
        pass
    
    
    def get_arrival_flights(country_id):
        pass
    
    
    def get_departure_flights(country_id):
        pass
    
    
    def get_tickets_by_customer(customer_id):
        pass
