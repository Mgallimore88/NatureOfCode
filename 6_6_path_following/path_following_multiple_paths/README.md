<h1> Path Following segmented line path </h1>
The vehicles calculate their future position by looking at a normalised version of their scalar velocity.
If the future position is outside of the path's radius, the vehicle's normal to the path is calculated by looking at the scalar projection of the vehicle's position vector along the path segment vector. 
This is the red spot.
A short distance along the path a target is created, and the vehicle seek this target.
this is the green spot.
The seeking behaviour is implemented by using a steering force = current velocity - desired velocity, where desired velocity is maximum speed in the direction of the target. 

[path following video](/path_following.gif)

