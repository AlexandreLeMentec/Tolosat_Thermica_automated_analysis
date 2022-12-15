# Tolosat_Thermica_automated_analysis
The goal is to create a python program that automates the task of analyzing each card configuration inside the Tolosat cube-sat.
The model file used for this program is accessible as the name of the variable is key in our program, hence the need for a unique set of names.
The program used is Systema, airbus's own analysis software in the field of satellite engineering. We're mainly focusing on the Thermal aspect as for this project.
This code is using the integrated python library of systema.

The following code, mission and model is an intellectual property of Tolosat and should not be copied or used without the proper consent of the Tolosat Bureau.


**alter_pos**(card,height)
>>Function that changes the height of the card. For example, alter_pos('AOCS',-0.02) will change the AOCS board 2 cm in the negative direction.

**swap_pos**(car1,card2)
>>Function that swaps the position of the two cards provided. For example, swap_pos('AOCS','Iridium') will change the positions of these two boards.
