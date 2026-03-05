[A4-2] (https://prezi.com/view/Ry5mVQexn9oiURFBH9QM/)

## Edit a file "main.cpp"

> Complete the program main.cpp

[Problem Definition]

Write a program that asks for the weight of the package and the distance it is to be shipped, and then displays the charges.

    The Fast Freight Shipping Company charges the following rates:

| Weight of Package (in Kilograms)   | Rate per 500 Miles Shipped |
| ---------------------------------- | -------------------------- |
| 2 kg or less                       | $1.10                      |
| Over 2 kg but not more than 6 kg   | $2.20                      |
| Over 6 kg but not more than 10 k   | $3.70                      |
| Over 10 kg but not more than 20 kg | $4.80                      |

    //** Input Validation :
    //*     Do not accept values of 0 or less for the weight of the package.
    //*     Do not accept weights of more than 20 kg (this is the maximum weight the company will ship).
    //*     Do not accept distances of less than 10 miles or more than 3,000 miles.
    //*     These are the company’s minimum and maximum shipping distances.

    // Program Outline
    // Input
    //     Two Integers, weight and distance.  ( 0< weight <= 20, 10 <= distance < 3000)
    // Output
    //     the Charges, Weight,  and Distances
    // Program Logic
    //     Input statement for user input
    //     make the validation statement for the input value
    //     make the decision structure to determine the rate based on weight
    //     calculate the total charges
    //         if distance > 500, ( charges = (distance / 500) * rate);
    //         else, charges = rate;
    //     print out the **charge**.
