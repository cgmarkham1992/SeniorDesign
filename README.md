# SeniorDesign
Computer Quarto Senior Design Project

## Mike Edits
Added two 'for' loops that replace a lot of the existing code. 
I left the original commented out so you can check functionality. **ctr+f 'Mike'**
You can use the layout groups like arrays to hold buttons, then use:
```
for b in layoutGroupName.children[:]:
	b.doWhateverYouWant
```
Remember to 'git pull' before you start working on the code, or you will have merge conficts that you will have to fix before you do another 'push'

Best, mike

##11/15 Update
Created piece characteristcs as a list of touples and linked them to their respective pieces in the "available pieces" section. Also added functionality to put the touples into a list (g_playBoard) corresponding to the selected Play Location. Plans for tomorrow are to finish the Two Player game by writing win loss conditionals based on the consecutive 1 or 0 values in the g_playBoard list. An example of a win would be four pieces straight down with 1s in the second column of the g_playBoard. 

WOOT, PROGRESS!
