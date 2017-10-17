# Roadmap for Critaholic
In no particular order...

## Critaholic
**The entire suite of tools**

###High
* The GM or GM's should have a visibility definition above Players (user roles) that define the information that can be 
    seen, the changes that can be made, or the control of different entities. **User Authentication**
    
###Low
* Update the templates to use bootstrap service from CDN
* Admin panel from a superuser perspective and a GM's perspective

## Initiative
**Tool for tracking intiative of various actors in an encounter**
* Implements a turn order field
* modify the interface to allow turn order modification with buttons
* modify the interface to allow turn order sent to bottom or top
* modify the interface to allow numeric changes to the turn order

###High
* Form validation *check*
* Behavior for delaying or holding an action
* Notes field
* Encounter name or label
* unique urls or slugs

###Future (Angular JS frontend)
* The different characters and associated powers are listed along with targets. By selecting boxes and values, such as 
    'Falkrainne', 'casts heal', 'Shaltorinn', the player can effect each other or monsters.
* multiple users creating and editing single encounter in real time (depends on user roles above)
* for list of initiative, \t or arrow or enter will highlight 'next' in turn order

## Party
**Character notes and details for PC's and critical NPC's in party**

* Character model and form
* Ownership (depends on user roles above)

## Hero
**Powers and abilities for individual PC's**

* Ability model and form
* Ability linked to item, modifying ability when used in encounter

## Backpack
**Items and their powers/benefits for PC's, NPC's, or other entities.**

* Item model and form
* Item association with Ability and Character, one-to-many

## Frontend changes
**Implement AngularJS as a frontend app**