# Lesson-12-Testing-Debugging-Exeptions

# Calculater appear.in
* show

# Mandatory 
* anybody answered anything?



# Soup and bug Analogy
* How to deal with bugs in soup?
    * Put a led on
        * (Defensive programming, being very carefull)
    * Close your eys and eat it
        * ..
    * Its high protien, so enjoy it  

# Debugging  

## Grace Hopper
 * Bug being found


# Print() approach

````python

    def add_numbers_x_times(num, x):
        for i in range(x):
            num += num

    add_numbers_x_times(10, 80)

````



# Error msg 

< Show in the interpretor

* Index Errors
  * Trying to access beond the limit of a list
    * test = [1, 2, 3] then test[4]
* Type Errors
  * Trying to convert an inappropiate type
    * int(Test)
  * Mixing Data types without appropiate coercion
    * '3'/4 
* Name Errors
  * Referencing a non-existing variable, function ie.
    * a
* AttributeErrors
  * object has no attribute
* Syntax Errors
  * a = len([1, 2, 3,]  =>  print(a)
* ValueError

## Logic Errors

## Rubber duck debugging
> Search for Rubber duck debugging
* Explain your code to someone that does not know anything.
  * Forces you to think about in detail what you did

## Black box testing
based on docstring  
* exercise black box testing

 ## Glass Box Testing
Code is visible  
* Exercise: Glass Box Testing

Guidelines
* Branches
    * exercise all parts of conditions (if else)


````python

    if month == 1:
        if day <= 20:
            return "Capricorn")
        else:
            print("Aquarius")

    elif month == 5:
        if day <= 21:
            print("Taurus")
        else:
            print("Gemini")
    else:
        if day <= 21:
            print("Sagittarius")
        else:
            print("Capricorn")  

````

* for loops
have a test case where:
    * loop not entered
    * Loop entered exactly once
    * Body of loop excuted more than once
* While loops
    * same as for loops, cases tht catch all ways to exit loop
