# Roadmap for Critaholic
In no particular order...

## App-level
*Near-term*
**User Authentication**
User roles for GMs and Players. A GM should have different insight into story mode, ability to create and control
initiative. A Player should have visibility into initiative and be able to see story information relevant to them.
*Long-term*
**Frontend**
Explore ways to add drag-and-drop reorder of initiative. Logos, icons, and other styling. Phase out bootstrap in favor
of something more refined.
**Admin**
Account view and encounter/session/campaign management for GMs. Super-adming panel for website admins.
**Deployment**
Packaging, availability.

## Initiative
**Tool for tracking intiative of various actors in an encounter**
* Implement a turn order field that can be used to override initiative order.
* modify the interface to allow turn order modification with buttons
* modify the interface to allow turn order sent to bottom or top
* modify the interface to allow numeric changes to the turn order
* Form validation *check*
* Notes/status field
* Encounter name or label
* Encounter level management - a list, create, delete, rename or view.

###Hopes, dreams, ambitions
* The different characters and associated powers are listed along with targets. By selecting boxes and values, such as 
    'Falkrainne', 'casts heal', 'Shaltorinn', the player can effect each other or monsters.
* multiple users creating and editing single encounter in real time (depends on user roles above)
* for list of initiative, \t or arrow or enter will highlight 'next' in turn order

## Story
Design a multi-user chat-like session. Each user participating can add a moderately sized entry (approx 100 words)
that informs the story of the session.
After implementing user roles, allow users to target limited individuals with a 'whisper'. GM has global visibility.