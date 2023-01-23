import pandas as pd
import numpy as np

#App UI class
class UI:
    def __init__(self, df):
        self .df = df

    
    #printing the header of the items of the list with proper spacings
    '''def display_headers(self):
       
        #displaying the columns of the list with right side space formatting
        print(f"{'Pos':3} {'car_id':10} {'reg':10} {'manufacturer':10} {'model':10} {'SIPP':10} {'max_seat':10} {'Width':10} {'Length':10} {'spd':10} {'MPG':10} {'OnHire':10}")
    '''
    
        
    def display_cars(self):        
        df  = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)
        return df   
    
      


    def display_menu(self):
        return f"""Menu: 
        A - Add Car to Car Registry
        D - Delete Car from Car Registry
        H - Hire Out
        R - Return to Garage
        U - Update Car Registry


        X - Exit
        """

    def process_option(self):
        #take users imput for selecting menu option
        option = input( "Please select your option: " ).upper()
        if option ==  "A" :
            #take from car registry
            CarRegistry.add_car(self)
        elif option ==  "D" :
            CarRegistry.remove_car(self)
        elif option ==  "H" :
            CarRegistry.hire_out(self)
        elif option ==  "R" :
            CarRegistry.return_car_to_garage(self)
        elif option ==  "U" :
            CarRegistry.update_car(self)
        elif option ==  "X" :
            print( "Goodbye!! Thank you for using our application." )
        else :
            print( "Invalid option! Please Try Again!!" )
            #show the menu again
            self .display_menu()
            self .process_option()



#car registry class
class CarRegistry:

    
    
    def add_car(self):        
        df = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)
        noOfActivities = int(input( "Enter the number of cars you want to add: " ))
        for i in range(noOfActivities):
            car_id = int(input( "Entry no. "+ str(i+1) +" : Enter car id: " ))
            if car_id in df['car_id'].values:
                print( "Car id already exists" )
                continue
            reg = input("Entry no. "+ str(i+1) +" : Enter car registration: " )
            manufacturer = input( "Entry no. "+ str(i+1) +" : Enter manufacturer: " )
            model = input( "Entry no. "+ str(i+1) +" : Enter model: " )
            SIPP = input( "Entry no. "+ str(i+1) +" : Enter SIPP: " )
            max_seat = int(input( "Entry no. "+ str(i+1) +" : Enter max seat: " ))
            Width = int(input( "Entry no. "+ str(i+1) +" : Enter width: " ))
            Length = int(input( "Entry no. "+ str(i+1) +" : Enter length: " ))
            spd = float(input( "Entry no. "+ str(i+1) +" : Enter max speed: " ))
            MPG = float(input( "Entry no. "+ str(i+1) +" : Enter milage per gallon: " ))
            OnHire = False
            #asking user if they want to save the changes or not
            save = input( "Do you want to save the changes? (Y/N): " ).upper()
            if save ==  "Y" :
                df.loc[len(df)] = [car_id, reg, manufacturer, model, SIPP, max_seat, Width, Length, spd, MPG, OnHire]
                df.to_csv('CarRegistry.csv', index=False)
                print( "Car has been added" )
            elif save ==  "N" :
                print( "Car has not been added" )
                print(df)
            else :
                print( "Invalid option" )

            #print the menu and process option again
            print(self .display_menu())
            self .process_option()

                

            
            
        
            
          

   




    
    #asking user to choose the position of car to be removed from CarRegistry.csv aswell as from CarRegistry.dat file and removing it
    def remove_car(self):
        df = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)
        print(df)
        car_id = int(input( "Enter car position that you want to remove : " ))
        df.drop(car_id, inplace=True)
        df.to_csv('CarRegistry.csv', index=False)
        print( "Car has been removed" )
        print(df)
        #display menu and process option again
        print(self .display_menu())
        self .process_option()

        


        

    
    #asking user to choose car id to return to garage and changing on_hire to false if true
    #and printing message if it it already false and not changing it
    #and saving the change in same column
    def return_car_to_garage(self):
        df = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)        
        car_id = int(input( "Enter the position of the car yo want to return to garrage: " ))
        if df.loc[car_id, 'OnHire'] ==  "False" :
        
            print( "Car is already in garage" )
        else :
            df.loc[car_id, 'OnHire'] =  "False" 
            df.to_csv('CarRegistry.csv', index=False)
            print( "Car has been returned to garage" )
            print(df)
        #display menu and process option again
        print(self .display_menu())
        self .process_option()


    

   
    def hire_out(self):
        '''
        *asking user to choose car id to hire out
        *not allowing user to hire out car if on_hire is true
        '''
        df = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)
        print(df)
        car_id = int(input( "Enter the position of the car that you want to hire: " ))
        if df.loc[car_id, 'OnHire'] ==  "True" :
            print( "Car is already hired out" )
        else :
            df.loc[car_id, 'OnHire'] =  "True" 
            df.to_csv('CarRegistry.csv', index=False)
            print( "Car has been hired out" )
            print(df)
        #display menu and process option again
        print(self .display_menu())
        self .process_option()

            

    def update_car(self):
        #allowing users to update car registry by asking for car id and updating the row from csv file
        df = pd.read_csv('CarRegistry.csv', delimiter=',')
        df.index = np.arange(1, len(df)+ 1)        
        car_id = int(input( "Enter car position whose data you want to change: " ))
        df = df[df.car_id != car_id]
        df.to_csv('CarRegistry.csv', index=False)        	
        car = []
        #using loop to ask for input and append to list
        car.append(input( "Enter car_id: " ))
        car.append(input( "Enter car registration number: " ))
        car.append(input( "Enter car manufacturer: " ))
        car.append(input( "Enter car modle: " ))
        car.append(input( "Enter car sip: " ))
        car.append(input( "Enter car's no of seat: " ))
        car.append(input( "Enter car's width: " ))
        car.append(input( "Enter car length: " ))
        car.append(input( "Enter car's max speed: " ))
        car.append(input( "Enter car's milage: " ))
        car.append(input( "Enter if car is  on hire or not: " ))
        #asking user if they want to save the changes or not
        save = input( "Do you want to save the changes? Y/N: " ).upper()
        if save ==  "Y" :
            df.loc[len(df)+ 1] = car
            df.to_csv('CarRegistry.csv', index=False)
            print(df)
            #and showing menue again
            self.process_option()
        elif save ==  "N" :
            print( "Car has not been updated" )
            print(df)
            #and showing process_option menue again
            self.process_option()
        else :
            print( "Invalid option" )
            print(df)
            
            self.process_option()

    

            


        
        


        



#car class
class Car:
    def __init__(self, car_id, reg_plate, sip, manufacturer, model, seat_cap, width, length, max_speed, rangee, OnHire):
        self.car_id = car_id
        self.reg_plate = reg_plate
        self.sip = sip
        self.manufacturer = manufacturer
        self.model = model
        self.seat_cap = seat_cap
        self.width = width
        self.length = length
        self.max_speed = max_speed
        self.rangee = rangee
        self.OnHire = OnHire


#Displaying UI and MENU
car1 = UI(df=pd.read_csv('CarRegistry.csv', delimiter=','))
#print(car1.display_headers())
print(car1.display_cars())
print(car1.display_menu())

car1.process_option()




