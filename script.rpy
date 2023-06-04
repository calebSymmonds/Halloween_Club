define skelly = Character("Skelly", who_color="#ffffff")
define hayate = Character("Hayate")
define student = Character("Student")
define student_2 = Character("Student 2")
define student_3 = Character("Student 3")

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
    
    hide skelly with dissolve
    stop music fadeout 2.0
    play music "audio/My Station - No Copyright Anime Music.mp3" volume 0.25
    
    "Ding dong ding dong"

    "Finally, another day of school is over."
    
    "You decided to go to this school to hang out with your friend Hayate, but fate decided to put the two of you in different classes."
    
    "Plus it seems like everyone around you already knew each other before starting the school year, so all the friend groups were decided before your first day."
    
    "Well, at least the two of you can hang out on your way back from school."
    
    "As soon as you finally decide to stand up, though, you see him standing in the classroom doorway."
    
    hayate "Hey, name. Sorry I’m late. Did you wait long?"
    
    menu:
            "Just a little while.":
                    hayate "Oh, good! I was worried you were gonna head out before I got here!"
    
            "Where were you?!":
                    hayate "Sorry! I got caught up with something…"
    
    hayate "Listen, I won’t be able to walk home with you anymore."
    
    hayate "You know how I’ve always wanted to be a photographer? Well, this school actually has a really good photography club."
    
    hayate "Hey! Maybe you should try joining a club too! Basically all of them are looking for new members right now."
    
    "And suddenly your high school life just got worse."
    
    hayate "Why don’t you just give it a shot? I’m sure there’s gotta be something you’ll like!"
    
    hayate "Well, I’d better get going. I’ll see you tomorrow!"
    
    "As soon as he turns a corner, you feel like kicking something."
    
    "Of course, you can’t tell him that he can’t join a club just because you don’t want to be lonely."
    
    "Still, though, you joined this school to be with him! Maybe you should just join the photography club along with him."
    
    "You take a deep breath and sigh."
    
    "You can’t do that. He loves photography. You’d just get in the way."
    
    "Besides, it’s not like you’re particularly interested in taking pictures of trees or bugs or whatever they do in that club."
    
    "Actually, now that you think about it, do you have <i>any</i> interests at all?"
    
    "Well, no point worrying about that now. Might as well go home and play video games or something."
    
    "As you walk out into the school courtyard, though, you quickly realize that Hayate wasn’t kidding."
    
    "The second the sunlight hits your nose, about a dozen students gather around you with fliers."
    
    student "Hey! Are you looking for a club? Why not join the cooking club?"
    
    student _2 "He doesn’t want to join the cooking club! He wants to join the tennis club!"
    
    student_3 "You’re both wrong! He’s obviously interested in underwater basket weaving!"
    
    "You try to walk through the crowd without looking anyone directly in the eye."
    
    "It seems like there’s a club for just about everything imaginable, but none of them sound very interesting."
    
    "Actually, in all honesty, there’s probably a lot of clubs that you’d have fun doing."
    
    "It’s just that you’re not as big a fan of the people who would be in the club with you."
    
    "Even if you liked the things they’d be doing, you’d still be left out, watching from the sidelines while everyone else ignored you."
    
    "They all sound so excited to have new club members, but you know that the minute you joined, they’d forget you were even there."
    
    "Just as you’re about to walk through the school gates, though, something catches your eye."
    
    'There’s an empty table with a sign that reads: “Reserved for the Halloween Club”'
    
    "You walk up to the table and see a note printed out by the student council."
    
    '“Meeting room A-121”'
    
    "Figures. This is probably just a joke club so that a group of friends can hang out after school."
    
    "Still, though, what even <i>is</i> a Halloween Club?"

    
    menu:
        "Where do you want to go?"
        
        "The beach":
            'You were eaten by sharks and died.'
            
        "The mountains":
            "Good ending! You enjoyed a nice picnic."

    return
