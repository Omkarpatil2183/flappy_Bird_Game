#bird.py
import pygame as pg

class Bird(pg.sprite.Sprite):
    def __init__(self,scale_factor):
        super(Bird,self).__init__()
        self.img_list=[pg.transform.scale_by(pg.image.load("assets/birdup.png").convert_alpha(),scale_factor),
                        pg.transform.scale_by(pg.image.load("assets/birddown.png").convert_alpha(),scale_factor)]
        self.image_index=0
        self.image=self.img_list[self.image_index]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=10
        self.flap_speed=250
        self.anim_counter=0
        self.update_on=False

    def update(self,dt):
        if self.update_on:
            self.playAnimation()
            self.applyGravity(dt)

            if self.rect.y<=0 and self.flap_speed==250:
                self.rect.y=0
                self.flap_speed=0
                self.y_velocity=0
            elif self.rect.y>0 and self.flap_speed==0:
                self.flap_speed=250

    
    def applyGravity(self,dt):
        self.y_velocity+=self.gravity*dt
        self.rect.y+=self.y_velocity
    
    def flap(self,dt):
        self.y_velocity=-self.flap_speed*dt
    
    def playAnimation(self):
        if self.anim_counter==5:
            self.image=self.img_list[self.image_index]
            if self.image_index==0: self.image_index=1
            else: self.image_index=0
            self.anim_counter=0
        
        self.anim_counter+=1



        """
from pymongo import MongoClient

# Replace <password> with your database password and <dbname> with your database name
connection_string = "mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority"
client = MongoClient(connection_string)

# Connect to the database
db = client.get_database('<dbname>')
collection = db['<collection_name>']

def save_high_score(username, score):
    high_score = {
        "username": username,
        "score": score
    }
    collection.insert_one(high_score)

def get_top_high_scores():
    top_scores = collection.find().sort("score", pymongo.DESCENDING).limit(10)
    return list(top_scores)

def update_high_score(username, new_score):
    collection.update_one(
        {"username": username},
        {"$set": {"score": new_score}}
    )
    
"""