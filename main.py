from shape_manager import ShapeManager
def show_menu():
    print("to Add shape press: 1")
    print("to Show all shapes press: 2")
    print("to Update shape press: 3")
    print("to Delete shape press: 4")
    print("to Exit press: 5")

def choice():
    my_choice=0
    while my_choice>5 or my_choice<1:
        try:
            my_choice=int(input("Enter your choice "))
            if my_choice>5 or my_choice<1:
                print("number must be between 1 and 5")
                continue
        except:
            raise TypeError("type illegal to casting")
    return my_choice

def main():
    #https://github.com/Davidspiller185/CRUD_SHAPE
    show_menu()
    my_choice=0
    while my_choice !=5:
        my_choice=choice()
        lst_shapes=["circle","hexagon","rectangle","square","triangle"]
        shape=ShapeManager()
        match my_choice:
            case 1:
                type_shape=input("Enter shape type ")
                while type_shape not in lst_shapes:
                    print("invalid shape")
                    type_shape=input("Enter shape type ")
                shape.create_shape(type_shape)
            case 2:
                print(shape.get_all_shapes())
            case 3:
                print(shape.get_all_shapes())
                id=int(input("Enter number id "))
                file=input("Enter the file you want update ")
                value=int(input("Enter the value you want update "))
                new_data={file:value}
                shape.update_shape(id,new_data)
            case 4:
                id=int(input("Enter number id "))
                shape.delete_shape(id)
            case 5:
                print("the CRUD SHAPE are finich")
if __name__=="__main__":
    main()



        


            


        

