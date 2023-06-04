define skelly = Character("Skelly", who_color="#ffffff")

label splashscreen: 
    "Warning: this game contains horror and frightening content." with dissolve
    play sound "audio/vpunch.mp3" volume 0.5
    "Only play if you can handle something REALLY spooky!" with vpunch
return
   
label start:
    scene bg1
    play music "audio/Naoya Sakamata.mp3" volume 0.25
    show skelly normal at truecenter

    skelly "Welcome to the Halloween Club visual novel!"

    skelly "This project is still in development. We appreciate your patience at this time."
    
    menu:
        "Where do you want to go?"
        
        "The beach":
            'You were eaten by sharks and died.'
            
        "The mountains":
            "Good ending! You enjoyed a nice picnic."

    return
