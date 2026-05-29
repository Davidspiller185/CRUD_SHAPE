from circle import Circle
from hexagon import Hexagon
from rectangle import Rectangle
from square import Square
from triangle import Triangle
import json
class ShapeManager:
    id=0
    def __init__(self):
        self.shapes = self.load_from_json()
    def create_shape(self, shape):
        if shape == "circle":
            try:
                radius=float(input("Enter a radius "))
            except:
                raise ValueError("invalid radius")
            ShapeManager.id+=1
            circ1=Circle(ShapeManager.id,shape,radius)
            self.shapes.append(circ1.to_dict())
            self.save_to_json()
            print("sucsses to create circle shape")
        elif shape=="hexagon":
            try:
                side=float(input("Enter the side "))
            except:
                raise ValueError("invalid side")
            ShapeManager.id+=1
            hex1=Hexagon(ShapeManager.id,shape,side)
            self.shapes.append(hex1.to_dict())
            self.save_to_json()
            print("succsses to create hexagon shape ")
        elif shape=="rectangle":
            try:
                width=float(input("Enter width rectangle " ))
                height=float(input("Enter height rectangle "))
            except:
                raise ValueError("incorrect value for rectangle")
            ShapeManager.id+=1
            rec1=Rectangle(ShapeManager.id,shape,width,height)
            self.shapes.append(rec1.to_dict())
            self.save_to_json()
            print("succsses to create rectangle shape")
        elif shape=="square":
            try:
                side=float(input("Enter the side of square "))
            except:
                raise ValueError("invalid square side")
            ShapeManager.id+=1
            square1=Square(ShapeManager.id,shape,side)
            self.shapes.append(square1.to_dict())
            self.save_to_json()
            print("succsses to create square shape")
        elif shape=="triangle":
            try:
                base=float(input("Enter base "))
                heigt=float(input("Enter height "))
                side_a=float(input("Enter side_a "))
                side_b=float(input("Enter side_b "))
                side_c=float(input("Enter side_c "))
            except:
                raise ValueError("not valid vaklue")
            ShapeManager.id+=1
            trian1=Triangle(ShapeManager.id,shape,base,heigt,side_a,side_b,side_c)
            self.shapes.append(trian1.to_dict())
            self.save_to_json()
            print("succsses to create triangle shape")

    def get_all_shapes(self):
        return self.shapes
    
    def update_shape(self, shape_id, new_data):
         flag=False
         for shape in self.shapes:
             if shape["id"] == shape_id:
                 flag=True
                 for key,value in new_data.items():
                     shape[key]=value
                     self.save_to_json()
                 break
         if flag:
             print("update succssed")
         else:
             print("the id number not excisste tu update")

                                                                                         
    def delete_shape(self, shape_id):
        flag=False
        for shape in self.shapes:
            if shape["id"]==shape_id:
                flag=True
                self.shapes.remove(shape)
                self.save_to_json()
                break
        if flag:
            print("deleted succssed")
        else:
            print("the id number not exccisste to delete")

    def save_to_json(self):
        with open("shapes.json","w",encoding="UTF-8") as f:
            json.dump(self.shapes,f,indent=4)

        
    def load_from_json(self):
        with open("shapes.json","r",encoding="UTF-8") as f:
            try:
             return json.load(f)
            except:
                raise FileNotFoundError("File not found")
            
    