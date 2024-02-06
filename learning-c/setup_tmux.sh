#!/bin/bash 


session=$1

echo $session

tmux has-session -t $session 2>/dev/null 

if [ $? != 0 ]; 
then 
	tmux new-session -d -s $session
	window = 0 # can use custom window names
	#tmux send-keys -t $session:$window '' C-m  # can use this to run multiple startup comands
fi 

tmux a -t $session

	
