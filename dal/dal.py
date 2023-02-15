'''
Generic DAL class uses model-specific parameters to perform CRUD operations on any model.
All methods would take as input both the model and the data to be processed, and use the model-specific parameters to perform the necessary database operations.

C - Create (create_object)
R - Read (get_object, get_all_objects)
U - Update (update object)
D - Delete (delete object)
'''

class GenericDAL:

    def __init__(self, model_class):
        self.model_class = model_class


    def create_object(self, data):
        obj = self.model_class(**data)
        obj.save()
        return obj


    def get_object(self, id):
        try:
            return self.model_class.objects.get(id=id)
        except self.model_class.DoesNotExist:
            return None


    def get_all_objects(self):
        return self.model_class.objects.all()


    def update_object(self, obj, data):
        for field, value in data.items():
            setattr(obj, field, value)
        obj.save()


    def delete_object(self, obj):
        obj.delete()
