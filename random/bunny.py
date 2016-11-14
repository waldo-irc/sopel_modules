# coding=utf-8
import sopel.module
import re
import calendar
import datetime
import time
from sopel.tools import events
import random

lastTime = {}
global running
running = 0

@sopel.module.commands('bunny')
def bunny(bot, trigger):
    if not trigger.admin:
        bot.say("Sorry, ASCII art is admin only pal.")
        exit(0)

    msg = trigger.group(2)
    x = 0
    y = 0
    xy = 0
    xyz = 0
    lines = {}
    lines['writing'] = []
    currenttime = calendar.timegm(trigger.time.timetuple())

    global running
    if running == 1:
        bot.msg(trigger.nick, "Bunny already running.  Must wait for end.")
        exit(0)

    running = 1

#    bot.say('%s' % lastTime)

#    try:
#        oldtime = datetime.datetime.utcfromtimestamp(lastTime['active'][0])
#        newtime = datetime.datetime.utcnow()
#        if ( newtime - oldtime ) < datetime.timedelta(seconds=10):
#            exit(0)
#        else:
#            del lastTime['active']
#    except KeyError:
#        lastTime['active'] = []
#        lastTime['active'].append(currenttime)    
    
#    bot.say('%s' % lastTime)

    for line in msg.split('\\n'):
        y = 0
        for i in line:
            y+=1
#        bot.say('%s' % y)
#        bot.say('%s' % xy)
        if xy == 0:
            xyz = y
        elif xy < y:
           xyz = y
        xy = y
 
#    bot.say(u'%s is longest string' % xyz)

    for line in msg.split('\\n '):
        if '\\n' in line:
            bot.say('Space required after \\n')
            exit(0)
        x+=1
        if len(line) > 31:
            bot.say("%s Line is too long.  31 characters max per line." % line)
            exit(0)
        if len(line) < 31:
            #spaces = 11 - len(line)
            spaces = (xyz + 4) - len(line)
            if spaces % 2 == 0:
                spaces = spaces/2
                line = (' ' * (spaces + 1)) + line + (' ' * spaces)
            else:
                spaces = (spaces/2) + 1
                line = (' ' * spaces) + line + (' ' * spaces)
        lines['writing'].append(line)

    if x > 5:
        bot.say("Can only do 5 new lines max.")
        exit(0)

    
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('￣' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('￣' * (((xyz + 4)/2) + 1)))
    for line in lines['writing']:
        bot.msg("##ha", '|%s|' % line)
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('＿' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('＿' * (((xyz + 4)/2) + 1)))
    bot.msg("##ha", '(\__/) ||')
    bot.msg("##ha", '(•ㅅ•) ||')
    bot.msg("##ha", '/ 　 づ')
 
    global running
    running = 0

@sopel.module.commands('cat')
def cat(bot, trigger):
    if not trigger.admin:
        bot.say("Sorry, ASCII art is admin only pal.")
        exit(0)

    msg = trigger.group(2)
    x = 0
    y = 0
    xy = 0
    xyz = 0
    lines = {}
    lines['writing'] = []
    currenttime = calendar.timegm(trigger.time.timetuple())

    global running
    if running == 1:
        bot.msg(trigger.nick, "Bunny already running.  Must wait for end.")
        exit(0)

    running = 1

#    bot.say('%s' % lastTime)

#    try:
#        oldtime = datetime.datetime.utcfromtimestamp(lastTime['active'][0])
#        newtime = datetime.datetime.utcnow()
#        if ( newtime - oldtime ) < datetime.timedelta(seconds=10):
#            exit(0)
#        else:
#            del lastTime['active']
#    except KeyError:
#        lastTime['active'] = []
#        lastTime['active'].append(currenttime)    
    
#    bot.say('%s' % lastTime)

    for line in msg.split('\\n'):
        y = 0
        for i in line:
            y+=1
#        bot.say('%s' % y)
#        bot.say('%s' % xy)
        if xy == 0:
            xyz = y
        elif xy < y:
           xyz = y
        xy = y
 
#    bot.say(u'%s is longest string' % xyz)

    for line in msg.split('\\n '):
        if '\\n' in line:
            bot.say('Space required after \\n')
            exit(0)
        x+=1
        if len(line) > 31:
            bot.say("%s Line is too long.  31 characters max per line." % line)
            exit(0)
        if len(line) < 31:
            #spaces = 11 - len(line)
            spaces = (xyz + 4) - len(line)
            if spaces % 2 == 0:
                spaces = spaces/2
                line = (' ' * (spaces + 1)) + line + (' ' * spaces)
            else:
                spaces = (spaces/2) + 1
                line = (' ' * spaces) + line + (' ' * spaces)
        lines['writing'].append(line)

    if x > 5:
        bot.say("Can only do 5 new lines max.")
        exit(0)

    
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('￣' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('￣' * (((xyz + 4)/2) + 1)))
    for line in lines['writing']:
        bot.msg("##ha", '|%s|' % line)
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('＿' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('＿' * (((xyz + 4)/2) + 1)))
    bot.msg("##ha", '         ||')
    bot.msg("##ha", '(> ” ” <)||')
    bot.msg("##ha", '( =’o\'= )||')
    bot.msg("##ha", '-(,,)-(,,)- ')
 
    global running
    running = 0

@sopel.module.commands('toad')
def toad(bot, trigger):
    if not trigger.admin:
        bot.say("Sorry, ASCII art is admin only pal.")
        exit(0)

    msg = trigger.group(2)
    x = 0
    y = 0
    xy = 0
    xyz = 0
    lines = {}
    lines['writing'] = []
    currenttime = calendar.timegm(trigger.time.timetuple())

    global running
    if running == 1:
        bot.msg(trigger.nick, "Bunny already running.  Must wait for end.")
        exit(0)

    running = 1

#    bot.say('%s' % lastTime)

#    try:
#        oldtime = datetime.datetime.utcfromtimestamp(lastTime['active'][0])
#        newtime = datetime.datetime.utcnow()
#        if ( newtime - oldtime ) < datetime.timedelta(seconds=10):
#            exit(0)
#        else:
#            del lastTime['active']
#    except KeyError:
#        lastTime['active'] = []
#        lastTime['active'].append(currenttime)    
    
#    bot.say('%s' % lastTime)

    for line in msg.split('\\n'):
        y = 0
        for i in line:
            y+=1
#        bot.say('%s' % y)
#        bot.say('%s' % xy)
        if xy == 0:
            xyz = y
        elif xy < y:
           xyz = y
        xy = y
 
#    bot.say(u'%s is longest string' % xyz)

    for line in msg.split('\\n '):
        if '\\n' in line:
            bot.say('Space required after \\n')
            exit(0)
        x+=1
        if len(line) > 31:
            bot.say("%s Line is too long.  31 characters max per line." % line)
            exit(0)
        if len(line) < 31:
            #spaces = 11 - len(line)
            spaces = (xyz + 4) - len(line)
            if spaces % 2 == 0:
                spaces = spaces/2
                line = (' ' * (spaces + 1)) + line + (' ' * spaces)
            else:
                spaces = (spaces/2) + 1
                line = (' ' * spaces) + line + (' ' * spaces)
        lines['writing'].append(line)

    if x > 5:
        bot.say("Can only do 5 new lines max.")
        exit(0)

    
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('￣' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('￣' * (((xyz + 4)/2) + 1)))
    for line in lines['writing']:
        bot.msg("##ha", '|%s|' % line)
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('＿' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('＿' * (((xyz + 4)/2) + 1)))
    bot.msg("##ha", '       … @ @..')
    bot.msg("##ha", '      ..(‘o‘)..')
    bot.msg("##ha", '      .º(__)º.')
 
    global running
    running = 0

@sopel.module.commands('0fucks')
def fucks(bot, trigger):
    if not trigger.admin:
        bot.say("Sorry, ASCII art is admin only pal.")
        exit(0)

    msg = trigger.group(2)
    x = 0
    y = 0
    xy = 0
    xyz = 0
    lines = {}
    lines['writing'] = []
    currenttime = calendar.timegm(trigger.time.timetuple())

    global running
    if running == 1:
        bot.msg(trigger.nick, "Bunny already running.  Must wait for end.")
        exit(0)

    running = 1

#    bot.say('%s' % lastTime)

#    try:
#        oldtime = datetime.datetime.utcfromtimestamp(lastTime['active'][0])
#        newtime = datetime.datetime.utcnow()
#        if ( newtime - oldtime ) < datetime.timedelta(seconds=10):
#            exit(0)
#        else:
#            del lastTime['active']
#    except KeyError:
#        lastTime['active'] = []
#        lastTime['active'].append(currenttime)

#    bot.say('%s' % lastTime)

    for line in msg.split('\\n'):
        y = 0
        for i in line:
            y+=1
#        bot.say('%s' % y)
#        bot.say('%s' % xy)
        if xy == 0:
            xyz = y
        elif xy < y:
           xyz = y
        xy = y

#    bot.say(u'%s is longest string' % xyz)

    for line in msg.split('\\n '):
        if '\\n' in line:
            bot.say('Space required after \\n')
            exit(0)
        x+=1
        if len(line) > 31:
            bot.say("%s Line is too long.  31 characters max per line." % line)
            exit(0)
        if len(line) < 31:
            #spaces = 11 - len(line)
            spaces = (xyz + 4) - len(line)
            if spaces % 2 == 0:
                spaces = spaces/2
                line = (' ' * (spaces + 1)) + line + (' ' * spaces)
            else:
                spaces = (spaces/2) + 1
                line = (' ' * spaces) + line + (' ' * spaces)
        lines['writing'].append(line)

    if x > 5:
        bot.say("Can only do 5 new lines max.")
        exit(0)


    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('￣' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('￣' * (((xyz + 4)/2) + 1)))
    for line in lines['writing']:
        bot.msg("##ha", '|%s|' % line)
    if xyz % 2 == 0:
        bot.msg("##ha", '|%s |' % ('＿' * ((xyz + 4)/2)))
    else:
        bot.msg("##ha", '|%s|' % ('＿' * (((xyz + 4)/2) + 1)))
    bot.msg("##ha", '(づ｡◕‿‿◕｡)づ')

    global running
    running = 0

@sopel.module.interval(30)
def checkrunning(bot):
    global running
    running = 0

@sopel.module.rule('.*')
@sopel.module.event('JOIN')
def newjoin(bot, trigger):
    if trigger.nick == bot.nick:
        exit(0)
    bot.say("Welcome to our channel %s!  If no one is around stick around and we'll get here. Run !help for a list of commands." % trigger.nick)
    chance = random.randint(1,3)
    if chance == 1:
        bunny2(bot, trigger)
    elif chance == 2:
        cat2(bot, trigger)
    else:
        toad2(bot, trigger)

@sopel.module.interval(30)
def checkrunning(bot):
    global running
    running = 0
