from db import db
from models.categories import CategoryModel

class PetModel(db.Model):
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key = True)
    pet_name = db.Column(db.String(30))
    price = db.Column(db.Float(precision=2))
    info = db.Column(db.String(30))
    img_url = db.Column(db.String(30))
    seller_id = db.Column (db.Integer)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    # users = db.relationship('UserModel')
    categories = db.relationship('CategoryModel', overlaps = "pets")
    
    
    
    
    @classmethod
    def find_pet_by_name(cls,name):
        return cls.query.filter_by(pet_name=name).first()
    
    
    @classmethod
    def find_pet_by_id(cls,pet_id):
        return cls.query.filter_by(id=pet_id).first()
    
    def json(self):
        return {'id': self.id, 'pet_name':self.pet_name, 'price':self.price, 'info':self.info, 'img_url': self.img_url, 'seller_id':self.seller_id, 'category_id':self.category_id, 'category_name': self.categories.category_name }
    
    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()