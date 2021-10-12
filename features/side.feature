Feature:sidebar scrolling
Scenario: the user moves element
  Given The user accesses the page https://qavbox.github.io/demo/dragndrop/
  When  The user scrolls the sidebar up to 100
  Then  The range 100 is displayed