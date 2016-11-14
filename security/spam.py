import sopel.module
from sopel.module import example, priority, rule, event
import collections
import sys
import time
from sopel.tools import iteritems, Identifier, events
from sopel.tools.target import User, Channel
import sopel.loader
import sopel.module
import subprocess
import re
import json
import random, string
import datetime
from dateutil.parser import parse as parse_date
import calendar

global justReset
justReset = 'False'

waldospam = {}

@sopel.module.rule("(.*)")
def spam(bot, trigger):
    if trigger.admin:
        exit(0)

    try:
        f = open('/home/sopel/.sopel/modules/sopel_bl', 'r')
        lastSpam = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, AttributeError):
        lastSpam = {}
 
    currenttime = calendar.timegm(trigger.time.timetuple())
    nick = u'%s' % trigger.nick.lower()
    masks = set(s for s in bot.config.core.host_blocks if s != '')

    if nick not in lastSpam:
        lastSpam[nick]=[]
        lastSpam[nick].append(0)
        lastSpam[nick].append(currenttime)
        lastSpam[nick].append(0)
        lastSpam[nick].append(0)

    if (lastSpam[nick][3] == 1 or lastSpam[nick][3] == 2) and justReset is 'True':
        global justReset
        justReset = 'False'
        lastSpam[nick][1] = currenttime

#    bot.say('Host is %s' % trigger.host)
 
    if lastSpam[nick][0] == 5:
        oldtime = datetime.datetime.utcfromtimestamp(lastSpam[nick][1])
        newtime = datetime.datetime.utcnow()
        if ( newtime - oldtime ) < datetime.timedelta(seconds=15):
            bot.say('Spam detected.  Muting you for 1 minute.  If you continue to spam the next mute will be 5 minutes.  There will be no third mute, just a 12 hour ban.')
            lastSpam[nick][0] = 0
            lastSpam[nick][1] = currenttime
            lastSpam[nick][2] += 1
            lastSpam[nick].append(trigger.host)
            bot.say('Warning Level %s' % lastSpam[nick][2])
            if lastSpam[nick][2] == 1 or lastSpam[nick][2] == 2:    
                bot.msg('chanserv', "quiet ##ha %s" % nick)
                masks.add(trigger.host)
                bot.config.core.host_blocks = list(masks)
                bot.config.save()
            elif lastSpam[nick][2] == 3:
                bot.msg('chanserv', "flags ##ha %s +b" % nick)
                masks.add(trigger.host)
                bot.config.core.host_blocks = list(masks)
                bot.config.save()
        else:
            lastSpam[nick][0] = 0
            lastSpam[nick][1] = currenttime
            lastSpam[nick][2] = 0
            lastSpam[nick][3] = 0

    for key, value in lastSpam.iteritems():
        if key == nick:
            lastSpam[key][0] += 1 

#    bot.say('Warning Level %s' % lastSpam[nick][2])

    f = open('/home/sopel/.sopel/modules/sopel_bl', 'w+')
    f.write(json.dumps(lastSpam))
    f.close()

@sopel.module.interval(2)
def checkblock(bot):
    try:
        f = open('/home/sopel/.sopel/modules/sopel_bl', 'r')
        lastSpam = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, AttributeError, IOError):
        lastSpam = {}

    masks = set(s for s in bot.config.core.host_blocks if s != '')

#    bot.msg("##ha", '2 seconds')

    for key, value in lastSpam.iteritems():
        oldtime = datetime.datetime.utcfromtimestamp(lastSpam[key][1])
        newtime = datetime.datetime.utcnow()
#        bot.msg("##ha", '%s %s' % (oldtime,newtime))
        if ( newtime - oldtime ) > datetime.timedelta(minutes=1) and lastSpam[key][2] == 1 and lastSpam[key][3] == 0:
            bot.msg('chanserv', "unquiet ##ha %s" % key)
            lastSpam[key][3] += 1
            global justReset
            justReset = 'True'
            mask = lastSpam[key][4]
            masks.remove(mask)
            bot.config.core.host_blocks = [unicode(m) for m in masks]
            bot.config.save()
            f = open('/home/sopel/.sopel/modules/sopel_bl', 'w+')
            f.write(json.dumps(lastSpam))
            f.close()
        elif ( newtime - oldtime ) > datetime.timedelta(minutes=5) and lastSpam[key][2] == 2 and lastSpam[key][3] == 1:
            bot.msg('chanserv', "unquiet ##ha %s" % key)
            lastSpam[key][3] += 1
            global justReset
            justReset = 'True'
            mask = lastSpam[key][4]
            masks.remove(mask)
            bot.config.core.host_blocks = [unicode(m) for m in masks]
            bot.config.save()
            f = open('/home/sopel/.sopel/modules/sopel_bl', 'w+')
            f.write(json.dumps(lastSpam))
            f.close()
        elif ( newtime - oldtime ) > datetime.timedelta(minutes=720) and lastSpam[key][2] == 3 and lastSpam[key][3] == 2:
            bot.msg('chanserv', "flags ##ha %s -b" % key)
            mask = lastSpam[key][4]
            masks.remove(mask)
            bot.config.core.host_blocks = [unicode(m) for m in masks]
            bot.config.save()
        elif ( newtime - oldtime ) > datetime.timedelta(minutes=1440):
            del lastSpam[key]
            f = open('/home/sopel/.sopel/modules/sopel_bl', 'w+')
            f.write(json.dumps(lastSpam))
            f.close()
#        else: 
#            bot.msg("##ha", 'nope')

@sopel.module.rule("(.*)")
def spamwaldo(bot, trigger):
    if not trigger.owner:
        exit(0)

    if trigger.nick not in waldospam:
        waldospam['waldo']=[]

    waldospam['waldo'].append(trigger.time)

    if len(waldospam['waldo']) == 3:
        firstSpam = waldospam['waldo'].pop(0)
        if (trigger.time - firstSpam).seconds <= 15:
            bot.msg('waldo', 'Relax Waldo, you got that bad habit.')
            waldospam['waldo'].append(trigger.time)
            del waldospam['waldo']
        else:
            del waldospam['waldo']


@sopel.module.rule('.*')
@sopel.module.event('JOIN')
def spamclear(bot ,trigger):
    try:
        f = open('/home/sopel/.sopel/modules/sopel_bl', 'r')
        lastSpam = json.loads(f.read())
        f.close()
    except (RuntimeError, TypeError, NameError, ValueError, AttributeError, IOError):
        lastSpam = {}

    masks = set(s for s in bot.config.core.host_blocks if s != '')

#    bot.msg("##ha", '2 seconds')

    for key, value in lastSpam.iteritems():
        oldtime = datetime.datetime.utcfromtimestamp(lastSpam[key][1])
        newtime = datetime.datetime.utcnow()
#        bot.msg("##ha", '%s %s' % (oldtime,newtime))
        if ( newtime - oldtime ) > datetime.timedelta(minutes=1) and lastSpam[key][2] == 1 and lastSpam[key][3] == 1:
            bot.msg('chanserv', "unquiet ##ha %s" % key)
            global justReset
            justReset = 'True'
        elif ( newtime - oldtime ) > datetime.timedelta(minutes=5) and lastSpam[key][2] == 2 and lastSpam[key][3] == 2:
            bot.msg('chanserv', "unquiet ##ha %s" % key)
            global justReset
            justReset = 'True'
        elif ( newtime - oldtime ) > datetime.timedelta(minutes=720) and lastSpam[key][2] == 3 and lastSpam[key][3] == 3:
            bot.msg('chanserv', "flags ##ha %s -b" % key)
