Feature:the user wants to move Draggable element
Scenario: the user moves the  Draggable element
  Given The user accesses the page https://qavbox.github.io/demo/dragndrop/
  When  The user move the"Drag me to my target" into the droppable element on the home page
  Then  The message "Dropped" is displayed