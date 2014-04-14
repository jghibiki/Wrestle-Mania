label game_init:
    scene black

    #build op here 
    python:
        import random
        
        style = random.randint(1,2)
        
        #style 1 -> random loop
        #style 2 -> even distrobution
        #style 3 -> emphasis

        if style == 1:
            timeLeft = time.days_to_go * time.time_in_day
            
            while timeLeft > 0:
                optime = random.randint(0 ,8) 
                while timeLeft-optime < 0:
                    optime = random.randint(0, 8)
                
                category = random.randint(1,4)

                if category == 1:
                    if op.incStat("strength", optime):
                        timeLeft -= optime
                elif category == 2:
                    if op.incStat("speed", optime):
                        timeLeft -= optime
                elif category == 3:
                    if op.incStat("cunning", optime):
                        timeLeft -= optime
                elif category == 4:
                    if op.incStat("karma", optime):
                        timeLeft -= optime
        elif style == 2:
            op.incStat("strength", 12)
            op.incStat("speed", 12)
            op.incStat("cunning", 12)
            op.incStat("karma", 12)
        

        opanger = False

    show wrestling room
    show coach at right

    e "So time for your complmentary pep talk."
    e "You are about to be crushed."
    e "Get over it."

    show men_dead_lock at topleft 

    e "You probably think you'll look like this."
    
    hide men_dead_lock 
    show reality at topleft

    e "Think again princess."
    e "And if it's not that, it's this..."

    hide reality 
    show reality2 at topleft

    e "And when you do, I'll be like..."

    hide reality2
    show crazy at topleft

    e "So don't just get your ass kicked, make it funny."

    hide crazy
    
    e "Oh looks like your opponent is here..."

    show opponent at left

    o "Me hungry."

    o "Me eat you."

    show flames1 at right
    show flames1 at left
    show flames2 at right
    show flames2 at left

    pause 1.0

    hide oppnent
    show opponent evil with fade

    scene hell
    show opponent evil 

    d "You die now <3"

label game:
    call screen game
    $action = _return
    $winner = None
    $bonusL = None
    $bonusS = None 
    ##process players turn
    $import random
    $opsMove = random.randint(1,3)
    if opsMove == 1:
        $opsMove = "charge"
    elif opsMove == 2:
        $opsMove = "feign"
    elif opsMove == 3:
        $opsMove = "lunge"

    if action == "charge":
        if opsMove == "lunge":
            $winner = "pc"
            if random.randint(0,char.strength) > random.randint(0,op.strength):
                $bonusL = True
        elif opsMove == "feign":
            $winner = "op"
            if random.randint(0,op.strength) > random.randint(0,char.strength):
                $bonusL = True
    elif action == "feign":
        if opsMove == "charge":
            $winner = "pc"
            if random.randint(0,char.cunning) > random.randint(0,op.cunning):
                $bonusL = True
        elif opsMove == "lunge":
            $winner = "op"
            if random.randint(0,op.cunning) > random.randint(0,char.cunning):
                $bonusL = True
    elif action == "lunge":
        if opsMove == "feign":
            $winner = "pc"
            if random.randint(0,char.speed) > random.randint(0,op.speed):
                $bonusL = True
        elif opsMove == "charge":
            $winner = "op"
            if random.randint(0,op.speed) > random.randint(0,char.speed):
                $bonusL = True
    else:
        $winner = "tie"

    if winner == "pc":
        if random.randint(0,char.karma) > random.randint(0,op.karma):
            $bonusS = True
    elif winner == "op":
        if random.randint(0,char.karma) > random.randint(0,op.karma):
            $bonusS = True

    if not winner == "tie":
        if winner == "pc":
            $oph -= 0.5
            if bonusS:
                $oph -= 0.5
            if bonusL:
                $oph -= 1
            if (bonusS or bonusL) and not (bonusS and bonusL):
                "Player used [action]."
            elif (bonusS and bonusL):
                "Player used [action].{w} It's super effective."
            else:
                "Player used [action].{w} It's not very effective."
        elif winner == "op":
            $playerh -= 0.5
            if bonusS:
                $playerh -= 0.5
            if bonusL:
                $playerh -= 1
            
            if (bonusS or bonusL) and not (bonusS and bonusL):
                "The Devil used [action]."
            elif (bonusS and bonusL):
                "The Devil used [action].{w} It's super effective."
            else:
                "The Devil used [action].{w} It's not very effective."
    else:
        "Tie."
    
    if oph <= 5 and not opanger:
        $opanger = True
        hide opponent evil
        show opponent evil at left
        show coach at right
        d "Hey what's with the nut shots?"

        d "You're supposed to let me eat you. That's what the lady said she'd make you do when I agreed to put her in my will."

        e "Well, let's see what the judges have to say..."

        show judge1 at top with dissolve

        e "..."
        e "Moving on..."

        hide judge1 with dissolve 
        show judge2 at top with dissolve

        e "What about you two?"

        "*cricket* *cricket*"

        e "Oh screw this, just kill eachother already."
        
        hide judge2
        hide coach with dissolve
        hide opponent evil
        show opponent evil

    if playerh <= 0:
        jump game_over
    elif oph <= 0:
        jump win

    jump game


screen game:
    frame:
        background None

        xfill False
        yfill False

        xpos 0.4
        ypos 0.8

        hbox:
            key "j" action Return("charge")
            textbutton "Charge" action Return("charge")

            key "k" action Return("feign")
            textbutton "Feign" action Return("feign")

            key "l" action Return("lunge")
            textbutton "Lunge" action Return("lunge")
    
    vbox:
        xpos 0
        ypos 0.8

        xmaximum 200
        xminimum 200
        
        text "You: "
        $ui.bar(value=playerh, range=10, width=180)

        null height 10

        text "Opponent: "
        $ui.bar(value=oph, range=10, width=180) 
    

label game_over:
    scene black
    centered "You have been defeated and devoured by the devil."
    centered "Game Over."
    e "I told you so, why even have bothered?"

    return

label win:
    "!!!"
    show flames1
    pause 0.1
    hide flames1
    show flames2
    pause 0.1
    hide flames2
    show flames2 at left
    show flames1 at right
    pause 0.1

    d "AAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHH!!!!!!!!!!!!!"

    hide flames2
    hide flames1
    show flames1
    pause 0.1
    hide flames1
    show flames2
    pause 0.1

    hide opponent evil
    show opponent crying

    d "Why are you so strong?"

    e "Um, well strong isn't really the word. More like how are {i}you{/i} so pathetic?"

    d "B-but getting thrown around huuuurrrts."

    e "Whatever shake and make up - what a couple of babies."

    hide opponent crying
    show opponent friendly
    d "Really we can be come friends!"

    d "Yaaaaay!"

    scene black
    centered "And thus you defeated the devil in a wrestling match. As a result you became friends with the devil, who as payment for beating him, trapped you in hell forever."
    e "Heh, if you cook any longer down there you'll become bacon piggy."
    centered "Good job."
    centered "The End."

