from db import db

class CategoryModel(db.Model):
    
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key = True)
    category_name = db.Column(db.String(30))
    
    pets = db.relationship("PetModel", lazy = 'dynamic')
    @classmethod
    def find_catego_by_name(cls,name):
        return cls.query.filter_by(category_name=name).first()
    
    @classmethod
    def find_catego_by_id(cls,categoid):
        return cls.query.filter_by(id=categoid).first()
    
    def json(self):
        return {'id': self.id, 'category_name':self.category_name, "avaliable pets": [pet.json() for pet in self.pets.all()] }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()