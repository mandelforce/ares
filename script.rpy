# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Ikeda")
define b = Character("Bacz", color="#ffcc00")
define c = Character("Clay", color="#00edff")
define s = Character("Stone", color="#c8ffc8")
define d = Character("Dijkstra", color="854db7")

# =Images=
#it is important that the images all start with ID to tell RenPy that are of the same class

image ID ikeda = "Id_ikeda.png"
image ID bacz = "ID_Andreas Bacz.png"
image ID clay = "ID_Daryl Clay.png"
image ID stone = "ID_Elias Stone.png"
image ID dijkstra = "ID_Marjo Dijkstra.png"
image ikeda outro  = "ikeda outro.jpg"
image diagnostic = Text("{size=80}Diagnostic", font="visitor.ttf", text_align=0.5)

#backgrounds
#these definitions are actually not needed as I am not using abbreviated names
# image bg space = "bg space.png"
# image bg space large = "bg space large.jpg"
# image bg earth horizon = "bg earth horizon.png"
# image bg earth large = "bg earth large.jpg"
# image bg liftoff = "bg liftoff.png"
# image bg spaceshuttle = "bg spaceshuttle.png"
# image bg earth horizon = "bg earth horizon.png"
# image bg deck earth view = "bg deck earth view.png"
# image bg earth view = "bg deck astronaut.png"
# image bg deck astronaut = "bg deck astronaut.png"
# image bg deck earth = "bg deck earth.png"
# image bg deck planets = "bg deck planets.png"
# image bg deck symmetry = "bg deck symmetry.png"
# image bg earth horizon = "bg earth horizon.png"
# image bg liftoff = "bg liftoff.png"
# image bg mars ground = "bg mars ground.png"
# image bg mars ground top = "bg mars ground top.png"
# image bg mars sand storm = "bg mars sand storm.jpg"

# =Audio=

define audio.liftoff = "audio/321liftoff.mp3"
define audio.shuttlelaunch = "audio/shuttlelaunch.mp3"
define audio.marsmirage = "audio/marsmirage.mp3"
define audio.history = "audio/history.mp3"
define audio.ambient = "audio/ambient.mp3"
define audio.space = "audio/space.mp3"
define audio.space2 = "audio/space2.mp3"
define audio.strangeratmo = "audio/strangeratmo.mp3"
define audio.antimatter = "audio/antimatter.mp3"
define audio.storm = "audio/storm.mp3"
define audio.thunderstrike = "audio/thunderstrike.wav"

define audio.static1 = "audio/static1.wav"
define audio.static2 = "audio/static2.wav"
define audio.static3 = "audio/static3.wav"
define audio.staticloop = "audio/staticloop.wav"

#to have dedicated channel for the storm sfx which allows controling volume independently
#see options


# =Transitions=

# Camera flash - quickly fades to white, then back to the scene.
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# The game starts here.
label start:

#Point system for behaviour tracking
    #Gullible -  in the sense of impressionable
    #Sceptical - does not trust
    #Rational - fact-oriented, wants to find out more

    $ gullible = 0
    $ sceptical = 0
    $ rational = 0

#Checks for callbacks

    $ seenpoem = False
    $ testtheory = False

# During the game, user choices affect these points. To increase the points, use:
# $ variable += 1    (It can be any number, for instance, to give some choices more weight)

#To decrease the points:
# $ variable -= 1


#testing screens:
    #jump diagnostic #for quick testing of end screen

#Scene INTRO
    # Intro background with music and sfx - moving slowly
    show bg space large with dissolve:
        #xzoom 0.1 yzoom 0.1
        zoom 0.3 #zoom out of large picture
        xpos 0
        ypos 0
        # speed in seconds and final position
        linear 40.0 xpos 0 ypos -300

    play music marsmirage
    i "It was never supposed to end this way...{w=2.0} All our hard work and sacrifice..."
    i "I don’t know what we’ll find... but we need to understand what happened."
    scene black #fade to black

#Scene Launch
    scene bg liftoff
    with fade
    play sound liftoff

    "3...{w=1.0} 2...{w=1.0} 1...{w=1.0} 0... {p=2.0}"

    scene bg spaceshuttle
    with flash
    play sound history

    "The space shuttle spread its wings{w=0.5} one final time{w=1.0}
    for the start of a sentimental journey into history…"
    with Dissolve(1.0)



#Scene Reverse shot of earth
    scene black
    show bg earth large with dissolve:
        truecenter zoom 1.4 rotate 10.0 #initial position
        # speed in seconds and final position
        linear 7.0 zoom 0.1 rotate 0.0
    play sound shuttlelaunch
    $ renpy.pause (7.0, hard=False)
    scene black #fade to black

#Scene TCSA

    scene bg mission control with fade
    stop sound fadeout 3.0
    "Established by the regional space agencies..."
    "the Transcontinental Space Agency (TCSA) is a global alliance..."

    show happymarsians with fade
    "based on a shared vision of creating an off-world colony..."
    "where humans could live in peace and safety,"
    show riot with fade
    "free from war, hunger and disease."

#Scene Mars Landscape

    scene bg mars ground with dissolve:
        truecenter zoom 1.0 #initial position
        # speed in seconds and final position
        linear 10.0 zoom 1.5
    "The first crew of scientists tasked with setting up the Ares lab on Mars arrived a few months earlier on board Phoenix 1."
    scene black #fade to black

#Scene Ship
    scene bg deck earth view with dissolve
    $ renpy.pause (2.0, hard=False)

    "Drs. Ikeda and Stone are now on their way with fresh supplies, new tech for upgrades and repairs, and their expertise."
    play sound [ static1, static3 ]
    "But en route to Ares, Phoenix 2 encounters technical problems, causing their communications to go dark..."
    play sound static2
    "... and preventing them from receiving information from either Earth or Ares."
    play sound staticloop

    scene bg deck earth with dissolve
    show ID ikeda
    play music ambient fadein 2.0
    i "Stone… TCSA just went dark. Comms are down."

    show ID stone
    s "Switching to alpha channel. You got anything?"
    play sound [ static3, static2, static1 ]

    show ID ikeda
    i "Nada. You?"

    show ID stone
    s "Nope. What do you think happened?"

    show ID ikeda
    i "Not sure… Could be a glitch. Let’s give it a few minutes."
    i "Ares, this is Phoenix 2. We’ve lost contact with TCSA. Do you read us?"
    play sound [ static1, static3, static2, static3, staticloop ]
    $ renpy.pause (5.0, hard=False) #will wait x sec or player's click to continue, player can skip - no "hard pause"
    show ID stone
    s "Well… looks like we’re on our own."
    scene black #fade to black
    show bg mars space distance with dissolve:
        truecenter zoom 0.4 rotate 0.0 #initial position
        # speed in seconds and final position
        linear 8.0 zoom 0.5 rotate 0.0
    "Mars the Red Planet. Half the size of Earth and twice as cold."
    scene black #fade to black

#Scene Ship View
    scene bg deck astronaut with fade
    $ renpy.pause (4.0, hard=False) #will wait x sec or player's click to continue, player can skip - no "hard pause"

    show ID ikeda with dissolve
    i "Beautiful, isn’t it?"

    show ID stone
    s "Breathtaking."

    show ID ikeda
    i "Listen, I think I’m getting comms back up with Ares. I’m going to try again. Enjoy the view!"

    show ID stone
    s "Copy that."


#Scene Comms back
    scene bg deck mars space with fade
    play sound static2

    show ID dijkstra with dissolve
    d "Phoenix 2, do you hear me? Good to have you back."
    play sound static3

    show ID ikeda
    i "Good to be back. Gave us a scare. Not gonna lie…"

    show ID dijkstra
    d "I bet. Well you were out for about a month. But you’re almost here."
    hide ID dijkstra

    $ renpy.pause (3.0, hard=False) #will wait x sec or player's click to continue, player can skip - no "hard pause"

    show ID dijkstra
    d "Hey, I wanted to ask you... What was the last thing you heard from TCSA?"
    play sound static1

    show ID ikeda
    i "Routine broadcast. Nothing special. Why, did we miss anything?"

    show ID dijkstra
    d "Yeah. No, there was just… I mean, it’s probably nothing."
    hide ID dijkstra

#Choice 1 Great Pandemic info yes/no
    # Changes the save name here.
    $ save_name = "First Choice"

menu:
    "It’s probably nothing."

    "Let's talk about it later then":
        jump notell_1

    "Please tell me":
        jump dotell_1


label notell_1:
    show ID ikeda
    i "Yeah ok. Listen, let’s catch up when we get there, ok?"
    play sound static2

    show ID dijkstra
    d "Actually, I would feel better sharing it now. You remember the GP 2020 right?"

    show ID ikeda
    i "You mean the Great Pandemic of 2020?"

    jump foldback

label dotell_1:
    show ID ikeda
    i "Please tell me… "
    play sound static3

    show ID dijkstra
    d "You remember the GP 2020 right?"

    show ID ikeda
    i "You mean the \"Great Pandemic\" in the 20s?"

label foldback:

    show ID dijkstra
    d """That’s the one.{w=2.0} Well, it seems we might have gotten another one.

    Reports vary between sources... some say it’s the flu, some say it’s the end of the world. You know how it is.

    There is one virologist saying we’ve got half a million infected. Mutation possible. Kill rate unknown.

    Not sure if she is for real or some quack.
    """
    hide ID dijkstra with dissolve
    play sound staticloop

label choice1:
#comment: I first labeled like this (horrible, exactly, nowords) but changed to a much more efficient system afterwards. I kept it like this for teaching purposes.

menu:
    "Another pandemic?"

    "That is horrible!":
        jump horrible_1

    "How would that be possible?":
        jump exactly_1

    "If that is true, we’re exactly right where we started.":
        jump nowords_1

label horrible_1:
    show ID ikeda
    $ gullible += 1
    i "That is horrible." with vpunch
    play sound static1
    i "Mankind will never learn! Just proves we were right with the Ares missions."

    show ID dijkstra
    d "I don’t know that that’s necessarily the case. The information could be inaccurate. "

    show ID ikeda
    i "No! Human greed was always going to be our downfall. It was only a matter of time."

    show ID dijkstra
    d "Ikeda!"
    play sound static3

    show ID ikeda
    i "What? It’s true isn’t it."

    show ID dijkstra
    d "OK, calm down. We’ll talk about it when you get here.{w=1.0} OK?"
    play sound static2

    show ID ikeda
    i "Yeah, I’m sorry."

    show ID dijkstra
    d """It’s fine, it’s fine.{w=1.0} Listen, we’re expecting a storm right around the time you’re ready to land.

    But it probably won’t last long, maybe a few hours.

    Just get here safely and we’ll figure it out.
    """
    show ID ikeda
    i "All right, thanks for the warning."

    jump foldback_1

label exactly_1:
    show ID ikeda
    $ sceptical += 1
    i "That can’t be...{w=2.0} We did everything right. Every precaution was taken! Earth is still dark and your info must be incomplete."
    play sound static1

    show ID dijkstra
    d "Yes, we don’t have enough information. We’re waiting to get comms back on."

    show ID ikeda
    i "It was probably some kind of mix-up. I really can’t believe a repeat of the ‘20s."

    show ID dijkstra
    d "Anything is possible."

    show ID ikeda
    i "Anything. But not that.{w=2.0} Not again..."

    show ID dijkstra
    d "OK, calm down. We’ll talk about it when you get here.{w=2.0} OK?"
    play sound static3

    show ID ikeda
    i "Yeah, ok."

    show ID dijkstra
    d "Listen, we’re expecting a storm right around the time you’re ready to land."
    d "But it probably won’t last long, maybe a few hours.{w=2.0} Just get here safely and we’ll figure it out."

    show ID ikeda
    i "All right, thanks for the warning."

    jump foldback_1

label nowords_1:
    show ID ikeda
    $ rational += 1
    i "If that’s true, then after all this work... all our sacrifice... {w=2.0} we’re exactly right where we started..."
    i "We need to get comms with Earth back up to clarify asap."
    play sound static2

    show ID dijkstra
    d "Absolutely, we’re waiting to get comms back on."

    show ID ikeda
    i "Then we’ll know more from TCSA. I hope comms are up by the time we land."
    play sound static3

    show ID dijkstra
    d "Listen, about that, we’re expecting a storm right around the time you’re ready to land."
    d "But it probably won’t last long, maybe a few hours.{w=2.0} Just get here safely and we’ll figure it out."

    show ID ikeda
    i "All right, thanks for the warning."

    jump foldback_1

label foldback_1:

    show ID dijkstra
    d "See you soon!"
    play sound static1
    stop music fadeout 2.0

    scene black #fade to black
    $ renpy.pause (2.0, hard=False)

#Scene Mars, Dust storm
    scene bg mars sand storm with fade
    play marssfx storm
    "Phoenix 2 manages to land in the middle of an electrical dust storm."

#lower volume of storm atmo since we are indoors now and want some music to start soon - comment: outdated info on renpy forums made this a tough one: it needs the $ not init python

    scene bg deck mars sand storm with fade
    $ renpy.music.set_volume(0.3, 0.0, channel='marssfx')
    $ renpy.pause (5.0, hard=False)

    show ID stone with flash
    s "Hey, Ikeda?"
    play sound thunderstrike

    show ID stone
    i "Yeah?"

    show ID stone with flash
    s "Ares warned us there would be a storm, but shit, this doesn’t look good."
    s "I think we’d better sit this one out."
    hide ID stone


label choice2:

menu:
    "I think we’d better sit this one out."

    "Yeah, ok.":
        jump gullible_2

    "Oh, come on, Stone!":
        jump sceptical_2

    "Let me check our stats...":
        jump rational_2

label gullible_2:
    show ID ikeda
    $ gullible += 1
    i "Yeah, ok. I guess tomorrow is soon enough."
    jump foldback_2

label sceptical_2:
    show ID ikeda
    $ sceptical += 1
    i "Oh, come on, Stone! The Rover has seen worse. Let’s live a little!"
    jump foldback_2

label rational_2:
    show ID ikeda
    $ rational += 1
    i "Let me check our stats. {w=2.0} Windspeed: 11. Visibility: Zero."
    i "Fuck, I was hoping to talk to the Phoenix 1 crew in person...{w=1.0} we need to figure out what happened on Earth."
    jump foldback_2

label foldback_2:

    show ID stone
    s "Patience is a virtue..."
    play sound static1

    show ID ikeda
    i "So is persistence."
    i "I’m gonna talk to the crew using comms. Anything you want to ask?"

    show ID stone
    s "Ask if they have some cold beers."

    show ID ikeda
    i "Haha.."
    play sound static3
    hide ID ikeda with dissolve

    scene black #fade to black

#Scene: Interior. View of Mars storm through the window.
    scene bg deck mars sand storm with flash
    $ renpy.music.set_volume(0.1, 0.0, channel='marssfx')
    play sound thunderstrike
    $ renpy.pause (4.0, hard=False)

    show ID ikeda with fade
    i "So you’re saying...{w=1.0} you haven’t received any comms since we lost connection with TCSA?"
    play music strangeratmo fadein 10.0

    show ID clay
    c "Correct. The last information packet came in about the same time we lost contact with you and Stone."
    play sound static3

    show ID ikeda
    i "Clay, I’m trying to figure out what this is. Walk me through the last available info, will you?"

    show ID clay
    c """OK, so it’s a really funny story... I had this info packet come in, right?

    Me, Dijkstra and Bacz -- we all read it. But it wasn’t... {w=2.0} clear.

    All I can tell you is that it came from TCSA, and it said: It’s happening again. 500 thousand infected within 10-14 days.

    Patient zero unknown. Origin unknown. {w=2.0} At least at the time of the message.
    """
    play sound static1
    hide ID clay

label choice3:

menu:

    "Makes sense.":
        jump gullible_3

    "No way, that’s insane, Clay.":
        jump sceptical_3

    "Are you sure it was TCSA?":
        jump rational_3

label gullible_3:
    show ID ikeda
    $ gullible += 1
    i "Makes sense. That’s probably the reason TCSA is compromised."
    i "That’s insane, Clay. Nothing, and I mean no infection known to man spreads that fast."
    i "Are you sure it was TCSA? Who was it?"
    play sound static3

    show ID clay
    c "I’m telling you, there’s some weird shit happening. I’m almost glad I’m off that rock."

    show ID ikeda
    i "Not funny, Clay."

    show ID clay
    c "I am serious. The world is doomed."

    show ID ikeda
    i "You can’t seriously believe that."

    show ID clay
    c "If you don’t believe that yourself, then why are you on this mission?"
    play sound static1

    show ID ikeda
    i "Touché, I guess."

    show ID clay
    c "See?"

    show ID ikeda
    i "All right, all right. I will...{w=1.0} talk to you later then."

    show ID clay
    c "Yep. Oh, hey -- storm’s coming, ok? You know the drill."

    show ID ikeda
    i "I do, indeed."
    play sound static3

    jump foldback_3

label sceptical_3:
    show ID ikeda
    $ sceptical += 1
    i "That’s insane, Clay. Nothing, and I mean no infection known to man spreads that fast."

    show ID clay
    c "I don’t know, Ikeda. Ask Dijkstra, maybe she knows more."

    show ID ikeda
    i "Well, I already talked to Dijkstra earlier. I’m not really a fan of the whole doomsday vibe."
    play sound static1

    show ID clay
    c "Dijkstra likes to tell it like it is."

    show ID ikeda
    i "Well, she is a scientist. She’s kind of supposed to be that way."

    show ID clay
    c "I had a science teacher in middle school who liked to say, \"Always leave room for doubt.\""

    show ID ikeda
    i "And your point is…?"
    play sound static1

    show ID clay
    c "I don’t have a point. Just saying... {w=2.0} Don’t believe everything you hear."

    show ID ikeda
    i "Copy that. I gotta go. I will talk to you later, yeah?"

    show ID clay
    c "Yep. Oh, hey -- storm’s coming, ok? You know the drill."

    show ID ikeda
    i "I do, indeed."
    play sound static3

    jump foldback_3

label rational_3:
    show ID ikeda
    $ rational += 1
    i "Are you sure it was TCSA? Who was it?"

    show ID clay
    c "Didn’t say. It was a broadcast -- got sent to TCSS, Artemis and Ares, we all received it."
    c "Listen, maybe Bacz can tell you more. That guy’s always going on about some weird conspiracy theory."
    play sound static2

    show ID ikeda
    i "Conspiracy theory, huh? I hate that stuff..."

    show ID clay
    c "Guy’s a little bit weird. Keeps to himself, doesn’t talk much. When he does talk, he’s all cryptic and shit."

    show ID ikeda
    i "Really."

    show ID clay
    c "Yes, really."

    show ID ikeda
    i "Ok, Bacz it is. I wonder what he knows that he’s not telling us…"

    jump foldback_3

label foldback_3:

#Scene: Interior. View of Mars storm through the window.
#Fade in. Some static (sound).
    scene bg deck mars sand storm with fade
    play sound [ staticloop, static3 ]
    $ renpy.pause (5.0, hard=False)

    show ID ikeda with fade
    i "Bacz?{w=2.0} Bacz, you there?"
    play sound static2

    show ID bacz
    b "Hello.{w=2.0} Welcome to Ares."

    show ID ikeda
    i "Heeeyy, Bacz, there you are!"

    show ID bacz
    b "How did you find the landing?"
    hide ID bacz

label choice4:

menu:

    "Hahaha!":
        jump gullible_4

    "You’re kidding, right?":
        jump sceptical_4

    "Rough, with a chance of lightning.":
        jump rational_4

label gullible_4:
    show ID ikeda
    $ gullible += 1
    i "Hahaha!"
    play sound [ static1, static3 ]
    jump foldback_4

label sceptical_4:
    show ID ikeda
    $ sceptical += 1
    i "You’re kidding,{w=0.5} right?"
    play sound [ static3, static3 ]
    jump foldback_4

label rational_4:
    show ID ikeda
    $ rational += 1
    i "Rough, with a chance of lightning."
    play sound [ static3, static2 ]
    jump foldback_4

label foldback_4:

    show ID bacz
    b "Haha!{w=2.0} Rare, this storm.{w=2.0} It will last another 24 hours.{w=2.0} Maybe.
    Then it should be fine."
    play sound static2

    show ID ikeda
    i "Good to know.{w=2.0} Hey, Bacz? What do you know about this whole Pandemic 2.0 that Dijkstra and Clay are talking about?"

    show ID bacz
    b "{w=2.0}Know? I don’t know."
    b "But I have some...{w=2.0} suspicions."

    show ID ikeda
    i "Suspicions? Like something shady, you mean? What is it?"
    play sound static3

    show ID bacz
    b "Why?"
    hide ID bacz


label choice5:

menu:
    "Why?"

    "I can’t decide what to think.":
        jump gullible_5

    "I don’t believe Dijkstra and Clay.":
        jump sceptical_5

    "Don’t you think we should investigate?":
        jump rational_5

label gullible_5:
    show ID ikeda
    $ gullible += 1
    i "I can’t decide what to think."
    play sound [ static1, static3 ]
    jump foldback_5

label sceptical_5:
    show ID ikeda
    $ sceptical += 1
    i "I don’t believe Dijkstra and Clay."
    play sound [ static3, static3 ]
    jump foldback_5

label rational_5:
    show ID ikeda
    $ rational += 1
    i "Don’t you think we should investigate?"
    play sound [ static3, static2 ]
    jump foldback_5

label foldback_5:

    show ID bacz with fade
    b "OK."
    play sound static3

    show ID ikeda
    i "So…"

    show ID bacz
    b "So… {w=2.0} what?"

    show ID ikeda
    i "So… what’s your theory?"

    show ID bacz
    b "Your parents,{w=2.0} do they know you are on Mars?"
    b "Or do they think you are on the space station?"
    play sound static1

    show ID ikeda
    i "18 months on the space station. Routine.{w=2.0} Why?"

    show ID bacz
    b "And yet here you are...{w=2.0} on Mars."

    show ID ikeda
    i "What are you getting at?"

    show ID bacz
    b "TCSA is not fully transparent about Ares 2036"
    b "Why? Why the secrecy?"

    show ID ikeda
    i "Non-disclosures. I don’t know."

    show ID bacz
    b "Balance of power."
    b "Whoever controls the first colony on Mars,{w=2.0} upsets the balance of power on Earth."
    b "This has...{w=2.0} implications."
    play sound static1
    hide ID bacz

label choice6:

menu:
    "Balance of power"

    "Okay... geopolitics":
        jump gullible_6

    "That has nothing to do with a pandemic":
        jump sceptical_6

    "Tell me more...":
        jump rational_6

label gullible_6:
    show ID ikeda
    $ gullible += 1
    i "Okayyy… geopolitics and all that."
    play sound [ static3 ]

    show ID bacz
    b " Yes. All that. It should be fine."
    b "Tell me something, Ikeda."
    b "What do you believe?"

    jump foldback_6

label sceptical_6:
    show ID ikeda
    $ sceptical += 1
    i "Not sure what you’re getting at. That has absolutely nothing to do with the news about the pandemic... {w=2.0}Alleged pandemic!"
    play sound [ static1 ]

    show ID bacz
    b "If you say so. It should be fine."

    show ID ikeda
    i "Exactly! We’re gonna be fine."

    show ID bacz
    b "Tell me something, Ikeda. As a scientist,{w=2.0} what do you believe?"

    jump foldback_6

label rational_6:
    show ID ikeda
    $ rational += 1
    i "Tell me more… What do you think happened?"
    play sound [ static3, static2 ]

    show ID bacz
    b "The news about the pandemic is real. But whether the pandemic itself is real or made up -- that we don’t know."

    show ID ikeda
    i "Wait, what? Hold up. Now you sound like a conspiracy theorist!" with vpunch

    show ID bacz
    b "Theory.{w=2.0} Conspiracy."
    b "This is all...{w=2.0} speculation...{w=2.0} entertainment."
    b "I am a scientist, Ikeda.{w=2.0} So are you."
    b "What do you believe?"

    jump foldback_6

label foldback_6:

    hide ID bacz
    play sound [ static2, static1 ]

label choice7:

menu:
    "What do you believe?"

    "I’m trying to decide what to think.":
        jump gullible_7

    "I think a second pandemic is highly unlikely!":
        jump sceptical_7

    "I believe in facts.":
        jump rational_7

label gullible_7:
    show ID ikeda
    $ gullible += 1
    i "I’m trying to decide what to think. That’s why I’m talking to everyone. "
    play sound [ static3 ]

    show ID bacz
    b "Good luck with that. I’ll catch you later, Ikeda."

    show ID ikeda
    i "Let’s catch up when we’re out of this shitstorm. Have some beers, yeah?"

    show ID bacz
    b "That, I like. See you later, Ikeda."

    jump foldback_7

label sceptical_7:
    show ID ikeda
    $ sceptical += 1
    i "I think a second pandemic is highly unlikely, not within the same century! We learned from the 20s - it changed us forever."
    i "This is probably some kind of a hoax. {w=2.0} Maybe a test even."
    play sound [ static1 ]
#Theory TEST --> true
    $ testtheory = True

    show ID bacz
    b "Perhaps. But we don’t have proof. {w=2.0} Good chat, Ikeda. I’ll catch you later."

    show ID ikeda
    i "All right, catch you later, Bacz. Beer’s on me!"

    jump foldback_7

label rational_7:
    show ID ikeda
    $ rational += 1
    i "Facts. I believe in facts. But I am struggling to get to the bottom of things, because I don’t have enough information."
    play sound [ static3, static2 ]

    show ID bacz
    b "{w=2.0}  “It was six men of Indostan to learning much inclined,{w=2.0} who went to see
	the Elephant though all of them were blind{w=2.0} that each by observation{w=2.0} might
	satisfy his mind…”"

    show ID ikeda
    i "\"Six men of...\"  what now? What are you talking about?"

    show ID bacz
    b "This is a poem.{w=2.0} By Saxe. You should read it."

#Player has seen the poem --> true
    $ seenpoem = True

    show ID ikeda
    i "What? Why?"

    show ID bacz
    b "Six men who cannot see...{w=2.0} describe the shape of an elephant."

    show ID ikeda
    i "Yeah, so?"

    show ID bacz
    b "So{w=2.0} if you ever only perceive one part of a thing... {w=2.0}how can you presume to understand the whole of the thing? {w=2.0}You understand?"

    show ID ikeda
    i "I...{w=2.0} think so?"

    show ID bacz
    b "You should read it. It’s a classic."

    show ID ikeda
    i "Ok... nerd.{w=2.0} I’ll get on it."

    show ID bacz
    b "You are the nerd. I’ll catch you and Stone later. I still have some vodka."

    jump foldback_7

label foldback_7:

    scene black #fade to black

#Scene: Interior. View of Mars storm through the window.
#Fade in. Static Sound.

    scene bg deck mars sand storm2 with fade
    play sound [ staticloop ]
    $ renpy.pause (5.0, hard=False)
    stop marssfx fadeout 20.0

    show ID stone with fade
    s "Ikeda, you up? Where are you?"

    play sound static3

    show ID ikeda
    i "I’m in the viewing deck. Storm's starting to clear up."

    show ID stone
    s "It’s going to be at least another few hours to be safe."
    s "Hey, did you speak to the Phoenix 1 crew? What’s the T?"

    show ID ikeda
    i "Did you just say, \"What’s the T?\""

    show ID stone
    s "What? You don’t know the expression?"

    show ID ikeda
    i "I do. I mean, hey, no judgement. I like vintage TV too."

    show ID stone
    s "Haha... So, seriously...{w=1.0} I didn't think it would be relevant."
    s "A few days before we lost our connection to Earth and Ares, I got a message from my... {w=2.0}father."

    show ID ikeda
    i "Not sure, huh?"

    show ID stone
    s "What? Yeah, my family is kind of...{w=1.0} complicated."
    s "So my father...{w=2.0} he didn’t really get into the details...{w=2.0} but he mentioned he would get out of the city to check on my kid brother."

    show ID ikeda
    i "And he did not say why?"

    show ID stone
    s "That’s the thing. He didn’t say. But...{w=2.0} I’m thinking it could be some kind of emergency. "

    show ID ikeda
    i "And you believe that?"

    show ID stone
    s """Honestly, I don’t know what to believe.

    We need to contact Earth. There are protocols for emergencies.

    What kind of national catastrophe could impact comms like this?

    TCSA would never leave us hanging under any circumstances.

    Anyway, we need more information.{w=1.0} What did you get from the crew?
    """
    play sound [ static3 ]
    hide ID stone

label choice8:

menu:
    "What did you get from the crew?"

    "It’s a pandemic":
        jump gullible_8

    "It could be a hoax":
        jump sceptical_8

    "Different views":
        jump rational_8

label gullible_8:
    show ID ikeda
    $ gullible += 1
    i "It’s a pandemic. I don’t know enough but from talking to the Phoenix 1 crew, it’s beginning to look a lot like a repeat of the 2020 pandemic."
    i "Probably even worse."
    play sound [ static3 ]

    show ID stone
    s "Jesus."

    show ID ikeda
    i "Yep."

    show ID stone
    s "I have to reach my father. We need to know what happens to the Ares mission."

    show ID ikeda
    i "Your father? Wait, what are you talking about? Who is your father?"

    jump foldback_8

label sceptical_8:
    show ID ikeda
    $ sceptical += 1
    i "It could be some kind of hoax. There is most likely another logical explanation."
    play sound [ static1 ]

    show ID stone
    s "OK, so we’re good, right? Business as usual?"

    show ID ikeda
    i "I’d say so."

    show ID stone
    s "Good coz I was a little worried..."

    show ID ikeda
    i "But we still have to re-establish contact, though. We need to know what happens to the Ares mission."

    show ID stone
    s "We need to reach my father."

    show ID ikeda
    i "Wait, what? Why? What do you mean? Who is your father?"

    jump foldback_8

label rational_8:
    show ID ikeda
    $ rational += 1
    i "They all had a different perspective. Dijkstra’s pretty sold that this is some kind of pandemic 2.0."
    i "Clay is more of a skeptic. And Bacz is just...{w=2.0} on an entirely different wavelength."
    play sound [ static3 ]

    show ID stone
    s "OK, so we’re good. Business as usual."

    show ID ikeda
    i "I’d say so.{w=1.0} But we still have to re-establish contact, though."
    i "We need to know what happens to the Ares mission."

    show ID stone
    s "We need to reach my father."

    show ID ikeda
    i "Wait, what are you talking about? Who is your father?"

    jump foldback_8

label foldback_8:

    show ID stone
    s "{w=1.0}Eli Lucht."

    show ID ikeda
    i "Eli Lucht as in,{w=1.0} TCSA founding member Eli Lucht?{w=1.0} But..."

    show ID stone
    s "Eli... Elias"

    show ID ikeda
    i "And all this time, I thought you were some boy genius from humble roots."

    show ID stone
    s "I am a boy genius. Just... {w=1.0}not so humble."

    show ID ikeda
    i "Yeah, I got that part... haha"

    scene black #fade to black

    stop music fadeout 10.0

    scene bg mars ares with fade
    "2 months after the crews of Phoenix 1 and 2 meet each other at the Ares 2036 lab, they remain disconnected from TCSA and Earth."
    scene bg deck mars space with fade
    "With no guidance from homebase, they decide to pack up and come back to Earth."
    play music antimatter fadein 4.0

#The Earth is slowly getting closer, as the ship makes its way back home. Use transparent image and slowly zoom into earth behind ship
    scene black
    show bg earth large with dissolve:
        truecenter zoom 0.0 rotate 0.0 #initial position
        # speed in seconds and final position
        linear 8.0 zoom 0.2 rotate 0.0
    $ renpy.pause (8.0, hard=False)


    show bg earth large with dissolve:
        truecenter zoom 0.2 rotate 0.0 #initial position
        # speed in seconds and final position
        linear 8.0 zoom 0.4 rotate 0.0
    $ renpy.pause (8.0, hard=False)


    "As the Phoenix 2 and its crew of 5 head home, Ikeda can’t help but wonder what lies in store for them."

#Show Ikeda astronaut image

    show ikeda outro with fade
    i "It was never supposed to end this way... All our hard work and sacrifice, gone."
    i "I don’t know what we’ll find when we get back. But we need to understand what happened. Only then can we deal with our own future."
    scene black #fade to black

#Scoring

#The ordering of the conditions above is important, because later alternatives assume that previous ones have been false.
#In general, you want to first test if any single variable wins, then test if they're all the same, then test to see which ones tied.
#This strategy avoids several possible pitfalls in the game logic.
#check: https://www.renpy.org/wiki/renpy/doc/tutorials/Remembering_User_Choices

# computer logbook screen - or empty deck

label diagnostic:
    show diagnostic:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    $ renpy.pause (2.0, hard=False)

    show bg space large with pixellate:
        #xzoom 0.1 yzoom 0.1
        zoom 0.3 #zoom out of large picture
        xpos 0
        ypos 0
        # speed in seconds and final position
        linear 40.0 xpos 0 ypos -300


    "Phoenix log:{w=1.0} Diagnostic{w=1.0}... Subject: IKEDA"
    "Scenario:{w=1.0} Communication blackout.\n
    Information saturation:{w=1.0} No verifiable facts."
    "Contact initiation Phoenix 1 -> Phoenix 2 crewmembers:{w=1.0} Satisfactory."

    "Rating dimensions:"
    "1. Impressionable.\n
    High tendency towards acceptance of available information."
    "2. Skeptical.\n
    High tendency towards rejection of available information."
    "3. Rational.\n
    High tendency towards collecting and comparing multiple perspectives."

    "Subject scored:\n
    [gullible] points on Impressionability\n
    [sceptical] points on Skepticism\n
    [rational] points on Rationality"

    #Checks for callbacks

    "Elias Stone identity revealed."
    if seenpoem == True:
        "Elephant analogy unlocked."
    if testtheory == True:
        "Hawthorne effect possible -> review research integrity."

    scene bg mission control with fade

    "We have the data you requested..."

    if gullible > max(sceptical, rational):

        "Subject shows strong interest in the opinions of others. Indicating insufficent capacity for independent thinking."

    elif sceptical > max(gullible, rational):

        "Subject displays strong signs of skepticism, failing to deliver desirable outcomes."

    elif rational > max(gullible, sceptical):

        "Subject demonstrates rational and investigative behaviour. We are very pleased."

    elif gullible == sceptical == rational:

        "This result is technically impossible." #as there are 8 points in total

    elif gullible == sceptical:

        "Subject demonstrates erratic behaviour without a clear trend. Diagnostic findings inconclusive. We are not pleased."

    elif rational == sceptical:

        "Subject demonstrates erratic behaviour without a clear trend. Diagnostic findings inconclusive. We are not pleased."

    elif gullible == rational:

        "Subject demonstrates erratic behaviour without a clear trend. Diagnostic findings inconclusive. We are not pleased."


    else:

        "Subject demonstrates erratic behaviour without a clear trend. Diagnostic findings inconclusive. We are not pleased."


label rerun:
    stop sound fadeout 4.0
    "Rerun diagnostic?"
    scene black with fade





    # This ends the game. Thanks for travelling with us!

    return
