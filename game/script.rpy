# You can place the script of your game in this file.
init:
    image wrestling room = "Assets/wrestling-room.jpg"
    image coach = "Assets/woman.png"
    image coach flex = "Assets/woman2.png"
    image coach stretch = "Assets/woman3.png"
    image coach angry = "Assets/angry.png"
    image black = "#000"
    image player = "Assets/player.png"
    image opponent = "Assets/opponent.png"
    image opponent evil = "Assets/opponent_evil.png"
    image opponent crying = "Assets/opponent_crying.png"
    image opponent friendly = "Assets/opponent_friendly.png"
    image flames1 = "Assets/flames.png"
    image flames2 = "Assets/flames2.png"
    image judge1 = "Assets/judge1.jpg"
    image judge2 = "Assets/judge2.jpg"
    image hell = "Assets/hell.png"
    image men_dead_lock = "Assets/men_dead_lock.jpg"
    image reality = "Assets/P140_20.jpg"
    image reality2 = "Assets/woman4.jpg"
    image crazy = "Assets/images.jpg"

    python:
        special = False
        charge = False
        dodge = False
        feign = False
        lunge = False
        
        
        playerh = 10
        playerx = 0
        playery = 5

        oph = 10
        opx = 9
        opy = 5

        #transition
        pokemon = ImageDissolve("Assets/transition.png", 3, alpha=True)
# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
# Declare characters used by this game.
define e = Character('Clarissa Chun', color="#c8ffc8")
define o = Character('Wrestler', color="#00ffff")
define d = Character('Devil', color="#00ffff")


#The game starts here.
label start:
    $log = Logger("storyLoger.log")
    $char = Char()
    $op = Char()
    $time = Time()

    scene wrestling room with fade 
    pause 0.1
    scene black with dissolve
    pause 0.1
    scene wrestling room with fade 
    pause 0.1
    scene black with dissolve
    pause 0.1
    scene wrestling room with dissolve
    pause 0.1 
    show black 
    show coach angry 
    e "Pay attention!" 
    hide black dissove 

    e "You've got to focus!"

    hide coach angry
    show coach

    e "There's only a few weeks left until the qualifiers. You'd better get it togeather or else you'll be squashed."

    e "Your fat to muscle ratio already highly favors the fat end of the spectrum. Basically a child could kick your butt, flabby."

    e "Unfortunately for you, since you can't affort further services of mine, the only support you'll be getting from me is an earful. You're traning routine is your own problem."

    jump sim


label sim:
    scene wrestling room
    show coach at right 
    show screen time
    call screen sim_gui
    $action = _return
    
    if action == "sleep":
        if time.isEndOfDay():
            show black with Dissolve(4)
            "You exhaustedly flop down on your mat in the hall and fall asleep."
            if time.incDay():
                jump sim
            else:
                jump game_init
        else:
            e "You can't run away so easily fool! Get back to work!"      
            jump sim
    elif action[0] == "stat":
        call screen how_long
        if time.incHour(_return):
            if action[1] == "str":
                $char.incStat("strength", _return)
                python:
                    import random
                    option = random.randint(1,3)
                if option == 1:
                    e "Sweaty flabby! Sweat!"
                elif option == 2:
                    e "Listen to that flab jiggle!"
                elif option == 3:
                    e "You can't do it tubby, may as well give up!"
            elif action[1] == "spd":
                $char.incStat("speed", _return)
                python:
                    import random
                    option = random.randint(1,3)
                if option == 1:
                    e "Ugh you're gunna make me hurl, have you showered lately?"
                elif option == 2:
                    e "Hahahaha, I've never seen someone face-plant when runnling by falling {i}backwards{i/}. Idiot."
                elif option == 3:
                    e "I have nothing to say to you piggy."
            elif action[1] == "cun":
                $char.incStat("cunning", _return)
                python:
                    import random
                    option = random.randint(1,2)
                if option == 1:
                    e "Reading books is not going to make you better, fool."
                elif option == 2:
                    e "Hiding in the library won't save you from your fate."
            elif action[1] == "whe":
                $char.incStat("weight", _return)
                "You stuff you face with food for a few hours."
            elif action[1] == "kar":
                $char.incStat("karma", _return)
                show black with dissolve
                python:
                    import random
                    option = random.randint(1,4)
                if option == 1:
                    centered "You go for a walk and end up rescuing a dog from a tree. You feel better about yourself."
                elif option == 2:
                    centered "You escort an old lady across the street."
                elif option == 3:
                    centered "You walk though the park singing to the birds"
                elif option == 4:
                    centered "You kill a rabid cat with a chair to save a kid's bunnies. The kid gives you one of the buch. You have hosenfefer for lunch."
                hide black with dissolve
        else:
            if time.isEndOfDay():
                e "You should probably head to bed for the day."
            else:
                e "There isn't enough time left to do that today."
    jump sim
   
screen sim_gui:
    vbox:
        textbutton "Strength +" action Return(("stat","str"))
        textbutton "Speed +" action Return(("stat", "spd")) 
        textbutton "Cunning +" action Return(("stat", "cun")) 
        textbutton "Karma +" action Return(("stat","kar")) 
        textbutton "Go to bed" action Return("sleep")
        if _config.developer == True or time.getCurrentDay() == time.days_to_go:
            textbutton "Prepare for fight!" action Jump("game_init")
        
screen how_long:
    vbox:
        text "Select a time quantity."
        textbutton "1h" action Return(1)
        textbutton "4h" action Return(4)
        textbutton "8h" action Return(8)



screen time:
    frame:
        background "#ccc"
        xfill False
        yfill False
        xpos 0.76
        ypos 10
        vbox:        
            text "Day: " + str(time.getCurrentDay()) + " of "+ str(time.days_to_go) color "#000"
            hbox:
                text "Time: " color "#000"
                if time.getTime() == 0:
                    text "8:00 am" color "#000"
                elif time.getTime() == 1:
                    text "9:00 am" color "#000"
                elif time.getTime() == 2:
                    text "10:00 am" color "#000"
                elif time.getTime() == 3:
                    text "11:00 am" color "#000"
                elif time.getTime() == 4:
                    text "12:00 pm" color "#000"
                elif time.getTime() == 5:
                    text "1:00 pm" color "#000"
                elif time.getTime() == 6:
                    text "2:00 pm" color "#000"
                elif time.getTime() == 7:
                    text "3:00 pm" color "#000"
                elif time.getTime() == 8:
                    text "4:00 pm" color "#000"
                elif time.getTime() == 9:
                    text "5:00 pm" color "#000"
                elif time.getTime() == 10:
                    text "6:00 pm" color "#000"
                elif time.getTime() == 11:
                    text "7:00 pm" color "#000"
                elif time.getTime() == 12:
                    text "8:00 pm" color "#000"


