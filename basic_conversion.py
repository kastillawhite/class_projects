def convert(mi_measurement):
    
    #the conversion from miles to meters is 1 mi = 1309.34 m
    #the conversion from meters to centimeters is 1 m = 100 cm
    #therefore the conversion from miles to cm is 1 mi = 130934.4cm
    
    if mi_measurement < 5:
        
        #if the user inputs a float less than 5
        #convert() converts it into cm
    
        cm_measurement = mi_measurement * 160934.4
        convert_measurement = int(cm_measurement)
        print('Your rounded centimeter conversion is:')
        
    else:

        #if the user inputs a float great than 5
        #convert() converts it into m
        
        m_measurement = mi_measurement * 1609.34
        convert_measurement = int(m_measurement)
        print('Your rounded meter conversion is:')

    #converted the float back into an integer form for a neater number

    return convert_measurement



print('Welcome to the miles centimeter or meter conversion!\n')

mi_measure = float(input('To get a centimeter conversion, enter a mile measurement that is less than 5, for a meter conversion input any mile measurement greater than five!: '))

mi_measure = convert(mi_measure)

print(mi_measure)

print('\nThank you for using this converter!')
