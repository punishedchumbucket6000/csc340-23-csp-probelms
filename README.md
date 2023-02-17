# csc340-23-csp-probelms

## Part 1
Follow along in class to solve the Australia coloring problem. Namely, using the colors red, green, and blue color all the states such that no adjacent states have the same color. 

X = {WA, NT, Q, NSW, V, SA, T}

D = {red, green, blue} //same for each X

C = {SA != WA, SA != NT, SA != Q, SA != NSW, SA != V, WA != NT, NT != NSW, NSW != V}


## Part 2
On your own, figure out this scheduling problem.

You are trying to schedule workers for the coming week. Some workers can only work on certain days. Also, some workers to not get along with each other, so they cannot work on the same day. Also, you have a husband and wife you need to work together on the same day, and a new trainee who needs to work with one of two trainers.

Here are your domains:
* Alice can work Mon, Wed, and Fri
* Bob can work Mon and Tue
* Charlie can work Tue, Wed, Thu, and Fri
* Danielle can work Mon, Wed, and Fri
* Edwin can work Wed, Thu, and Fri

Here are your constraints:
* Bob has to work on the same day as Alice
* Danielle cannot work with Charlie
* Bob cannot work with Charlie
* Danielle cannot work with Edwin
* Danielle cannot work with Alice
* Edwin needs to work with either Bob or Charlie

